#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.parse import quote


def query(char):
    """
    """
    return "q=" + char


def format(type):
    """
    query for response format
    """
    return "format=" + type


def pubStartDate(first, last):
    """
    query for first date of publication range given by first and last
    """
    return "publication.startDate" + quote(":") + "[" + str(first) +\
        toQuery() + str(last) + "]"


def pubEndDate(first, last):
    """
    query for last date of publication range given by first and last
    """
    return "publication.endDate" + quote(":") + "[" + str(first) +\
        toQuery() + str(last) + "]"


def pubLocation(name):
    """
    query for publication place given by name
    """
    return "publication.location" + quote(":") + name


def toQuery():
    """
    combine date parameters
    """
    return "+TO+"


def andQuery():
    """
    combine search parameters
    """
    return "+AND+"
