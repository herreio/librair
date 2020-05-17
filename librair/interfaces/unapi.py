#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..protocols import http


class Client:
    """
    unAPI client for database given by url and id
    and items specified by given variable
    """

    def __init__(self, URL, DB, VAR):
        self.URL = URL
        self.DB = DB
        self.VAR = VAR
        self.formats = self._formats()

    def _formats(self):
        response = http.get_request(self.URL)
        response = http.response_xml(response)
        schemas = [c for c in response.getchildren()]
        formats = {}
        for s in schemas:
            n = s.attrib['name']
            formats[n] = {}
            if 'type' in s.attrib:
                formats[n]['type'] = s.attrib['type']
            else:
                formats[n]['type'] = None
            if 'docs' in s.attrib:
                formats[n]['docs'] = s.attrib['docs']
            else:
                formats[n]['docs'] = None
        return formats

    def address(self, idn, schema):
        """
        get url of entity specified by idn in given schema
        """
        return self.URL + "/?id=" + self.DB + ":" + \
            self.VAR + ":" + idn + "&format=" + schema

    def request(self, idn, schema):
        """
        request data of entity specified by idn in given schema
        """
        if schema in self.formats:
            schematype = self.formats[schema]['type']
            url = self.address(idn, schema)
            response = http.get_request(url)
            if response is not None:
                if "xml" in schematype:
                    return http.response_xml(response)
                elif "json" in schematype:
                    return http.response_json(response)
                elif "plain" in schematype:
                    return http.response_text(response)
            else:
                return response
        else:
            print("schema not supported!")
            return None
