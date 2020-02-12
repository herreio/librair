#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..utilities import url
from ..protocols import http, sru
from ..schemas import xml

BASE = "https://data.cerl.org"
THESAURUS = url.join_paths([BASE, "thesaurus"])

SRU = url.join_paths([THESAURUS, "_sru"])
VERSION = "1.2"
SCHEMA = "marcxml"  # ctas, ctas10


def explain(store=False, path=""):
    """
    get sru explanation
    """
    result = sru.explain(SRU, VERSION)
    if not store:
        xml.pretty(result)
    else:
        file = xml.filepath("sru", "cerl", "", "")
        xml.writer(result, file, path=path)


def _entity(idx, format, style):
    """
    request entitiy by given idx in specified format and style
    """
    _url = "/".join([THESAURUS, idx])
    _params = url.param("format", format)
    if style:
        _style = url.param("style", style)
        _params = url.join_params([_params, _style])
        if style == "internal":
            _params = url.join_params([_params, "pretty"])
    else:
        if format == "json":
            _params = url.join_params([_params, "pretty"])
    _url = url.add_params(_url, _params)
    _res = http.get_request(_url)
    if format == "rdfxml":  # RDF-XML
        return http.response_xml(_res)
    elif format == "json":  # JSON / JSON-LD
        return http.response_json(_res)
    else:                   # RDF-TTL / YAML / CT
        return http.response_text(_res)


def cnc(idx="cnc00019524", format="rdfxml", style=None):
    """
    request coporate bodies data given by idx in specified format and style
    """
    return _entity(idx, format, style)


def cni(idx="cni00031211", format="rdfxml", style=None):
    """
    request imprint data given by idx in specified format and style
    """
    return _entity(idx, format, style)


def cnl(idx="cnl00029460", format="rdfxml", style=None):
    """
    request location data by given idx in specified format and style
    """
    return _entity(idx, format, style)


def cnp(idx="cnp00390358", format="rdfxml", style=None):
    """
    request person data by given idx in specified format and style
    """
    return _entity(idx, format, style)
