
from block_read import connect_mongo
from block_read import read_file
from block_write import save_data
from block_write import save_block_section_stock
from section_builder import section_build_stock
from block_remove import remove_block_stock
from block_group import block_group
from block_read import block_view_stock

def write_block_stock(db, block_datas):

	block_stocks = map(lambda block_data:section_build_stock(block_data), block_datas)
	
	map(lambda block_stock:save_block_section_stock(db, block_stock), block_stocks)
	

if __name__ == '__main__':

	file_path = "dongcai_block_data.txt"
	db = connect_mongo()
	
	block_datas = read_file(file_path)

	remove_block_stock(db)

	# write_block_stock(db, block_datas)

	block_groups_dict = block_group(block_datas)

	for type_name in block_groups_dict.keys():
		
		type_data= block_view_stock(block_datas, type_name)

		write_block_stock(db, type_data)

	