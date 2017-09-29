
from collections import Counter

def block_group(block_datas):

	block_groups_list =[]
	block_groups_dict ={}
	
	for block_data in block_datas:
			
		block_groups_list.append(block_data["TypeName"])

	block_groups_dict = Counter(block_groups_list)

	return block_groups_dict



		