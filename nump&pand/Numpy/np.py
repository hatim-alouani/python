# import numpy as np

# myList = [1, 2, 3, 4, 5]
# myArray = np.array([1, 2, 3, 4])

# print(myList)
# print(myArray)

# print("#" * 50)

# print(type(myList))
# print(type(myArray))

# print("#" * 50)

# a = np.array(10)
# b = np.array([10, 20])
# c = np.array([[1, 2], [3,4]])
# d = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])

# print(d[0][0][-2])
# print(d[0,0,0])

# print("#" * 50)

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

# print("#" * 50)

# myCustomArray = np.array([1, 2, 3] , ndmin=3)

# print(myCustomArray)
# print(myCustomArray.ndim)
# print(myCustomArray[0][0][0])

# print("#" * 50)

# print(id(myList[0]))
# print(id(myList[1]))

# print(id(myArray[0]))
# print(id(myArray[1]))

# print("#" * 50)

# myListOfData = [1, 2, "A", 'B', True, 10.50]
# myArrayOfData = np.array([1, 2, "A", 'B', True, 10.50])

# print(myListOfData)
# print(myArrayOfData)

# print(type(myListOfData[0]))
# print(type(myArrayOfData[0]))

# myListOfData2 = [1, 2, "Hatim", 'B', True, 10.50]
# myArrayOfData2 = np.array([1, 2, 10.5])

# print(myListOfData2)
# print(myArrayOfData2)

# print("#" * 50)

# print(type(myListOfData2[0]))
# print(type(myArrayOfData2[0]))

# import time
# import sys

# elements = 15
# myList1 = range(elements)
# myList2 = range(elements)

# myArray1 = np.arange(elements)
# myArray2 = np.arange(elements)

# listStart = time.time()
# listResult = [(n1 + n2) for n1, n2 in zip(myList1, myList2)]
# print(f"list time : {time.time() - listStart}")

# arrayStart = time.time()
# arrayResult = myArray1 + myArray2
# print(f"array time : {time.time() - arrayStart}")

# for n1, n2 in zip(myList1, myList2):
#     print(n1 + n2)

# for n in myArray1:
#     print(n)

# print(listResult)

# myArray = np.arange(100)
# print(myArray)
# print(myArray.itemsize)
# print(myArray.size)
# print(myArray.size * myArray.itemsize)

# print("#" * 50)

# myList = range(100)
# print(sys.getsizeof(1))
# print(len(myList))
# print(sys.getsizeof(1) * len(myList))

#slicing arrays
# a = np.array(["A", "B", "C", "D", "E", "F"])
# print(a.ndim)
# print(a[1])
# print(a[1:4])
# print(a[:4])
# print(a[2:])

# print("#" * 50)

# b = np.array([["A", "B", "C"], ["D", "E", "F"], ["J", "H", "I"], ["M", "N", "O"]])
# print(b[1])
# print(b[:3, 0])
# print(b[:4])
# print(b[1:])

# myArray1 = np.array([1, 2, 3])
# myArray2 = np.array([1.9, 2.5, 3.6])
# myArray3 = np.array(["Ahhhdvdsv bfbfbh", "B", "C"])

# print(myArray1.dtype)
# print(myArray2.dtype)
# print(myArray3.dtype)

# myArray4 = np.array([1, 0.2, 3], dtype=float)
# myArray5 = np.array([1.9, 0.5, 3.6], dtype=int)
# myArray6 = np.array(["Ahhhdvdsv bfbfbh", "B", "C"])

# print(myArray5.dtype)
# myArray5 = myArray5.astype('i')
# print(myArray5.dtype)
# print(myArray5.itemsize)

# myArray = np.array([[6, 4], [3,9]])
# myArray2 = myArray.ravel()
# print(myArray.ndim)
# print(myArray.shape)
# rechapedArray = myArray2.reshape(4, 1, 1, 1)
# print(myArray2)
# print(rechapedArray)
# array = np.full((10, 2, 2), 6)
# print((array1))

# array = np.zeros(10)
# print(array)
# arr = np.array([1, 8, 4, 5, 2, 7, 3, 0, 2])

# array = np.sqrt(array)
# array = np.absolute(array)
# print((array))

# arr = array.view() # create a refrence
# arr = array.copy() # copy
# print((arr))

# for x in np.nditer(array):
#     print(x)


# print(np.sort(arr))



# arr = np.array(["vd", "dddd", "aaa", "fdhfg"])
# print(np.sort(arr))

# x = np.where(arr == 3)
# print(x)

# x = [True, False , False, True, False , False, True, False , False]
# print(arr[x])
# filtered = []
# for i in arr:
#     if arr[i] % 2 == 0:
#         filtered.append(True) #append() = add to the end of the list
#     else:
#          filtered.append(False)

# print(arr[filtered])