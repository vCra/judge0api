judge0api
===========

.. image:: https://img.shields.io/pypi/v/judge0api.svg
   :target: https://pypi.python.org/pypi/judge0api
   :alt: Latest PyPI version

.. image:: https://travis-ci.com/vCra/judge0api.svg?branch=master
    :target: https://travis-ci.com/vCra/judge0api

.. image:: https://api.codeclimate.com/v1/badges/f61d15c277295dbbfa46/maintainability
   :target: https://codeclimate.com/github/vCra/judge0api/maintainability
   :alt: Maintainability

.. image:: https://api.codeclimate.com/v1/badges/f61d15c277295dbbfa46/test_coverage
   :target: https://codeclimate.com/github/vCra/judge0api/test_coverage
   :alt: Test Coverage

judge0api is a Python API for interacting with the Judge0 REST API.

Usage
-----
Using this tool is super easy!

>>> import judge0api as api
>>> client = api.Client("https://api.judge0.com")
>>> submission = api.submission.submit(
...     client,
...     b"print(f'Hello {input()}')",
...     34,
...     stdin=b'Judge0',
...     expected_output=b"Hello Judge0"
... )
>>> submission.stdout
'Hello Judge0'

Installation
------------

Simply run ``pip install judge0api``

Requirements
^^^^^^^^^^^^

`Python requests
<http://docs.python-requests.org/en/master/>`_ is required.

Compatibility
-------------

Only Python >= 3.6 is supported.

Help!
-----

Is something not working properly? Are the docs awful? Want to help make this better?
If the answer is yes then great! All you have to do is open an issue. 

Licence
-------

This software is released under the MIT License

Authors
-------

`judge0api` was written by `Aaron Walker <aaw13@aber.ac.uk>`_.
