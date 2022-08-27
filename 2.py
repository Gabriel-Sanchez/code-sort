
def heapsort(MyList):
  n = len(MyList)
  for i in range(n//2, -1, -1):
    heapify(MyList, n-1, i)

  for i in range(n-1, -1, -1):
    
    MyList[i], MyList[0] = MyList[0], MyList[i]

    heapify(MyList, i-1, 0)

def heapify(MyList, n, i):
  max, left, right = i, 2*i + 1, 2*i + 2
 
  if left <= n and MyList[left] > MyList[max]:
    max = left

  if right <= n and MyList[right] > MyList[max]:
    max = right

  if max != i:
    MyList[i], MyList[max] = MyList[max], MyList[i]
    
    heapify(MyList, n, max) 

def PrintList(MyList):
  for i in MyList:
    print(i, end=" ")
  print("\n")
  
MyList = [10, 1, 23, 50, 7, -4]
n = len(MyList)
print("Original List")
PrintList(MyList)

heapsort(MyList)
print("Sorted List")
PrintList(MyList)