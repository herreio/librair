#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json


# //////////////// #
# /// JSON I/O /// #
# //////////////// #


def filepath(term, base, schema, service="api"):
    """
    generate file path for given parameters
    """
    main = "-".join([term, base, service, schema])
    main = re.sub("^-", "", main)
    main = re.sub("-*$", "", main)
    main = re.sub("--", "-", main)
    return main + ".json"


def writer(data, file, path="res"):
    """
    write given dict data to json file at path
    """
    if path and not os.path.exists(path):
        os.makedirs(path)
    out = os.path.join(path, file)
    with open(out, 'w', encoding="utf-8") as f:
        s = json.dumps(data, indent=2)
        f.write(s)


def reader(path):
    """
    read json file from given path
    """
    result = {}
    with open(path, 'r', encoding='utf-8') as f:
        result = json.load(f)
    return result
