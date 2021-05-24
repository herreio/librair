.. role:: shell(code)
   :language: shell

Librair Vniuersal
=================

Introduction
------------

This is a package for harvesting data from different library catalogs.

Installation
------------

You can simply install this package via `PyPI <https://pypi.org/project/librair/>`_:

.. code-block:: shell

    pip install librair

... or via this repository:

.. code-block:: shell

    pip install -e git+https://github.com/herreio/librair.git#egg=librair

... or by cloning the repository:

.. code-block:: shell

    git clone https://github.com/herreio/librair.git
    cd librair
    # create and activate virutalenv
    utils/setup
    source env/bin/activate


Documentation
-------------

A minimal documentation can be found on `Read the Docs <https://librair.readthedocs.io/>`_.

To build the documentation from the files found at docs:

.. code-block:: shell

    cd docs
    make html
