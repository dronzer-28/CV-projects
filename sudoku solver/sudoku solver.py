from typing import Tuple, List
# No other imports allowed

# PART OF THE DRIVER CODE

def input_sudoku() -> List[List[int]]:
	"""Function to take input a sudoku from stdin and return
	it as a list of lists.
	Each row of sudoku is one line.
	"""
	sudoku= list()
	for _ in range(9):
		row = list(map(int, input().rstrip(" ").split(" ")))
		sudoku.append(row)
	return sudoku

def print_sudoku(sudoku:List[List[int]]) -> None:
	"""Helper function to print sudoku to stdout
	Each row of sudoku in one line.
	"""
	for i in range(9):
		for j in range(9):
			print(sudoku[i][j], end = " ")
		print()

# You have to implement the functions below

def get_block_num(sudoku:List[List[int]], pos:Tuple[int, int]) -> int:
	"""This function takes a parameter position and returns
	the block number of the block which contains the position.
	"""
	# your code goes here
	
	return (((pos[0]-1)//3)*3+(pos[1]-1)//3+1)

def get_position_inside_block(sudoku:List[List[int]], pos:Tuple[int, int]) -> int:
	"""This function takes parameter position
	and returns the index of the position inside the corresponding block.
	"""
	r = (pos[0]-1)
	c = (pos[1]-1)
	ans =0
	# your code goes here
	if r%3 ==0:
		if c%3 ==0:
			ans =1
		elif c%3==1:
			ans =2
		elif c%3 == 2:
			ans = 3
	if r%3 ==1:
		if c%3 ==0:
			ans =4
		elif c%3==1:
			ans = 5
		elif c%3 == 2:
			ans = 6
	if r%3 ==2:
		if c%3 ==0:
			ans = 7
		elif c%3==1:
			ans = 8
		elif c%3 == 2:
			ans = 9
	return ans


def get_block(sudoku:List[List[int]], x: int) -> List[int]:
	"""This function takes an integer argument x and then
	returns the x^th block of the Sudoku. Note that block indexing is
	from 1 to 9 and not 0-8.
	"""
	# your code goes here
	list = []
	if x == 1:
		for i in range(0,3):
			for j in range(0,3):
				list.append(sudoku[i][j])
	if x == 2:
		for i in range(0,3):
			for j in range(3,6):
				list.append(sudoku[i][j])
	if x == 3:
		for i in range(0,3):
			for j in range(6,9):
				list.append(sudoku[i][j])
	if x == 4:
		for i in range(3,6):
			for j in range(0,3):
				list.append(sudoku[i][j])
	if x == 5:
		for i in range(3,6):
			for j in range(3,6):
				list.append(sudoku[i][j])
	if x == 6:
		for i in range(3,6):
			for j in range(6,9):
				list.append(sudoku[i][j])
	if x == 7:
		for i in range(6,9):
			for j in range(0,3):
				list.append(sudoku[i][j])
	if x == 8:
		for i in range(6,9):
			for j in range(3,6):
				list.append(sudoku[i][j])
	if x == 9:
		for i in range(6,9):
			for j in range(6,9):
				list.append(sudoku[i][j])

	return list
	

def get_row(sudoku:List[List[int]], i: int)-> List[int]:
	"""This function takes an integer argument i and then returns
	the ith row. Row indexing have been shown above.
	"""
	# your code goes here
	return sudoku[i-1]
	

def get_column(sudoku:List[List[int]], x: int)-> List[int]:
	"""This function takes an integer argument i and then
	returns the ith column. Column indexing have been shown above.
	"""
	# your code goes here
	col = []
	for c in range(0,9):          
		col.append(sudoku[c][x-1])
	return col

def find_first_unassigned_position(sudoku : List[List[int]]) -> Tuple[int, int]:
	"""This function returns the first empty position in the Sudoku. 
	If there are more than 1 position which is empty then position with lesser
	row number should be returned. If two empty positions have same row number then the position
	with less column number is to be returned. If the sudoku is completely filled then return `(-1, -1)`.
	"""
	# your code goes here
	for i in range(0,9):
		for j in range(0,9):
			if sudoku[i][j] == 0:
				return (i+1,j+1)

	return (-1,-1)

def valid_list(lst: List[int])-> bool:
	"""This function takes a lists as an input and returns true if the given list is valid. 
	The list will be a single block , single row or single column only. 
	A valid list is defined as a list in which all non empty elements doesn't have a repeating element.
	"""
	# your code goes here
	for i in range(0,len(lst)):
		for j in range(i+1,len(lst)):
			if lst[i] != 0 or lst[j] != 0:
				if lst[i] == lst[j]:
					return False
	return True

def valid_sudoku(sudoku:List[List[int]])-> bool:
	"""This function returns True if the whole Sudoku is valid.
	"""
	# your code goes here

	for i in range(0,9):
		if valid_list(get_column(sudoku,i)) == False:
			return False
	for i in range(0,9):
		if valid_list(get_row(sudoku,i)) == False:
			return False
	for i in range(0,9):
		if valid_list(get_block(sudoku,i+1)) == False:
			return False
	return True




def get_candidates(sudoku:List[List[int]], pos:Tuple[int, int]) -> List[int]:
	"""This function takes position as argument and returns a list of all the possible values that 
	can be assigned at that position so that the sudoku remains valid at that instant.
	"""
	# your code goes here
	row = get_row(sudoku,pos[0])
	col = get_column(sudoku,pos[1])
	block_num = get_block_num(sudoku,pos)
	block = get_block(sudoku,block_num)
	candidates_list = []
	for i in range(0,9):
		if (i+1) not in row and (i+1) not in col and (i+1) not in block:
			candidates_list.append(i+1)

	return candidates_list
	

def make_move(sudoku:List[List[int]], pos:Tuple[int, int], num:int) -> List[List[int]]:
	"""This function fill `num` at position `pos` in the sudoku and then returns
	the modified sudoku.
	"""
	# your code goes here
	sudoku[pos[0]-1][pos[1]-1] = num
	return sudoku

def undo_move(sudoku:List[List[int]], pos:Tuple[int, int]):
	"""This function fills `0` at position `pos` in the sudoku and then returns
	the modified sudoku. In other words, it undoes any move that you 
	did on position `pos` in the sudoku.
	"""
	# your code goes here
	sudoku[pos[0]-1][pos[1]-1] = 0
	return sudoku

def sudoku_solver(sudoku: List[List[int]]) -> Tuple[bool, List[List[int]]]:
	""" This is the main Sudoku solver. This function solves the given incomplete Sudoku and returns 
	true as well as the solved sudoku if the Sudoku can be solved i.e. after filling all the empty positions the Sudoku remains valid.
	It return them in a tuple i.e. `(True, solved_sudoku)`.

	However, if the sudoku cannot be solved, it returns False and the same sudoku that given to solve i.e. `(False, original_sudoku)`
	"""
	# your code goes here
	# to complete this function, you may define any number of helper functions.
	# However, we would be only calling this function to check correctness.
	position = find_first_unassigned_position(sudoku)
	while position !=(-1,-1):	
				row = position[0]	
				col = position[1]
				candidate = get_candidates(sudoku,(row,col))
				for val in candidate:
					make_move(sudoku, (row,col), val)
					checker = sudoku_solver(sudoku)[0]
					if checker:
						return (True,sudoku)
					else:
						undo_move(sudoku, (row,col))
				return (False, sudoku)

	return (True, sudoku)

# PLEASE NOTE:
# We would be importing your functions and checking the return values in the autograder.
# However, note that you must not print anything in the functions that you define above before you 
# submit your code since it may result in undefined behaviour of the autograder.

def in_lab_component(sudoku: List[List[int]]):
	print("Testcases for In Lab evaluation")
	print("Get Block Number:")
	print(get_block_num(sudoku,(4,4)))
	print(get_block_num(sudoku,(7,2)))
	print(get_block_num(sudoku,(2,6)))
	print("Get Block:")
	print(get_block(sudoku,3))
	print(get_block(sudoku,5))
	print(get_block(sudoku,9))
	print("Get Row:")
	print(get_row(sudoku,3))
	print(get_row(sudoku,5))
	print(get_row(sudoku,9))
	
	print("get position inside block")
	print(get_position_inside_block(sudoku,(1,1)))
	print(get_position_inside_block(sudoku,(4,6)))
	print(get_position_inside_block(sudoku,(5,5)))

	print("first unassigned position")
	print(find_first_unassigned_position(sudoku))

	print(valid_list(sudoku[0]))
	print(valid_list(sudoku[1]))
	print(valid_list(sudoku[2]))
	print("get candidates")
	print(get_candidates(sudoku, (1,3)))
	print(get_candidates(sudoku, (9,9)))
	print(get_candidates(sudoku, (5,7)))


	print(make_move(sudoku,(4,2),1))
	print("undo move")
	print(undo_move(sudoku, (4,5)))

# Following is the driver code
# you can edit the following code to check your performance.
if __name__ == "__main__":

	# Input the sudoku from stdin
	sudoku = input_sudoku()

	# Try to solve the sudok	
	possible, sudoku = sudoku_solver(sudoku)

	# The following line is for the in-lab component
	in_lab_component(sudoku)
	# Show the result of the same to your TA to get your code evaulated

	# Check if it could be solved
	if possible:
		print("Found a valid solution for the given sudoku :)")
		print_sudoku(sudoku)

	else:
		print("The given sudoku cannot be solved :(")
		print_sudoku(sudoku)