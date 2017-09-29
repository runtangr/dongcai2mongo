
#encoding=utf-8
__author__ = 'gbalaraman'

# from dongcai_block_test import BlockTestCase
import unittest
import json
from dongcai_block import block_write
import os 
from pymongo import MongoClient
class BlockWrite(unittest.TestCase):

    def _connect_mongo(self):

        host = os.environ.get('MYDB_PORT_27017_TCP_ADDR',"127.0.0.1")
        client = MongoClient(host)
        db = client.F10data3
        return db
      

    def test_save_data(self):  
        db = self._connect_mongo()
        block_data = {
                    "ClassId": "DH00451", 
                    
                    "SysCode":"行业板块", 
                    "SectionLevel": "0",
                    "PlateCode":"DH00451",
                    "SectionNameH":"房地产",
                    "SectionName":"房地产",
                    "gps":0,
                    "ComputerType":1 ,
                    "ShortCode":"XASD"
        }
        #"ShortCode":"XASD"
        block_write.save_data(db,  block_data)


    def test_block_section_stock(self):  
        db = self._connect_mongo()
        block_data = {
                    "ClassId": "DH00451", 
                 
                    "SysCode":"行业板块",
                    "SectionNameH":"房地产",
                    "SectionName":"房地产",
                    "PlateCode":"DH00451", 
                    "SectionLevel": "0",
                    "MarketCode": "DH",
                    "StockCode":"600639",
                    "StockShortName":"浦东金桥",
                    "Obj":"SH600639",
                    "bzzb":0,
        }

#         {u'Code': u'SH600639', u'PlateName': u'\u884c\u4e1a\u677f\u5757', 
#         u'Name': u'\u6d66\u4e1c\u91d1\u6865', u'TypeName': u'\u623f\u5730\u4ea7', 
#         u'SysCode': u'DH00451', u'Date': u'2017-09-27', u'TypeZm': u'F'}
# 浦东金桥
# SH600639
# 行业板块
# 房地产

        #"ShortCode":"XASD"
        block_write.save_block_section_stock(db,  block_data)


if __name__ == '__main__':
    unittest.main()
