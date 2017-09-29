# encoding=utf-8
__author__ = 'tangr'

import unittest
import json
import os
from pymongo import MongoClient
from dongcai_block import block_section_dc
from dongcai_block import block_section_stock_dc
from dongcai_block import block_read


class BlockSectionDc(unittest.TestCase):
    def _read_data(self):
        file_path = "dongcai_block_data.txt"
        with open(file_path) as json_file:
            self._block_data = json.load(json_file)

    def _connect_mongo(self):
        host = os.environ.get('MYDB_PORT_27017_TCP_ADDR', "127.0.0.1")
        client = MongoClient(host)
        db = client.F10data3
        return db

    def test_write_block_stock(self):
        db = self._connect_mongo()
        self._read_data()
        type_name = "房地产"
        block_datas = block_read.block_view(self._block_data, type_name)
        block_section_stock_dc.write_block_stock(db, block_datas)