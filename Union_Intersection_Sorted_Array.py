#--------------------------------------------------------------#
# Description      : Union & Intersection of two sorted arrays #
# Time Complexity  : O(n*m) -> Intersection & O(m+n) -> Union  #
# Space Complexity : O(1)                                      #
# Date             : 31/10/2020                                #
#--------------------------------------------------------------#

if __name__ == "__main__":
	A = [1, 2, 4, 9, 11, 22, 33] 
	B = [2, 3, 5, 7, 9, 33]
	print('Intersection Elements: ', list(set(A).intersection(B)))
	print('Union Elements: ', list(set(A).union(B)))
    