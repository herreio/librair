#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# ///////////////// #
# /// PLAIN I/O /// #
# ///////////////// #


def reader(path, encoding="utf-8"):
    """
    read txt file from given path
    """
    if os.path.exists(path):
        with open(path, "r", encoding=encoding) as f:
            # return list of without line breaks
            return [line.strip() for line in f]
    else:
        print("path does not exists!")
        return None


def writer(data=None, file="out.txt", path="."):
    """
    write given data (str or list of str) to txt file at path
    """
    if data is None:
        print("please pass data!")
        return None
    if type(data) == list:
        data = "\n".join(data)
    if not os.path.exists(path):
        os.makedirs(path)
    out = os.path.join(path, file)
    with open(out, 'w', encoding="utf-8") as f:
        f.write(data)
