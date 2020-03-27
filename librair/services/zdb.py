#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..protocols import http

from urllib.request import urlretrieve

BASE = "https://ld.zdb-services.de"
SCHEMA = ["html", "rdf", "ttl", "jsonld"]
EXAMPLE = "331668-3"


def address(idn, schema):
    """
    get url of item specified by idn in given schema
    """
    if schema not in SCHEMA:
        print("schema not supported!\n")
        print("choose out of:\n")
        for s in SCHEMA:
            print("\t\t", s)
        print("")
        return None
    return "{0}/{1}/{2}.{3}".format(BASE, "data", idn, schema)


def retrieve(idn, schema="jsonld"):
    """
    retrieve data specified by idn in given schema

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


def store(idn, schema="jsonld", path="."):
    """
    request data specified by idn in given schema
    and save it to file at path
    """
    url = address(idn, schema)
    if url is not None:
        fp = idn + "." + schema
        print("file:\t", fp)
        print("path:\t", path)
        fp = path + "/" + fp
        urlretrieve(url, fp)
