#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..protocols import sru
from ..schemas import xml

BASE = "http://cbsopac.rz.uni-frankfurt.de/sru/DB=2.1/"
VERSION = "1.1"
SCHEMA = "pica"  # "marc21"


def explain(store=False, path=""):
    result = sru.explain(BASE, VERSION)
    if not store:
        xml.pretty(result)
    else:
        file = xml.filepath("sru", "hebis", "", "")
        xml.writer(result, file, path=path)
