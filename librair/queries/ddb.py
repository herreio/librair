#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""

from urllib.parse import quote

# see: /doku/display/ADD/Hierarchietyp
HIERARCHY = [
  "htype_001",   # Abschnitt / Section
  "htype_003",   # Beigefügtes oder enthaltenes Werk / Contained works
  "htype_006",   # Aufsatz / Article
  "htype_007",   # Band / Volume
  "htype_014",   # Heft / Issue
  "htype_017",   # Inhaltsverzeichnis / Table of contents
  "htype_020",   # Mehrbändiges Werk / Multivolume work
  "htype_023",   # Fortlaufendes Sammelwerk / Serial
  "htype_026",   # Rezension / Review
  "htype_026",   # Text / Text
  "htype_032",   # Serie / Series
  "htype_033",   # Unterserie / Subseries
  "htype_035"    # Teil / Part
]

# see: /doku/display/ADD/Medientyp
MEDIA = [
  "mediatype_003",  # Text
  "mediatype_004",  # Volltext
  "mediatype_006",  # Sonstiges
  "mediatype_007"   # ohne Medientyp
]

# see: /doku/display/ADD/Sparte
SEC = [
  "sec_01",  # Archive
  "sec_02",  # Bibliothek
  "sec_04"   # Forschungseinrichtung
]

# see: /doku/display/ADD/Zeitvokabular
CENTURY_17TH = "time_61700"
CENTURY_18TH = "time_61800"
CENTURY_19TH = "time_61900"
PERIOD = [
  "time_61705",    # 1601 bis 1650
  "time_61745",    # 1651 to 1700
  "time_61807",    # 1701 to 1725
  "time_61825",    # 1726 to 1750
  "time_61847",    # 1751 bis 1775
  "time_61875",    # 1776 bis 1800
  "time_61907",    # 1801 bis 1825
  "time_61925"     # 1826 bis 1850
]


def build(facet="",
          facet_name=[],
          facet_limit="",
          mindocs=0,
          offset=0,
          query="",
          rows=10,
          sort=None,
          apikey=None):
    """
    """
    full = []
    full.append(_query(query))
    if facet:
        full.append(_facet(facet))
    if facet_name:
        full.append("&".join([_facet_name(i[0], i[1]) for i in facet_name]))
    if mindocs:
        full.append(_mindocs(mindocs))
    if offset:
        full.append(_offset(offset))
    if rows:
        full.append(_rows(rows))
    if sort:
        full.append(_sort(sort))
    if apikey:
        full.append(_oauth_key(apikey))
    return "&".join(full)


def _facet(name):
    """
    """
    return "facet" + "=" + name


def _facet_name(name, value):
    """
    possible values:

        time_fct
        place_fct
        affiliate_fct
        keywords_fct
        language_fct
        type_fct
        sector_fct
        provider_fct
    """
    return name + "=" + value


def _mindocs(num):
    """
    """
    return "mindocs=" + str(num)


def _oauth_key(value):
    """
    """
    return "oauth_consumer_key=" + value


def place_fct(name):
    """
    """
    return "place_fct=" + name


def _offset(num):
    """
    """
    return "offset=" + str(num)


def _query(value):
    """
    """
    return "query=" + value


def _rows(num):
    """
    """
    return "rows=" + str(num)


def _sort(type):
    """
    possible values:

        ALPHA_ASC
        ALPHA_DESC
        RANDOM_<seed>
        RELEVANCE
    """
    return "sort=" + type


def place(name):
    """
    """
    return "place" + quote(":") + name
