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
