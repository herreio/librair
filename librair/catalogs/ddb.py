#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""

from .. import queries
from ..protocols import http

BASE = 'https://api.deutsche-digitale-bibliothek.de/'

# endpoints
ITEMS = BASE + "items"      # json / xml
SEARCH = BASE + "search"    # json only !
SEARCH_ORG = SEARCH + "/organization"

# methods of items
VIEW = "view"
EDM = "edm"
PARENTS = "parents"
PROFILE = "indexing-profile"


def _header_json(key):
    """
    header for:
        items (default)
        facets (only!)
        search (only!)
    """
    return {'accept': 'application/json',
            'Authorization': 'OAuth oauth_consumer_key="' + key + '"'}


def _header_xml(key):
    """
    header for:
        items
    """
    return {'accept': 'application/xml',
            'Authorization': 'OAuth oauth_consumer_key="' + key + '"'}


def _header_aster(key):
    """
    header for:
        items (returns json)
        facets (returns json)
    """
    return {'accept': '*/*',
            'Authorization': 'OAuth oauth_consumer_key="' + key + '"'}


def query_url(query):
    """
    """
    return "?".join([SEARCH, query])


def view_url(idx):
    """
    """
    return "/".join([ITEMS, idx, VIEW])


def facets_url(type="SEARCH"):
    """
    """
    return SEARCH + "/facets?type=" + type


def view(idx, key):
    """
    """
    url = view_url(idx)
    res = http.get_request(url, _header_json(key))
    return http.response_json(res)


def search(query, key, size=10):
    """
    """
    query = queries.ddb.build(query=query, rows=size)
    url = query_url(query)
    res = http.get_request(url, _header_json(key))
    return http.response_json(res)


def scroll(query):
    """
    """
    pass


def search_facets(key):
    """
    !! returns [] !!
    """
    url = facets_url(type="SEARCH")
    res = http.get_request(url, _header_json(key))
    return http.response_json(res)
