#-----------------------------------------------------#
# Description      : Sort 0s, 1s, 2s using Merge Sort #
# Time Complexity  : O(nlogn)                         #
# Space Complexity : O(n)                             #
# Date             : 31/10/2020                       #
#-----------------------------------------------------#

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        
    #Recursive call on each half
        merge_sort(left)
        merge_sort(right)
    
    # Two iterators for traversing the two halves & for the main list
        i, j, k = 0, 0, 0
    
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
    array = [0,1,2,0,1,2,0,1,2]
    print('The original array is: ', array)
    merge_sort(array)
    print('The sorted array is: ', array)
