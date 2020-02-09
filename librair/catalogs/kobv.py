#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..protocols import sru
from ..schemas import xml

BASE = "http://z3950.kobv.de/k2"
VERSION = "1.1"
SCHEMA = "dc"   # "marcxml"


def explain(store=False, path=""):
    result = sru.explain(BASE, VERSION)
    if not store:
        xml.pretty(result)
    else:
        file = xml.filepath("sru", "kobv", "", "")
        xml.writer(result, file, path=path)
