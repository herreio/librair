.. role:: shell(code)
   :language: shell

Librair Vniuersal
=================

Synopsis
--------

``librair`` is a Python package for harvesting data from different library catalogs. It has been developed as part of the `Dikon project <https://dikon.izea.uni-halle.de/>`_ (2019–2020) at the `Interdisciplinary Centre for European Enlightenment Studies <https://www.izea.uni-halle.de/>`_.

Installation
------------

You can install this package via `PyPI <https://pypi.org/project/librair/>`_:

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

The documentation can be found on `Read the Docs <https://librair.readthedocs.io/>`_.

To build the documentation from the files found at docs:

.. code-block:: shell

    cd docs
    make html
