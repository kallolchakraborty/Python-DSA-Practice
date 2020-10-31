#------------------------------------------------------#
# Description      : Reversing an array                #
# Time Complexity  : O(n)                              #
# Space Complexity : O(1)                              #
# Date             : 31/10/2020                        #
#------------------------------------------------------#

array = ['1','2','3','4','5','6','7','8','9']
print('The original array is: ', array)
print('The reversed array using list slicing is: ', array[::-1])

print()

array = ['1','2','3','4','5','6','7','8','9']
print('The original array is: ', array)
array.reverse()
print('The reversed array using the reverse method is: ', array)
