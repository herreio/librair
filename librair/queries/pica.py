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

    used by:
        - vd18
    """
    return "pica.plc" + quote("=") + name


def publisher(name):
    """
    get query for publisher / publication place given by name

    used by:
        - vd18
    """
    return "pica.pub" + quote("=") + name


def veroeffentlichungsort(name):
    """
    get query for publication place given by name

    used by:
        - vd17
    """
    return "pica.vlo" + quote("=") + name


def ort(name):
    """
    get query for place given by name

    used by:
        - hebis
    """
    return "pica.ort" + quote("=") + name


def issn_im_aufsatz(issn):
    """
    get query for articles in journal with given issn

    used by:
        - gjz18
    """
    return "pica.zis" + quote("=") + str(issn)


def zdbnum_im_aufsatz(zdbnum):
    """
    get query for articles in journal with given zdb number (identifier)

    used by:
        - gjz18
    """
    return "pica.zzd" + quote("=") + str(zdbnum)
