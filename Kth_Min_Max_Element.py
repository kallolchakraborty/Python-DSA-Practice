#------------------------------------------------------#
# Description      : "Kth" max and min element         #
# Time Complexity  : O(nlogn)                          #
# Space Complexity : O(n)                              #
# Date             : 31/10/2020                        #
#------------------------------------------------------#

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        
    #Recursive call on each half
        merge_sort(left)
        merge_sort(right)
    
    # Two iterators for traversing the two halves
        i, j = 0, 0
    
    # Iterator for the main list
        k = 0
    
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              # The value from the left half has been used
              array[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                array[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1
    
        # For all the remaining values
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
            
if __name__ == "__main__":
    array = [11,2,35,4,25,6,7,88,9]
    print('The original array is: ', array)
    merge_sort(array)
    kmin, kmax = 1, 5
    print('The Kth min element is: ', array[kmin])
    print('The Kth max element is: ', array[kmax])
