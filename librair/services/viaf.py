#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..protocols import http

from urllib.request import urlretrieve

BASE = "https://viaf.org/viaf"
SCHEMA = ["marc21", "viaf", "rdf", "links"]
EXAMPLE = "32049320"


def address(idn, schema):
    """
    get url of entity given by idn in given schema
    """
    if schema not in SCHEMA:
        print("schema not supported!")
        print("choose out of:")
        for s in SCHEMA:
            print("\t", s)
        return None
    if not schema == "links":
        return "{0}/{1}/{2}.xml".format(BASE, idn, schema)
    return "{0}/{1}/justlinks.json".format(BASE, idn)


def request(idn, schema="rdf"):
    """
    request data of entity given by idn in given schema

    supported schemas:

        ID      TYPE
        marc21  lxml.etree.Element
        viaf    lxml.etree.Element
        rdf     lxml.etree.Element
        links   dict
    """
    url = address(idn, schema)
    if url is not None:
        response = http.get_request(url)
        if schema != "links":
            return http.response_xml(response)
        else:
            return http.response_json(response)
    else:
        return url


def store(idn, schema="rdf", path="."):
    """
    request data specified by idn and schema
    afterwards save it to file at path
    """
    url = address(idn, schema)
    if url is not None:
        fp = idn + "." + schema
        fp = path + "/" + fp
        urlretrieve(url, fp)
