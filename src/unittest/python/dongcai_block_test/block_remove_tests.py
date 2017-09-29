
#encoding=utf-8
__author__ = 'tangr'

# from dongcai_block_test import BlockTestCase
import unittest
import json
from dongcai_block import block_remove
import os 
from pymongo import MongoClient
class BlockWrite(unittest.TestCase):

    def _connect_mongo(self):

        host = os.environ.get('MYDB_PORT_27017_TCP_ADDR',"127.0.0.1")
        client = MongoClient(host)
        db = client.F10data3
        return db
      

    def test_remove_block(self):  
    	db = self._connect_mongo()
    	block_remove.remove_block(db)


    def test_remove_block_stock(self):  
    	db = self._connect_mongo()
    	block_remove.remove_block_stock(db)
