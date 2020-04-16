#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from . import http


def _param(param, value):
    """
    create 'parameter=value'
    """
    return "{0}={1}".format(param, value)


def _andparam(params):
    """
    string join parameter list with &
    """
    return "&".join(params)


def _query(char):
    """
    get query created from given chars
    """
    return _param("query", char)


def _version(num):
    """
    get version parameter with given number
    """
    return _param("version", str(num))


def _operation(name):
    """
    operation parameter with given name
    """
    return _param("operation", name)


def _schema(name):
    """
    schema of records with given name
    """
    return _param("recordSchema", name)


def _maxnum(num):
    """
    maximum of records to return
    """
    return _param("maximumRecords", str(num))


def _build(version, operation, query, schema, records):
    """
    get part of request url for given parameters
    """
    return _andparam([_version(version),
                      _operation(operation),
                      _query(query),
                      _schema(schema),
                      _maxnum(records)])


def address(base, query, schema="mods", records=10,
            version="1.2", operation="searchRetrieve"):
    """
    get http address for given parameters
    """
    params = _build(version, operation, query, schema, records)
    return "{0}?{1}".format(base, params)


def explain(base, version):
    """
    return explanation page for given base and version
    """
    ver = _version(version)
    op = _operation("explain")
    url = "{0}?{1}".format(base, _andparam([ver, op]))
    return retrieve(url)


def retrieve(url):
    """
    send request to given url and return xml response
    """
    response = http.get_request(url)
    return http.response_xml(response)
