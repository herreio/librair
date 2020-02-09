#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..protocols import http
from ..queries import lobid


BASE = "https://lobid.org/resources"
SEARCH = BASE + "/search"


def query_url(query):
    """
    """
    return "?".join([SEARCH, query])


def search(query):
    """
    """
    query = lobid.query(query)
    url = query_url(query)
    url += "&" + lobid.format("json")
    response = http.get_request(url)
    return http.response_json(response)
