#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..protocols import http

BASE = "http://d-nb.info"
SCHEMA = ["lds", "marcxml", "bibframe"]
EXAMPLE = "575235691"


def address(idn, schema):
    """
    get url of item given by idn in given schema
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
    request data of entity given by idn in given schema

    supported schemas:

        ID        TYPE
        bibframe  str
        marcxml   lxml.etree.Element
        lds       str

    to do:

        - handle lds (RDF Turtle)
        - handle bibframe
    """
    url = address(idn, schema)
    if url is not None:
        response = http.get_request(url)
        if "xml" in schema or "frame" in schema:
            return http.response_xml(response)
        else:
            return http.response_text(response)
    else:
        return url
