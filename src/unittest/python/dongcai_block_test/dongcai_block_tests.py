
#encoding=utf-8
__author__ = 'gbalaraman'

# from dongcai_block_test import BlockTestCase
import unittest
import json
import os
from dongcai_block import block_read
class TestBlockStorage(unittest.TestCase):

    def _read_data(self):
        file_path = "dongcai_block_data.txt"
        with open(file_path) as json_file:
            self._block_data  = json.load(json_file)
      

    def test_view(self):  
        self._read_data()
        print(self._block_data[0])


    def test_block_view(self):  
        self._read_data()
        block_views = []
        for data in  self._block_data:
            if data["TypeName"] == u"房地产":
                print(data)
                print(data["Name"])
                print(data["Code"])
                print(data["PlateName"])
                print(data["TypeName"])
                block_views.append(data)






if __name__ == '__main__':
    unittest.main()

    