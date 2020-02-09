#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..protocols import sru
from ..schemas import xml

BASE = "http://sru.k10plus.de/"
K10PLUS = BASE + "opac-de-627"  # k10plus verbundkatalog
VD17 = BASE + "vd17"
GVK = BASE + "gvk"

VERSION = "2.0"     # "1.1" / "1.2"
SCHEMA = "mods"  # "dc" / "marcxml" / "picaxml"


def explain(store=False, path=""):
    result = sru.explain(K10PLUS, VERSION)
    if not store:
        xml.pretty(result)
    else:
        file = xml.filepath("sru", "k10plus", "", "")
        xml.writer(result, file, path=path)
