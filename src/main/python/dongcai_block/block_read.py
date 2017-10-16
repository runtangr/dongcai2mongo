#encoding=utf-8
import pymongo
import sys
from pymongo import MongoClient
import os
import json


def read_file(file_path):

    with open(file_path) as json_file:
        block_data = json.load(json_file)
        return block_data

def connect_mongo():

	host = os.environ.get('MYDB_IP_ADDR',"127.0.0.1")
	port = os.environ.get('MYDB_PORT',27017)
	client = MongoClient(host, int(port))
	db = client.F10data3
	return db

def block_view_stock(block_data, type_name):
	block_views = []
	for data in  block_data:
	    if data["TypeName"] == type_name:
	        # print(data)
	        # print(data["Name"])
	        # print(data["Code"])
	        # print(data["PlateName"])
	        # print(data["TypeName"])
	        block_views.append(data)

	return block_views


def block_view(block_data, type_name):
	block_views = []
	for data in  block_data:
	    if data["TypeName"] == type_name:
	        # print(data)
	        # print(data["Name"])
	        # print(data["Code"])
	        # print(data["PlateName"])
	        # print(data["TypeName"])
	        block_views.append(data)
	        break

	return block_views