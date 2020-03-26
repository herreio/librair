#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..protocols import http

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

        ID      FORMAT
        marc21  xml
        viaf    xml
        rdf     xml
        links   json
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
