#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..protocols import http

from urllib.request import urlretrieve

BASE = "https://kalliope-verbund.info/xmleac"
EXAMPLE = "2170917-8"


def address(idn):
    """
    get url of entity given by idn
    """
    return "{0}?eac.id={1}".format(BASE, idn)


def request(idn):
    """
    request data of entity given by idn
    """
    url = address(idn)
    res = http.get_request(url)
    return http.response_xml(res)


def store(idn, path="."):
    """
    request data specified by idn and schema
    afterwards save it to file at path
    """
    url = address(idn)
    fp = idn + ".xml"
    fp = path + "/" + fp
    urlretrieve(url, fp)
