#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ..protocols import http

from tqdm import tqdm


class Client:
    """
    Hydra client for database given by URL
    """

    def __init__(self, URL):
        self.URL = URL

    def address(self, query, size, page):
        """
        get url for given query, size and page
        """
        return "{0}.jsonld?q={1}&size={2}&page={3}".format(self.URL,
                                                     query, size, page)

    def retrieve(self, query, size=10, page=1):
        """
        retrieve data for given query in size from page
        """
        url = self.address(query, size, page)
        response = http.get_request(url)
        return Response(http.response_json(response)).members()

    def total(self, query):
        """
        determine total number of results for given query
        """
        url = self.address(query, 1, 1)
        response = http.get_request(url)
        return Response(http.response_json(response)).total()

    def scroll(self, query, size=100, page=1):
        """
        | scroll items matching given query, in steps specified by size,
        | starting from given page
        """
        members = []
        total = self.total(query)
        if total == 0:
            return members
        pbar = tqdm(total=total)
        url = self.address(query, size, page)
        while url != "":
            result = http.get_request(url)
            result = Response(http.response_json(result))
            addnew = result.members()
            if addnew != []:
                members += addnew
                pbar.update(len(addnew))
            else:
                url = ""
            url = result.view_next()
        pbar.close()
        return members

    def request(self, idn):
        """
        request data specified by idn
        """
        url = "{0}/{1}.jsonld".format(self.URL, idn)
        response = http.get_request(url)
        return http.response_json(response)


class Response:
    """
    wrapper for json response from hydra interface
    """

    def __init__(self, data):
        self.data = data

    def total(self):
        """
        get total number of records from response
        """
        if 'totalItems' in self.data:
            return int(self.data['totalItems'])
        return 0

    def members(self):
        """
        get record data from response
        """
        if 'member' in self.data:
            return self.data['member']
        return []

    def view_next(self):
        """
        get url of next items from result set
        """
        if 'view' in self.data:
            if 'next' in self.data['view']:
                return self.data['view']['next']
        return ""
