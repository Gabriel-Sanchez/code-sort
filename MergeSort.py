def mergesort(MyList, left, right):
  if left < right:
    mid = left + (right - left)//2
    mergesort(MyList, left, mid)
    mergesort(MyList, mid+1, right)
    merge(MyList, left, mid, right)

def merge(MyList, left, mid, right):
  n1 = mid - left + 1  
  n2 = right - mid     
  LeftList = MyList[left:mid+1] 
  RightList = MyList[mid+1:right+1]

  x, y, z = 0, 0, left
  while x < n1 and y < n2:
    if LeftList[x] < RightList[y]: 
      MyList[z] = LeftList[x] 
      x+=1 
    else:
      MyList[z] = RightList[y]  
      y+=1 
    z+=1

  while x < n1:
    MyList[z] = LeftList[x]  
    x+=1  
    z+=1

  while y < n2:
    MyList[z] = RightList[y]
    y+=1  
    z+=1 
    
def PrintList(MyList):
  for i in MyList:
    print(i, end=" ")
  print("\n")

MyList = [10, 1, 23, 50, 4, 9, -4]
n = len(MyList)
print("Original List")
PrintList(MyList)

mergesort(MyList, 0, n-1)
print("Sorted List")
PrintList(MyList)