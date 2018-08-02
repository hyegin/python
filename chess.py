from copy import deepcopy

def check_pos(board, i , j, piece):
	
	if(piece == 1):
		if(board[i][j] == 2):
			return True
		else:
			return False
	else:
		if(board[i][j] == 1):
			return True
		else:
			return False
def check_pos2(board, i ,j , piece):
	if(board[i][j] == 0):
		print("True")
		return True
	print("False")
	return False

def adjustBoard(board, old_i, old_j, new_i, new_j, piece):
	temp_board = deepcopy(board)
	temp_board[old_i][old_j] = 0
	temp_board[new_i][new_j] = piece
	printBoard(temp_board)

def checkMoves(board, i, j, checker, piece):
	temp_board = deepcopy(board)
	'''special cases first'''
	#at 0 row
	#at n row
	#at 0 col
	#at n col
	
	if(piece == 1):
		if(board[i][j] == 0 or board[i][j] == 2):
			return
		print("Original Board1")
		printBoard(temp_board)
		print("i: " , i ," j: ", j)
		print("~~~~~~~~~~~~~~~~~")
		if(i == 0):
			'''0 row'''
			if(j == 0):
				'''0 column '''
				#thus only check bottom, bottom right, and right
				if(check_pos(board, i + 1, j + 1, piece)):
					adjustBoard(board, i, j, i + 1, j + 1, piece)
			'''0 row'''
			if(j == len(board[i]) - 1):
				'''final column'''
				#thus check left, bottom, bottom left
				if(check_pos(board, i + 1, j - 1, piece)): # bottom left
					adjustBoard(board, i , j , i + 1 , j - 1, piece)


		if((j != 0 ) and (j != len(board[i]) - 1)): # somewhere in the middle? at top row

				if(check_pos(board,i + 1, j - 1, piece)):
					adjustBoard(board, i, j, i + 1, j - 1, piece)
				if(check_pos(board, i + 1, j + 1, piece)):
					adjustBoard(board, i, j , i + 1, j + 1, piece)
		if(check_pos2(board, i + 1, j, piece) and board[i + 1][j] == 0): #empty space at the bottom of us
			adjustBoard(board, i, j , i + 1, j, piece)
	elif(piece == 2):
		if(board[i][j] == 0 or board[i][j] == 1):
			return
		print("Original Board2")
		printBoard(temp_board)
		print("i: " , i ," j: ", j)
		print("~~~~~~~~~~~~~~~~~")

		if(j == 0):
			'''0 column '''
			#thus only check  top right
			if(check_pos(board, i - 1, j + 1, piece)):
				adjustBoard(board, i, j, i -1, j + 1, piece)
		'''0 row'''
		if(j == len(board[i]) - 1):
			'''final column'''
			#thus check  top left
			if(check_pos(board, i -1, j - 1, piece)): # bottom left
				adjustBoard(board, i , j , i - 1 , j - 1, piece)
		if((j != 0 ) and (j != len(board[i]) - 1)):
			if(check_pos(board,i - 1, j - 1, piece)):
					adjustBoard(board, i, j, i - 1, j - 1, piece)
			if(check_pos(board, i - 1, j + 1, piece)):
				adjustBoard(board, i, j , i - 1, j + 1, piece)
		if(check_pos2(board, i - 1, j, piece)): #empty space at the toop
			adjustBoard(board, i, j , i - 1, j, piece)

	print("All moves done!")
	print("~~~~~~~~~~~~~~~~~~~~")





def move_maker(board, color):
	''' this function does some board shit.'''
	for i in range(0, len(board)):
		checker = 0
		for j in range(0, len(board[i])):
			if(board[i][j] == 1):
				'''if this is true, we want to see every move the piece can make'''
				checkMoves(board, i, j, checker, color)
				checker += 1
			elif(board[i][j] == 2):
				checkMoves(board,i,j,checker,color)
				checker+=1


def printBoard(board):
    print("   ", end = "")
    for i in range(0, len(board[0])):
        print(str(i)+" ", end = "")

    print("\n")
    row = 0
    for r in board:
        print(row, " ", end = "")
        for c in r:
            if c == 1:
                print("w ", end = "")
            elif c == 2:
                print("b ", end = "")
            else:
                print("- ", end = "")
        print()
        row = row + 1
    print()
            

