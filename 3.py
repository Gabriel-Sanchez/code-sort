def quicksort(MyList, left, right):
  if left < right:
    pivot = partition(MyList, left, right)
    quicksort(MyList, left, pivot-1)
    quicksort(MyList, pivot+1, right)   

def partition(MyList, left, right):
  i = left
  pivot = MyList[right]
  for j in range(left, right):
    if(MyList[j] < pivot):
      MyList[i], MyList[j] = MyList[j], MyList[i]
      i = i + 1
  MyList[i], MyList[right] = MyList[right], MyList[i]
  return i

def PrintList(MyList):
  for i in MyList:
    print(i, end=" ")
  print("\n")
  
MyList = [-4, 1, 25, 50, 8, 10, 23]
n = len(MyList)
print("Original List")
PrintList(MyList)

quicksort(MyList, 0, n-1)
print("Sorted List")
PrintList(MyList)