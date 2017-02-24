#!/usr/bin/env python

import sys, os
from lxml import etree
from cStringIO import StringIO

def cdata_inward(node):
    if node.text and node.from_cdata:
        node.wrap_raw_content("cdata")
    for child in node:
        cdata_inward(child)

with open(sys.argv[1]) as file_obj:
    xml_tree = etree.parse(file_obj, parser=etree.XMLParser(huge_tree=True, strip_cdata=False, ns_clean=True))

    cdata_inward(xml_tree.getroot())
    with open(sys.argv[2], 'w') as file_out:
        xml_tree.write(file_out, encoding=xml_tree.docinfo.encoding, pretty_print=False, xml_declaration=True)