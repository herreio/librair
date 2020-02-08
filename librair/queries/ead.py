#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def idx(char):
    """
    get query for given id
    """
    return "ead.id=" + char


def archdesc(char):
    """
    get query for given id of archival description
    """
    return "ead.archdesc.id=" + char
