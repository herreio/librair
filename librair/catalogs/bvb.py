#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..schemas import xml
from ..protocols import sru


BASE = "http://bvbr.bib-bvb.de:5661/bvb01sru"
VERSION = "1.1"


def explain(store=False, path=""):
    """
    get sru explanation
    """
    result = sru.explain(BASE, VERSION)
    if not store:
        xml.pretty(result)
    else:
        file = xml.filepath("sru", "bvb", "", "")
        xml.writer(result, file, path=path)
