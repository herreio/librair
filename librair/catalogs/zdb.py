#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tqdm import tqdm

from ..protocols import sru
from ..schemas import xml

BASE = "http://services.dnb.de/sru/zdb"
VERSION = "1.1"
SCHEMA = "mods-xml"


def retrieve(query):
    """
    retrieve items matching given query
    """
    url = sru.address(BASE, query,
                      version=VERSION,
                      schema=SCHEMA,
                      records=100)
    return sru.retrieve(url)


def _explain():
    """
    get sru explanation
    """
    return sru.explain(BASE, VERSION)


def explain():
    """
    print pretty sru explanation
    """
    result = _explain()
    xml.pretty(result)


def explain_store():
    """
    store sru explanation
    """
    result = _explain()
    file = xml.filepath("sru", "zdb", "", "")
    xml.writer(result, file, path="res/meta")


def scroll(query, size=100, meta="mods-xml"):
    """
    scroll responses for given query and return result list
    """
    result = []
    url = sru.address(BASE, query, schema=meta, version="1.1", records=1)
    tree = sru.retrieve(url)
    total = int(
      tree.find(".//{http://www.loc.gov/zing/srw/}numberOfRecords").text
    )
    for i in tqdm(range(1, total+1, size)):
        url = sru.address(BASE, query=query, schema=meta,
                          version="1.1", records=size) + \
            "&startRecord=" + str(i)
        tree = sru.retrieve(url)
        data = tree.findall(".//{http://www.loc.gov/zing/srw/}recordData")
        data = [d.getchildren()[0] for d in data]
        result = result + data
    return result
