#------------------------------------------------------------------#
# Description      : Segregate -ve & +ve elements using Merge Sort #
# Time Complexity  : O(n)                                          #
# Space Complexity : O(1)                                          #
# Date             : 31/10/2020                                    #
#------------------------------------------------------------------#

def segregate(array):
    i, j = 0, len(array)-1
    
    while(j > 1):
        while(array[i] < 0 and i < j):
            i += 1
            
        while(array[j] > 0 and i < j):
            j -= 1
        
        if(i < j):
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
        else:
            break
        
    return array
            
if __name__ == "__main__":
    array = [0,-11,2,-20,1,-32,-1,31,52]
    print('The original array is: ', array)
    print('The segregated array is: ', segregate(array))
