#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.parse import quote


def title(char):
    """
    """
    return "query=pica.tit" + quote("=") + char


def place(name):
    """
    get query for place given by name
    """
    return "query=pica.plc" + quote("=") + name


def publisher(name):
    """
    get query for publisher given by name
    """
    return "pica.pub" + quote("=") + name
