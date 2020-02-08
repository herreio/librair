#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

urlenc = {
  " ": "%20",
  "=": "%3D",
  ">=": "%3E%3D",
  "=<": "%3D%3C"
}


def get_request(url, headers={}):
    """
    """
    return requests.get(url, headers=headers)


def response_json(response):
    """
    """
    if response.status_code == 200:
        return response.json()
    else:
        print("something went wrong!")
        print("http status code: ",
              str(response.status_code))
        return {}
