#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..schemas import xml
from ..protocols import sru

from tqdm import tqdm


GJZ18 = "http://sru.gbv.de/gjz18"
VD17 = "http://sru.gbv.de/vd17"
VD18 = "http://sru.gbv.de/vd18"
IDZ = "http://sru.gbv.de/idz"

VERSION = "2.0"
SCHEMA = "mods"


def explainVD18(store=False):
    """
    sru explanation of VD18
    """
    result = sru.explain(VD18, VERSION)
    if not store:
        xml.pretty(result)
    else:
        file = xml.filepath("sru", "vd18", "", "")
        xml.writer(result, file, path="res/meta")


def explainVD17(store=False):
    """
    sru explanation of VD17
    """
    result = sru.explain(VD17, VERSION)
    if not store:
        xml.pretty(result)
    else:
        file = xml.filepath("sru", "vd17", "", "")
        xml.writer(result, file, path="res/meta")


def explainIDZ(store=False):
    """
    sru explanation of IDZ
    """
    result = sru.explain(IDZ, VERSION)
    if not store:
        xml.pretty(result)
    else:
        file = xml.filepath("sru", "idz", "", "")
        xml.writer(result, file, path="res/meta")


def explainGJZ18(store=False):
    """
    sru explanation of GJZ18
    """
    result = sru.explain(GJZ18, VERSION)
    if not store:
        xml.pretty(result)
    else:
        file = xml.filepath("sru", "gjz18", "", "")
        xml.writer(result, file, path="res/meta")


def items(url):
    """
    determine number of results for query given in url
    """
    tree = sru.retrieve(url)
    ns = tree.nsmap
    return int(tree.find(".//zs:numberOfRecords", namespaces=ns).text)


def scroll(base, query, size=500, meta="mods"):
    """
    scroll responses for given query and return result list
    """
    result = []
    url = sru.address(base, query=query, schema=meta, records=1)
    tree = sru.retrieve(url)
    ns = tree.nsmap
    total = int(tree.find(".//zs:numberOfRecords", namespaces=ns).text)
    for i in tqdm(range(1, total+1, size)):
        url = sru.address(base, query=query, schema=meta, records=size) + \
            "&startRecord=" + str(i)
        tree = sru.retrieve(url)
        data = tree.findall(".//zs:recordData", namespaces=ns)
        data = [d.getchildren()[0] for d in data]
        result = result + data
    return result
