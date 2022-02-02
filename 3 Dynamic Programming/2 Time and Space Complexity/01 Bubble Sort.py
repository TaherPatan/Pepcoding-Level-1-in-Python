def swap(arr, i, j):
    print("Swapping", arr[i], "and", arr[j])
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def isSmaller(arr,i,j):
    print("Comparing",arr[i],"and",arr[j])
    if arr[i] < arr[j]:
        return True
    else:
        return False


def bubbleSort(arr):
  for i in range(1, len(arr)):
      for j in range(0, len(arr) - i):
          if isSmaller(arr, j + 1, j):
              swap(arr, j + 1, j)


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end="\n")
    print()


if __name__ == '__main__':
    arr = []
    n = int(input())
    for i in range(0, n):
        ele = int(input())
        arr.append(ele) 
    bubbleSort(arr)
    printList(arr)
