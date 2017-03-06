# -*- coding:utf-8 -*-
import os
from os import listdir
from os.path import isfile, join
import xml.etree.ElementTree as ET

count_down = 0
count_up = 0
count_total = 0
count_error = 0

root_path = 'D:\\TMP\\20170228\\opt\\dr\\data\\nmap\\20170228'

for session_path in listdir(root_path):
    print session_path
    for file in listdir(os.path.join(root_path,session_path)):
        if file.endswith('.xml'):
            print "parsing: " + file
            try:
                tree = ET.ElementTree(file=os.path.join(root_path,session_path,file))
                for elem in tree.iterfind('runstats/hosts'):
                    if elem.attrib.get('total') == '0':
                        count_total += 1
                    if elem.attrib.get('up') == '0':
                        count_up += 1
                    if elem.attrib.get('down') == '0':
                        count_down += 1
            except:
                count_error += 1

print "sum: " + str(len(session_path))
print "count_total " + str(count_total)
print "count_up " + str(count_up)
print "count_down " + str(count_down)
print "count_error " + str(count_error)



