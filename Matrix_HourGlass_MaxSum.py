#Matrix Hour-Glass Max Sum
#Time Complexity : O(n2)
#Space Complexity : O(1)
def Matrix_Hour_Glass(mat, row, col):
  max_sum = 0
  #Total number of hourglasses : (row-2)*(col-2)
  for i in range(row-2):
    for j in range(col-2):
      #Sum of top 3 elements
      top = sum(mat[i][j:j+3])

      #Mid element
      mid = mat[i+1][j+1]
      
      #Sum of bottom 3 elements
      bottom = sum(mat[i+2][j:j+3])

      #Local Hourglass Sum
      hourglass = top + mid + bottom

      if hourglass > max_sum:
        max_sum = hourglass

  print('The Maximum Hourglass Sum is : ',max_sum)


mat = [[3, 2, 3, 0, 2], 
       [0, 0, 0, 0, 1], 
       [2, 1, 4, 0, 1], 
       [0, 2, 0, 0, 1], 
       [8, 1, 0, 1, 1]]

Matrix_Hour_Glass(mat,5,5)
