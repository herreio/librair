#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.parse import quote


def title(char):
    """
    get query for given title
    """
    return "pica.tit" + quote("=") + char


def place(name):
    """
    get query for place given by name
    """
    return "pica.plc" + quote("=") + name


def publisher(name):
    """
    get query for publisher given by name
    """
    return "pica.pub" + quote("=") + name


def ort(name):
    """
    get query for place given by name

    used by:
        - hebis
    """
    return "pica.ort" + quote("") + name
