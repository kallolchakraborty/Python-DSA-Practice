#Array Rotation left
#Time Complexity : O(n)
#Space Complexity : O(1)
def gcd(a,b):
  if b == 0:
    return a
  return(gcd(b,a%b))

#Juggling Algorithm
def LeftArrayRotation(arr,arr_size,rotate):
  limit = gcd(arr_size,rotate)
  for i in range(limit):
    temp = arr[i]
    j = i
    while 1:
      k = (j+rotate)%arr_size   #Eg: rotate=3: (0+3)%9=3, a[0]=a[3]
      if k == i:
        break
      arr[j] = arr[k]
      j = k
    arr[j] = temp
    
  print("Rotated array is :\n", arr)

arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
print("The Original array is :\n", arr)
LeftArrayRotation(arr, 9, 3)


