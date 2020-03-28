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


def writer(tree, file, path="."):
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
        self.ns = ns if ns is not None else self.namespace()

    def __repr__(self):
        return etree.tostring(self.raw, pretty_print=True).decode()

    def namespace(self):
        """
        extract full namespace (URL) from root element
        """
        if len(self.raw.nsmap) > 0:
            return self.raw.nsmap[None] if None in self.raw.nsmap else \
                list(self.raw.nsmap.values())[0]
        else:
            return None

    def xpath(self, tag, relative=True):
        """
        create xpath query for given tag
        """
        if self.ns is not None:
            return ".//{" + self.ns + "}" + tag if relative else \
                "{" + self.ns + "}" + tag
        else:
            return ".//" + tag if relative else tag

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
