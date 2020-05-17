#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..protocols import http

from urllib.request import urlretrieve

BASE = "http://beacon.findbuch.de/seealso/pnd-aks"
SCHEMA = ["seealso", "sources", "redirect", "opensearchdescription"]
EXAMPLE = "116473207"


def address(idn, schema):
    """
    get url of entity specified by idn in given schema
    """
    if schema not in SCHEMA:
        print("schema not supported!\n")
        print("choose out of:\n")
        for s in SCHEMA:
            print("\t", s)
        print("")
        return None
    return "{0}?id={1}&format={2}".format(BASE, idn, schema)


def request(idn, schema="seealso"):
    """
    request data of entity specified by idn in given schema

    +------------------------+--------------------+
    | SCHEMA                 | RETURN TYPE        |
    +========================+====================+
    | seealso                | json               |
    +------------------------+--------------------+
    | sources                | str (html)         |
    +------------------------+--------------------+
    | redirect               | str (html)         |
    +------------------------+--------------------+
    | opensearchdescription  | lxml.etree.Element |
    +------------------------+--------------------+
    """
    url = address(idn, schema)
    if url is not None:
        res = http.get_request(url)
        if schema == "seealso":
            return http.response_json(res)
        elif schema == "opensearchdescription":
            return http.response_xml(res)
        else:
            return http.response_text(res)
    else:
        return url


def store(idn, schema="rdf", path="."):
    """
    | request data of entity specified by idn in given schema
    | afterwards save it to directory at path
    """
    url = address(idn, schema)
    if url is not None:
        fp = idn + "." + schema
        fp = path + "/" + fp
        urlretrieve(url, fp)
