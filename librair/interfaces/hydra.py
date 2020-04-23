#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..protocols import http


class Client:
    """
    Hydra client for database given by URL
    """

    def __init__(self, URL):
        self.URL = URL

    def _base(self, query, size, page):
        return "{0}/?q={1}&size={2}&page={3}".format(self.URL,
                                                     query, size, page)

    def retrieve(self, query, size=10, page=1):
        """
        retrieve data for given query in size from page
        """
        url = self._base(query, size, page)
        response = http.get_request(url)
        return http.response_json(response)

    def request(self, idn):
        """
        request data specified by idn
        """
        url = "{0}/{1}/{2}".format(self.URL, "resource", idn)
        response = http.get_request(url)
        return http.response_json(response)
