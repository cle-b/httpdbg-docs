import httpx


def redirect_to(url):
    return httpx.get(
        "https://httpbin.org/redirect-to", params={"url": url}, follow_redirects=True
    )
