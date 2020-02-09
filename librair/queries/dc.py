#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.parse import quote


def title(char):
    """
    get query for given title
    """
    return "dc.title" + quote("=") + char


def creator(name):
    """
    get query for creator given by name
    """
    return "dc.creator" + quote("=") + name


def publisher(name):
    """
    get query for publisher given by name
    """
    return "dc.publisher" + quote("=") + name


def date(date):
    """
    get query for given publication date
    """
    return "dc.date" + quote("=") + str(date)
