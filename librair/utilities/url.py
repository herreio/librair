#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.parse import quote


def param(name, value, encode=False):
    """
    """
    return "{0}={1}".format(name, value) if not encode \
        else quote("{0}={1}".format(name, value))


def add_params(url, query):
    """
    """
    return "{0}?{1}".format(url, query)


def join_params(params):
    """
    """
    return "&".join(params)


def join_paths(paths):
    """
    """
    return "/".join(paths)
