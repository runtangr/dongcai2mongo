
def remove_block(db):
	mongo_data = {}

	db["f10_6_1_block_section_dc"].remove({})


def remove_block_stock(db):
	mongo_data = {}

	db["f10_6_2_block_section_stock_dc"].remove({})