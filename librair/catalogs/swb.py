#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..protocols import sru
from ..schemas import xml

BASE = "https://sru.bsz-bw.de/swb"
VERSION = "2.0"     # "1.1" / "1.2"
SCHEMA = "picaxml"  # extppxml (Pica+)


def explain(store=False, path=""):
    result = sru.explain(BASE, VERSION)
    if not store:
        xml.pretty(result)
    else:
        file = xml.filepath("sru", "swb", "", "")
        xml.writer(result, file, path=path)
