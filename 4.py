def shellsort(MyList): 
  n = len(MyList)
  gap = n // 2 
  while gap > 0: 
    for i in range(gap,n): 
      temp = MyList[i] 
      j = i 
      while  j >= gap and MyList[j-gap] > temp: 
        MyList[j] = MyList[j-gap] 
        j = j - gap 
      MyList[j] = temp 
    gap = gap // 2

def PrintList(MyList):
  for i in MyList:
    print(i, end=" ")
  print("\n")
  
MyList = [10, 1, 23, 50, 4, 9, -4]
print("Original List")
PrintList(MyList)

shellsort(MyList)
print("Sorted List")
PrintList(MyList)