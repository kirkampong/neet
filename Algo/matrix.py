# SET MATRIX ZEROES
# Given an m x n integer matrix, if an element is 0, 
# set its entire row and column to 0's. You must do it IN PLACE.
# Approach:
# Good O(mxn) space, O(m*n)^2 time
#   - We can't simply iterate setting rows and columns as we go along
#       else we will be setting zeroes where we shouldn't 
#   - We can maintain a copy matrix which we don't change as we go along
#       we iterate over the non-modified version and modify the other O(mn)
# Better: O(m+n) space, O(mxn) time
#   - Instead of keeping a whole matrix copy, we can keep 2 just arrays 
#     lengths n & m for row and col O(m+n), we use these to mark each row
#     and col we should set to 0 as we go along then after and set all 0's
# Best: O(1) space, O(mxn) time
#   - use first r and c of matrix as tracking which r's,c's to set to 0
#   - We need one more cell since tracking row and col overlap at(0,0)
#   - Iterate over cells, setting [1st row] and [extra cell + 1st col[1;]]
#     to 0 to mark which r's and c's should be zeroed out
def setZeroes(matrix):
    numRows = len(matrix)
    numCols = len(matrix[0])
    # extra 'cell' to track first row 0
    rowZero = False 
    # mark rows and cols to zero out
    for r in range(numRows):
        for c in range(numCols):
            if matrix[r][c] == 0:
                #mark column be setting 1st row
                matrix[0][c] = 0
                #mark row be setting 1st col, except topLeft
                if r > 0:
                    matrix[r][0] = 0
                else:
                    rowZero = True
                    # continue ??
    # zero out marked r's and c's (excluding 1st r & c)
    for r in range(1,numRows):
        for c in range(1,numCols):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0
    # now zero out matrix[0][0] if needed
    if matrix[0][0] == 0:
        for r in range(numRows):
            matrix[r][0] = 0
    # check if we should zero out the first row
    
    if rowZero:
        for c in range(numCols):
            matrix[0][c] = 0
    
    return matrix


# SPIRAL MATRIX:
# Given an m x n matrix, return all elements of the matrix in spiral order.
# Approach:
#   - Keep a top, bottom, left, right boundary and decrement as we go along
def spiralMatrix(matrix):
    res = []
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)

    while left < right and top < bottom:
        # get top row values
        for i in range(left,right):
            res.append(matrix[top][i])
        top += 1 #shift top down
        
        # get right col values
        for i in range(top,bottom):
            res.append(matrix[i][right-1])
        right -= 1 # shift right inwards
        
        if not (left < right and top < bottom):
            break  # exit for single row or col matrix
        
        # get bottom row values
        for i in range(right-1,left-1,-1):
            res.append(matrix[bottom-1][i])
        bottom -= 1
        
        # get left col values
        for i in range(bottom-1, top-1, -1):
            res.append(matrix[i][left])
        left += 1
    return res


# ROTATE IMAGE:
# Given an nxn matrix, rotate it 90 degrees (clockwise).
# You have to rotate the image IN_PLACE
# Approach:
#   - Start from outer layer and work your way in
#   - Keep left, right, top, bottom boundaries and rotate corners first
#   - Then rotate inner positions (n-1) rotations
#   = Shift pointers inwards and repeat
#   - NOTE: We will rotate backwards(counter clockwise) to reduce tempVars
def rotateMatrix(matrix):
    # left, right tracks the current layer
    left ,right = 0 ,len(matrix)-1

    while left < right:
      # i shifts us from corners inwards on a given layer
      for i in range(right-left):
        top, bottom = left, right
        #save top left
        topLeft = matrix[top][left + i]

        #move bottom left into top left
        matrix[top][left + i] = matrix[bottom - i][left]

        #move bottom right into bottom left
        matrix[bottom - i][left] = matrix[bottom][right - i]

        #move top right into bottom right
        matrix[bottom][right - i] = matrix[top + i][right]

        #move top left into top right
        matrix[top + i][right] = topLeft
      #update pointers
      right -= 1
      left += 1
    return matrix


# WORD SEARCH: (SEE END OF TREES.PY FOR PART 2 - LIST OF WORDS INPUT!)
# Given an m x n grid and a string word, return true if word exists in grid.
# Traverse letters of adjacent cells (horizontally or vertically neighboring).
# The same letter cell may not be used more than once.
# Approach:
#   - Use simple brute force: Recursive DFS with backtracking
#   - Complexity ~ O(n * m * 4^len(word))
def wordExists(board,word):
  numRows = len(board)
  numCols = len(board[0])
  path = set() # tracks visited cells in path
  
  # i is position in word we're trying to match
  def dfs(row,col,i): 
    if i == len(word):
      return True
    if (row < 0 or col < 0 or
        row >= numRows or col >= numCols or
        word[i] != board[row][col] or 
        (row,col) in path):
        return False

    path.add((row,col))
    result = (dfs(row + 1, col, i + 1) or
              dfs(row - 1, col, i + 1) or
              dfs(row, col + 1, i + 1) or
              dfs(row, col - 1, i + 1))
    
    path.remove((row,col))
    return result

  for r in range(numRows):
    for c in range(numCols):
      if dfs(r,c,0):
        return True
  return False