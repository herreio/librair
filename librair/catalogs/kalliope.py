#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

from ..protocols import sru
# from ..schemas import xml


BASE = "http://kalliope-verbund.info/sru"
VERSION = "1.2"
SCHEMA = "mods"


def explain():
    """
    no explain page given!?

    response message:

    Unsupported operation 'explain'. The only supported
    operation is 'searchRetrieve'.
    """
    return sru.explain(BASE, VERSION)


def items(url):
    """
    determine number of results for query given in url
    """
    tree = sru.retrieve(url)
    ns = tree.nsmap
    return int(tree.find(".//srw:numberOfRecords", namespaces=ns).text)


def total(query, meta="mods"):
    """
    retrieve all items matching given query
    """
    url = sru.address(BASE, query=query, schema=meta, records=1)
    total = items(url)
    print("start retrieving", total, "items...")
    start = time.time()
    url = sru.address(BASE, query=query, schema=meta, records=total)
    result = sru.retrieve(url)
    fin = time.time()
    print("finished retrieving all items!")
    elapsed = fin - start
    print("time elapsed:", round(elapsed, 2), "(sec)")
    return result
