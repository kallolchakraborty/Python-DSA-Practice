#--------------------------------------------------------------#
# Description      : Segregate 0s, 1s, 2s using Dutch National #
#                    Flag Algorithm OR 3-way Partitioning      #
# Time Complexity  : O(n)                                      #
# Space Complexity : O(1)                                      #
# Date             : 31/10/2020                                #
#--------------------------------------------------------------#

def seg_0_1_2(array):
    low, mid, high = 0, 0, len(array)-1
    
    while(mid <= high):
        if array[mid] == 0:
            array[mid], array[high] = array[high], array[mid]
            high -= 1
        elif array[mid] == 1:
            mid += 1
        elif array[mid] == 2:
            array[low], array[mid] = array[mid], array[low]
            low += 1
            mid += 1
    return array
    
if __name__ == "__main__":
    array = [0,1,2,0,1,2,0,1,2]
    print('The original array is: ', array)
    print('The segregated array is: ', seg_0_1_2(array))
