#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.parse import quote


def period(first, last):
    """
    query for period given by first and last year
    """
    return "dnb.eje" + quote(">=") + str(first) + andquery() \
           + "dnb.eje" + quote("<=") + str(last)


def letzterscheinung(year):
    """
    query for last year of publication
    """
    return "dnb.eje" + quote("=") + str(year)


def ersterscheinung(year):
    """
    query for first year of publication
    """
    return "dnb.ejl" + quote("=") + str(year)


def andquery():
    """
    combine search parameters
    """
    return "+and+"
