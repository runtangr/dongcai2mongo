
from block_read import connect_mongo
from block_read import read_file
from block_read import block_view
from block_write import save_data
from block_write import save_block

from section_builder import section_build
from block_remove import remove_block
from block_group import block_group


def write_block(db, block_datas, gps):

	block_stocks = map(lambda block_data:section_build(block_data, gps), block_datas)
	
	map(lambda block_stock:save_block(db, block_stock), block_stocks)
	

if __name__ == '__main__':

	file_path = "dongcai_block_data.txt"
	db = connect_mongo()

	block_datas = read_file(file_path)

	remove_block(db)

	block_groups_dict = block_group(block_datas)

	for type_name,gps in block_groups_dict.items():
		
		type_data= block_view(block_datas, type_name)

		write_block(db, type_data, gps)

	