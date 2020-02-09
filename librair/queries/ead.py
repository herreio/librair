#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.parse import quote


def idx(char):
    """
    get query for given id
    """
    return "ead.id" + quote("=") + char


def archdesc(char):
    """
    get query for given id of archival description
    """
    return "ead.archdesc.id" + quote("=") + char
