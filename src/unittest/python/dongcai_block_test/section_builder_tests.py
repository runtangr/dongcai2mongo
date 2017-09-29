
#encoding=utf-8
__author__ = 'gbalaraman'

# from dongcai_block_test import BlockTestCase
import unittest
import json
import os 
from dongcai_block import section_builder

class SectionBuild(unittest.TestCase):



    def test_section_build_stock(self):  

        source =  {u'Code': u'SH600639', u'PlateName': u'\u884c\u4e1a\u677f\u5757', 
        u'Name': u'\u6d66\u4e1c\u91d1\u6865', u'TypeName': u'\u623f\u5730\u4ea7', 
        u'SysCode': u'DH00451', u'Date': u'2017-09-27', u'TypeZm': u'F'}

        rest = section_builder.section_build_stock(source)
        print("rest = ",rest)
        self.assertTrue(rest["StockCode"]==u'600639')
       