#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .schemas import plain
from .protocols import http


class Beacon:
    """
    Beacon parser for files exposed by given path or url
    """

    def __init__(self, path="", url=""):
        self.path = path
        self.url = url
        self.raw = []
        self.meta = {}
        self.links = []
        self.targets = []
        self.size = 0
        if path != "":
            self._read()
        if url != "":
            self._retrieve()
        self._parse()

    def __str__(self):
        repr = []
        for k in self.meta:
            ws = 15 - len(k)
            repr.append(k + ws * " " + self.meta[k])
        return "\n".join(repr)

    def _retrieve(self):
        self.raw = http.response_text(http.get_request(self.url)).split("\n")

    def _read(self):
        self.raw = plain.reader(self.path)

    def _parse(self):
        temp = [r for r in self.raw[:20] if r.startswith("#")]
        temp = [t.replace("#", "").split(":", 1) for t in temp]
        temp = [[t[0].strip(), t[1].strip()] for t in temp]
        for t in temp:
            self.meta[t[0]] = t[1]
        temp = [r for r in self.raw if "#" not in r and r != ""]
        self.size = len(temp)
        temp = [t.split("|") for t in temp]
        for t in temp:
            self.links.append(t[0])
            self.targets.append(t[1:]) if len(t[1:]) > 1 \
                else self.targets.append(t[1])

    def save(self, file="beacon.txt", path="."):
        """
        save beacon data to given path and file
        """
        plain.writer(self.raw, file=file, path=path)
