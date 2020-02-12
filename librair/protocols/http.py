#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from ..schemas import xml


def get_request(url, headers={}):
    """
    send http get request to given url with headers (optional)
    """
    return requests.get(url, headers=headers)


def response_text(response):
    """
    get text data from http repsonse
    """
    if response.status_code == 200:
        return response.text
    else:
        print("something went wrong!")
        print("http status code: ",
              str(response.status_code))
        return ""


def response_json(response):
    """
    get json data from http repsonse
    """
    if response.status_code == 200:
        return response.json()
    else:
        print("something went wrong!")
        print("http status code: ",
              str(response.status_code))
        return {}


def response_xml(response):
    """
    get xml data from http repsonse
    """
    if response.status_code == 200:
        parser = xml.etree.XMLParser(remove_blank_text=True)
        return xml.etree.fromstring(response.content, parser=parser)
    else:
        print("something went wrong!")
        print("http status code: ",
              str(response.status_code))
        return None
