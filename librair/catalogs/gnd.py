#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..protocols import sru
from ..schemas import xml

BASE = "https://services.dnb.de/sru/authorities"
VERSION = "1.1"
SCHEMA = "mods-xml"  # dc, RDFxml, PicaPlus-xml, baseDc-xml


def explain(store=False, path=""):
    result = sru.explain(BASE, VERSION)
    if not store:
        xml.pretty(result)
    else:
        file = xml.filepath("sru", "dnb-authorities", "", "")
        xml.writer(result, file, path=path)
