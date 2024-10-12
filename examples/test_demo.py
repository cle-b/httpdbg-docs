import pytest
import requests


@pytest.fixture(scope="session", autouse=True)
def get_in_a_fixture():
    requests.get("https://httpbin.org/get/session/setup")
    yield
    requests.get("https://httpbin.org/get/session/teardown")


@pytest.fixture()
def post_in_a_fixture():
    return requests.post("https://httpbin.org/post", json={"demo": "in-fixture"})


def test_post(post_in_a_fixture):
    assert post_in_a_fixture.status_code == 200
    assert (
        requests.post("https://httpbin.org/post", json={"demo": "in-test"}).status_code
        == 200
    )


def test_get():
    assert requests.get("https://www.example.com").status_code == 200
