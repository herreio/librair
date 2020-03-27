#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..protocols import http

from urllib.request import URLopener

DB = ["data", "resource"]
BASE = "https://ld.zdb-services.de"
SCHEMA = ["html", "rdf", "ttl", "jsonld"]
EXAMPLE = "331668-3"


def address(idn, schema):
    """
    get url of item with given idn in given schema
    """
    if schema not in SCHEMA:
        print("schema not supported!\n")
        print("choose out of:\n")
        for s in SCHEMA:
            print("\t", s)
        print("")
        return None
    return "{0}/{1}/{2}.{3}".format(BASE, "data", idn, schema)


def request(idn, schema="jsonld"):
    """
    request data given by idn in given schema from given base

    supported schemas:

        ID          TYPE
        html        str
        rdf         etree.Element
        ttl         str
        jsonld      dict
    """
    url = address(idn, schema)
    if url is not None:
        res = http.get_request(url)
        if schema == "jsonld":
            return http.response_json(res)
        elif schema == "rdf":
            return http.response_xml(res)
        else:
            return http.response_text(res)
    else:
        return url


def store(idn, schema="jsonld", path="."):
    """
    request data specified by idn and schema
    afterwards save it to file at path
    """
    data = URLopener()
    url = address(idn, schema)
    if url is not None:
        fp = idn + "." + schema
        fp = path + "/" + fp
        data.retrieve(url, fp)
