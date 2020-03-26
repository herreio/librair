#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..protocols import http

BASE = "https://hub.culturegraph.org/entityfacts"


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
