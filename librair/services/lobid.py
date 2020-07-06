#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..protocols import http

from urllib.request import urlretrieve

GND_BASE = "http://lobid.org/gnd"
GND_SCHEMA = ["json"]

PND = "116473207"
GKD = "104526539X"
SWD = "4133333-0"


def gnd_address(idn):
    """
    get url of entity specified by idn
    """
    return "{0}/{1}.json".format(GND_BASE, idn)


def gnd_request(idn):
    """
    request data of entity specified by idn
    """
    url = gnd_address(idn)
    res = http.get_request(url)
    return http.response_json(res)


def gnd_store(idn, path="."):
    """
    | request data of entity specified by idn
    | afterwards save it to directory at path
    """
    url = gnd_address(idn)
    fp = idn + ".json"
    fp = path + "/" + fp
    urlretrieve(url, fp)
