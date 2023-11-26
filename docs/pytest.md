# httpdbg - pytest

`pytest-httpdbg` is a plugin for `pytest`.

## installation

_httpdbg_ is available on _pip_.

```console
(venv) ~/$ pip install pytest-httpdbg
```

or

```console
(venv) ~/$ pip install httpdbg[pytest]
```

### compatibility

_pytest-httpdbg_ has been tested on:

 * Python `3.7`, `3.8`, `3.9`, `3.10`, `3.11`, `3.12`.
 * Pytest >= `7.0`.
 * `Linux`, `Windows`, `MacOS`.


## pyhttpdbg

The `pytest-httpdbg` plugin is mandatory to trace the HTTP requests in your tests only if you use the plugin [`pytest-xdist`](https://pypi.org/project/pytest-xdist/).

Here is an example of test file:

```python
import pytest
import requests


@pytest.fixture()
def a_post():
    return requests.post("https://httpbin.org/post", json={"demo": "in-fixture"})


def test_post(a_post):
    assert a_post.status_code == 200
    assert (
        requests.post("https://httpbin.org/post", json={"demo": "in-post"}).status_code
        == 200
    )


def test_get():
    assert requests.get("https://www.example.com").status_code == 200
```

You can use `pyhttpdbg` to execute `pytest` like for any module.

```console
pyhttpdbg -m pytest -v examples/
```

![pyhttpdbg console](img/pytest-1.png)

Open `http://localhost:4909`

![httpdbg web interface](img/pytest-2.png)

## pytest

You can use `httpdbg` to save the trace of the HTTP requests in your test report.

### usage

```
  --httpdbg             record HTTP(S) requests
  --httpdbg-dir=HTTPDBG_DIR
                        save httpdbg traces in a directory
  --httpdbg-no-clean    do not clean the httpdbg directory
  --httpdbg-initiator=HTTPDBG_INITIATOR
                        add a new initiator (package) for httpdbg
```

### generate report

For this example, we will use [`pytest-html`](https://pypi.org/project/pytest-html/) to generate the report.


You can copy the following code in your top-level `conftest.py` to include the logs into your report.

```python
import os

import pytest

from pytest_httpdbg import httpdbg_record_filename


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if call.when == "call":
        if httpdbg_record_filename in item.stash:
            extras.append(
                pytest_html.extras.url(
                    os.path.basename(item.stash[httpdbg_record_filename]),
                    name="HTTPDBG",
                )
            )
            report.extras = extras
```

_This example works if you use the same directory for the html test report files and the httpdbg logs. If this is not the case, you must adapt it to your configuration._

Run the tests using the `pytest` command.

```console
pytest examples/ --httpdbg --httpdbg-dir report  --html=report/report.html
```

![pytest console](img/pytest-report-1.png)

Open the test report in a browser.

![pytest-html](img/pytest-report-2.png)

There is a link to an HTTPDBG trace export for each test. Open it using a markdown viewer.

![httpdbg markdown export](img/pytest-report-3.png)
