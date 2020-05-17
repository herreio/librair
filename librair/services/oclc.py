#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..protocols import http

from urllib.request import urlretrieve

BASE = "https://www.worldcat.org/oclc"
SCHEMA = ["ttl", "jsonld", "rdf", "nt"]
EXAMPLE = "78515859"

# http://www.worldcat.org/oclc/<OCLCID>.<FORMAT>
# http://worldcat.org/entity/<ENTITYTYPE>/id/<ENTITYID> (Linked Data Explorer)
#     Entities: work, person, ...


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
    return "{0}/{1}.{2}".format(BASE, idn, schema)


def request(idn, schema="jsonld"):
    """
    request data of entity specified by idn in given schema

    +----------+--------------------+
    | SCHEMA   | RETURN TYPE        |
    +==========+====================+
    | nt       |  str               |
    +----------+--------------------+
    | rdf      | lxml.etree.Element |
    +----------+--------------------+
    | ttl      |  str               |
    +----------+--------------------+
    | jsonld   |  dict              |
    +----------+--------------------+
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


def store(idn, schema="rdf", path="."):
    """
    | request data of entity specified by idn in given schema
    | afterwards save it to file at path
    """
    url = address(idn, schema)
    if url is not None:
        fp = idn + "." + schema
        fp = path + "/" + fp
        urlretrieve(url, fp)
