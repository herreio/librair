#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from lxml import etree


# //////////////////// #
# /// XML PRINTING /// #
# //////////////////// #


def pretty(elements):
    """
    pretty print elements
    """
    print(etree.tostring(elements, pretty_print=True).decode())

# //////////////////// #
# /// XML HANDLING /// #
# //////////////////// #


def unlist(elements):
    """
    create tree from list of elements
    """
    root = etree.Element("response")
    numrecs = etree.Element("numberOfRecords")
    numrecs.text = str(len(elements))
    root.append(numrecs)
    recs = etree.Element("records")
    for e in elements:
        recs.append(e)
    root.append(recs)
    return root


# /////////////// #
# /// XML I/O /// #
# /////////////// #


def filepath(term, base, schema, service="sru"):
    """
    generate file path for given parameters
    """
    main = "-".join([term, base, service, schema])
    main = re.sub("^-", "", main)
    main = re.sub("-*$", "", main)
    main = re.sub("--", "-", main)
    return main + ".xml"


def writer(tree, file, path="res"):
    """
    write given element tree to file at path
    """
    parser = etree.XMLParser(remove_blank_text=True)
    xml = etree.ElementTree(tree, parser=parser)
    if path and not os.path.exists(path):
        os.makedirs(path)
    out = os.path.join(path, file)
    # keep xml response unmodified
    # declaration could be added like so:
    # encoding="UTF-8", xml_declaration=True
    xml.write(out, pretty_print=True)


def reader(path):
    """
    read xml file at given path
    """
    parser = etree.XMLParser(remove_blank_text=True)
    return etree.parse(path, parser=parser)


class Element:
    """
    wrapper for xml element
    """

    def __init__(self, tree, ns=None):
        self.raw = tree
        self.ns = None
        if ns is not None:
            self.ns = ns
        else:
            self.ns = self.namespace()

    def __repr__(self):
        return etree.tostring(self.raw, pretty_print=True).decode()

    def namespace(self):
        """
        extract full namespace (URL) from root element
        """
        if len(self.raw.nsmap) > 1 and None in self.raw.nsmap:
            return self.raw.nsmap[None]
        else:
            return list(self.raw.nsmap.values())[0]

    def xpath(self, tag, relative=True):
        """
        create xpath query for given tag
        """
        if relative:
            return ".//{" + self.ns + "}" + tag
        else:
            return "{" + self.ns + "}" + tag

    def find(self, tag, relative=True):
        """
        find tag in raw xml from namespace of root
        """
        query = self.xpath(tag, relative=relative)
        return self.raw.find(query)

    def findall(self, tag, relative=True):
        """
        find all tags in raw xml from namespace of root
        """
        query = self.xpath(tag, relative=relative)
        return self.raw.findall(query)
