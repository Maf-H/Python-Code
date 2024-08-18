binary_tree_array = ['R', 'A', 'B', 'C', 'D', 'E', 'F', None, None, None, None, None, None, 'G']
# root_index = 0
# root.left = root_index * 2 + 1
# root.right = root_index * 2 + 2
length = len(binary_tree_array)
def left_child_index(index):
	if index <= length:
		return index * 2 + 1

def right_child_index(index):
	if index <= length:
		return index * 2 + 2


def pre_order(index):
	if index >= length or (binary_tree_array[index] is None):
		return []
	else:
		return [binary_tree_array[index]] + pre_order(left_child_index(index)) + pre_order(right_child_index(index))

def in_order(index):
	if index < length and (binary_tree_array[index] is not None):
		return in_order(left_child_index(index)) + [binary_tree_array[index]] + in_order(right_child_index(index))
	else:
		return []

def post_order(index):
	if index >= len(binary_tree_array) or binary_tree_array[index] is None:
		return []
	else:
		return post_order(left_child_index(index)) + post_order(right_child_index(index)) + [binary_tree_array[index]]

print(pre_order(0))
print(in_order(0))
print(post_order(0))




