#Array Rotation left
#Time Complexity : O(n)
#Space Complexity : O(1)

def LeftArrayRotation(arr, arr_size, rotate):
    #print("Rotated Array is\n", arr[rotate:] + arr[:rotate])
    #Formatting with the .format() method
    print("Rotated array by {} rotation is\n {}".format(rotate, arr[rotate:] + arr[:rotate]))

arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
print("The Original array is :\n", arr)
LeftArrayRotation(arr, 5, 3)


