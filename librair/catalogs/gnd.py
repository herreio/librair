#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..protocols import sru
from ..schemas import xml

BASE = "https://services.dnb.de/sru/authorities"
VERSION = "1.1"
SCHEMA = "RDFxml"  # dc, RDFxml, PicaPlus-xml, baseDc-xml, mods-xml


def explain(store=False, path=""):
    result = sru.explain(BASE, VERSION)
    if not store:
        xml.pretty(result)
    else:
        file = xml.filepath("sru", "dnb-authorities", "", "")
        xml.writer(result, file, path=path)


def retrieve(query):
    """
    retrieve items matching given query
    """
    url = sru.address(BASE, query,
                      version=VERSION,
                      schema=SCHEMA,
                      records=100)
    return sru.retrieve(url)
