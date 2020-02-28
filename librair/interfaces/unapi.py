#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..protocols import http


class Client:
    """
    unAPI client
    """

    def __init__(self, URL):
        self.URL = URL
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
