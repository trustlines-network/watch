|Build Status| |Code style: black|

trustlines-watch
================

trustlines-watch helps monitoring the trustlines cluster. It watches a
running parity or geth client via the JSONRPC interface and pushes
information to a riemann instance.

Installation
------------

trustlines watch requires python 3.5 or up. Please run the following
command in a python 3 virtualenv:

::

    pip install . -c constraints.txt

This will install a 'tl-watch' executable.

Usage
-----

tl-watch etherscan
~~~~~~~~~~~~~~~~~~

Watches etherscan for the current blockNumber. Run
``tl-watch etherscan --help`` for available command line options.

tl-watch jsonrpc
~~~~~~~~~~~~~~~~

Watches a parity or geth client via the JSONRPC interface. Run
``tl-watch jsonrpc --help`` for available command line options.

CHANGES
=======

0.2.1
-----

-  The tlwatch executable has been renamed to tl-watch, though it's also
   still available as tlwatch. It will be removed in a future release.

.. |Build Status| image:: https://travis-ci.org/trustlines-network/watch.svg?branch=develop
   :target: https://travis-ci.org/trustlines-network/watch
.. |Code style: black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black
