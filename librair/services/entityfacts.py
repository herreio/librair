#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..protocols import http

from urllib.request import urlretrieve

BASE = "https://hub.culturegraph.org/entityfacts"

PND = "116473207"
GKD = "104526539X"


def address(idn):
    """
    get url of entity given by idn
    """
    return "{0}/{1}".format(BASE, idn)


def request(idn):
    """
    request data of entity given by idn
    """
    url = address(idn)
    res = http.get_request(url)
    return http.response_json(res)


def store(idn, path="."):
    """
    request data specified by idn and schema
    afterwards save it to file at path
    """
    url = address(idn)
    fp = idn + ".json"
    fp = path + "/" + fp
    urlretrieve(url, fp)
