
def save_block(db, block_data):
	mongo_data = {}

	db["f10_6_1_block_section_dc"].insert(block_data)


def save_block_section_stock(db, block_data):
	mongo_data = {}

	db["f10_6_2_block_section_stock_dc"].insert(block_data)

def save_data(db, block_data):
	# print(block_data[0])
	# map(lambda data:save(db, collection, data), block_data)
	save_block(db, block_data)


# mongo_data["ClassId"] = data["SysCode"]
# 	# mongo_data["ClassfatherId"]
# 	mongo_data["SysCode"] = data["PlateName"]
# 	mongo_data["SectionLevel"] = "0"
# 	mongo_data["PlateCode"] = data["SysCode"]
# 	mongo_data["SectionNameH"] = data["TypeName"]
# 	mongo_data["SectionName"] = data["TypeName"]
# 		# mongo_data["gps"] = data[""]  //tongji
# 	mongo_data["ComputerType"] = 1
# 		# mongo_data["ShortCode"] = data[""]