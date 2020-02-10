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
