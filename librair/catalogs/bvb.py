#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..schemas import xml
from ..protocols import sru


BASE = "http://bvbr.bib-bvb.de:5661/bvb01sru"
VERSION = "1.1"


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
    file = xml.filepath("sru", "bvb", "", "")
    xml.writer(result, file, path="res/meta")
