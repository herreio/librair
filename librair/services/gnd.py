#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..protocols import http

from urllib.request import urlretrieve

BASE = "http://d-nb.info/gnd"
SCHEMA = ["lds", "marcxml"]

PND = "116473207"
GKD = "104526539X"
SWD = "4133333-0"


def address(idn, schema):
    """
    get url of entity specified by idn in given schema
    """
    if schema not in SCHEMA:
        print("schema not supported!")
        print("choose out of:")
        for s in SCHEMA:
            print("\t", s)
        return None
    return "{0}/{1}/about/{2}".format(BASE, idn, schema)


def request(idn, schema="lds"):
    """
    request data of entity specified by idn in given schema

    +----------+--------------------+
    | SCHEMA   | RETURN TYPE        |
    +==========+====================+
    | lds      |  str               |
    +----------+--------------------+
    | marcxml  | lxml.etree.Element |
    +----------+--------------------+

    to do:

        - handle lds (RDF Turtle)
    """
    url = address(idn, schema)
    if url is not None:
        response = http.get_request(url)
        if "xml" in schema:
            return http.response_xml(response)
        else:
            return http.response_text(response)
    else:
        return url


def store(idn, schema="lds", path="."):
    """
    | request data of entity specified by idn in given schema
    | afterwards save it to directory at path
    """
    url = address(idn, schema)
    if url is not None:
        fp = idn + "." + schema
        fp = path + "/" + fp
        urlretrieve(url, fp)
