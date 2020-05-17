#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..protocols import http

from urllib.request import urlretrieve

BASE = "https://data.cerl.org/thesaurus"
SCHEMA = ["rdfxml", "txt", "json"]
STYLE = ["ttl", "jsonld", "internal"]

CORPORATE = "cnc00019524"
IMPRINT = "cni00031211"
LOCATION = "cnl00029460"
PERSON = "cnp00390358"


def address(idn, schema, style):
    """
    get url of entity specified by idn in given schema and style
    """
    if schema not in SCHEMA:
        print("schema not supported!")
        print("choose out of:")
        for s in SCHEMA:
            print("\t\t", s)
        return None
    # case: json (jsonld), txt (ttl), txt (internal)
    if style:
        if style not in STYLE:
            print("style not supported!")
            print("choose out of:")
            for s in STYLE:
                print("\t\t", s)
            return None
        if schema == "internal":
            return "{0}/{1}?format={2}&style={3}&pretty".format(BASE, idn,
                                                                schema, style)
        # case: jsonld or ttl
        return "{0}/{1}?format={2}&style={3}".format(BASE, idn, schema, style)
    # case: json, rdfxml, txt [= yml]
    else:
        if schema == "json":
            return "{0}/{1}?format={2}&pretty".format(BASE, idn, schema)
        # case: rdfxml or yml (txt)
        return "{0}/{1}?format={2}".format(BASE, idn, schema)


def request(idn, schema="rdfxml", style=None):
    """
    request data of entity specified by idn in given schema and (optional) style

    +--------+---------+--------------------+
    | SCHEMA | STYLE   | RETURN TYPE        |
    +========+=========+====================+
    | rdfxml | None    | lxml.etree.Element |
    +--------+---------+--------------------+
    | json   | None    |  dict              |
    +--------+---------+--------------------+
    | json   | jsonld  |  dict              |
    +--------+---------+--------------------+
    | txt    | ttl     |  str               |
    +--------+---------+--------------------+
    | txt    | internal|  str               |
    +--------+---------+--------------------+
    """
    url = address(idn, schema, style=style)
    if url is not None:
        res = http.get_request(url)
        if schema == "rdfxml":
            return http.response_xml(res)
        elif schema == "json":
            return http.response_json(res)
        else:
            return http.response_text(res)


def store(idn, schema="json", style=None, path="."):
    """
    | request data of entity specified by idn in given schema and (optional) style
    | afterwards save it to directory at path
    """
    url = address(idn, schema, style)
    if url is not None:
        fp = idn + "." + schema
        print("file:\t", fp)
        print("path:\t", path)
        fp = path + "/" + fp
        urlretrieve(url, fp)
