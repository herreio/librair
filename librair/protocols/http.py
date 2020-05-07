#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from ..schemas import xml


def get_request(url, headers={}):
    """
    send http get request to given url with (optional) headers
    """
    try:
        return requests.get(url, headers=headers)
    except requests.exceptions.ConnectionError:
        print("librair.protocols.http.get_request:")
        print("request failed! connection error...")
    except requests.exceptions.Timeout:
        print("librair.protocols.http.get_request:")
        print("request failed! timeout... try later?")
    except requests.exceptions.TooManyRedirects:
        print("librair.protocols.http.get_request:")
        print("request failed! bad url, try another one!")
    except requests.exceptions.RequestException:
        print("librair.protocols.http.get_request:")
        print("request failed! don't know why...")
    return None


def response_ok(response):
    if response is None:
        return False
    if response.status_code == 200:
        return True
    else:
        print("librair.protocols.http.response_ok:")
        print("response is not ok!")
        print("url of request:")
        print(response.url)
        print("http status code: ",
              str(response.status_code))
        return False


def response_text(response):
    """
    get text data from http repsonse
    """
    if response_ok(response):
        return response.text
    return ""


def response_json(response):
    """
    get json data from http repsonse
    """
    if response_ok(response):
        if response.json() is not None:
            return response.json()
    return {}


def response_xml(response):
    """
    get xml data from http repsonse
    """
    if response_ok(response):
        parser = xml.etree.XMLParser(remove_blank_text=True)
        return xml.etree.fromstring(response.content, parser=parser)
    else:
        return None
