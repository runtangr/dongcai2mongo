
#encoding=utf-8
__author__ = 'tangr'

# from dongcai_block_test import BlockTestCase
import unittest
import json
from dongcai_block import block_group
import os 
from pymongo import MongoClient

class BlockGroup(unittest.TestCase):

    def _read_data(self):
        file_path = "dongcai_block_data.txt"
        with open(file_path) as json_file:
            self._block_data  = json.load(json_file)

    def test_block_group(self):  
        self._read_data()
        block_groups = block_group.block_group(self._block_data)
        print("block_groups = ",block_groups)
       