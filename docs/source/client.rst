Client
======

.. toctree::
   :maxdepth: 2
   :caption: Contents:

judge0api uses the concept of a "client" in order to interface with a Judge0 API. The client holds information about
the following:

- The "Endpoint" server - this is normally a domain, with a scheme. The public endpoint is https://api.judge0.com/, although different schemes, and even ports can be used.
- Any authentication information that is needed
- Any authorization information that is needed

.. autoclass:: judge0api.Client