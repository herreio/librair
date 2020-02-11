#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.parse import quote


def param(name, value, encode=False):
    """
    """
    if not encode:
        return name + "=" + value
    else:
        return name + quote("=") + value


def join_params(params):
    """
    """
    return "&".join(params)


def add_params(url, query):
    """
    """
    return "?".join([url, query])


def join_dirs(dirs):
    """
    """
    return "/".join(dirs)
