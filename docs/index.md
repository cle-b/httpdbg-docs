# httpdbg

Welcome to the _httpdbg_'s documentation!

_httpdbg_ is a tool to trace the HTTP(S) client requests in your python code.

![httpdbg web interface](img/pytest1.png)

## simple

Simplicity is the keyword of _httpdbg_. It requires:

 * no external dependency
 * no setup
 * no super user right
 * no code modification

## powerful

Simple doesn't mean basic:

  * the HTTP request initiator is reported for each request

## integrated

Theorically, all pure python HTTP client libraries are fully traceable by _httpdbg_. 

Some of them have a special integration for more information:

 * [requests](https://pypi.org/project/requests/)
 * [httpx](https://pypi.org/project/httpx/)
 * [aiohttp](https://pypi.org/project/aiohttp/)
 * [urllib3](https://pypi.org/project/urllib3/)

Some test frameworks are also supported to provide additional information:

 * [pytest](https://pypi.org/project/pytest/)
 * [unittest](https://docs.python.org/3/library/unittest.html)

Some extensions are available for different famous Python tools:

  * [pytest-httpdbg](https://github.com/cle-b/pytest-httpdbg) for [pytest](https://pypi.org/project/pytest/)
  * [notebook-httpdbg](https://github.com/cle-b/notebook-httpdbg) for [notebook](https://pypi.org/project/notebook/)
