#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.parse import quote


def record(idx):
    """
    get record by given id
    """
    return "rec.id" + quote("=") + idx


def cqlall(char):
    """
    get query for all fields
    """
    return "cql.all" + quote("=") + char


def cqlserver(name):
    """
    get query for server given by name
    """
    return "cql.serverChoice" + quote("=") + name
