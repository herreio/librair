#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import argparse

from . import services


def main(gnd=None, zdb=None):
    if gnd is not None:
        response = services.entityfacts.request(gnd)
        return json.dumps(response, ensure_ascii=False, indent=2)
    if zdb is not None:
        response = services.zdb.request(zdb)
        return json.dumps(response, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='librair',
                                     description="Retrieve library data")
    parser.add_argument("--gnd",
                        type=str,
                        help="GND ident number of entity to retrieve",
                        metavar="GND-ID")
    parser.add_argument("--zdb",
                        type=str,
                        help="ZDB ident number of serial item to retrieve",
                        metavar="ZDB-ID")
    gnd = parser.parse_args().gnd
    if gnd is not None:
        response = main(gnd=gnd)
        print(response)
    zdb = parser.parse_args().zdb
    if zdb is not None:
        response = main(zdb=zdb)
        print(response)
