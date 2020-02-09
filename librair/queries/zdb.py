#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.parse import quote
from . import dnb


def verlagsort(name):
    """
    part of query for publisher given by name
    """
    return "vort" + quote("=") + name


def andquery():
    """
    combine search parameters
    """
    return dnb.andquery()
