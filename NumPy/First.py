import numpy as np

arr = np.array([0,1,2,3,4,5,6,7,8,9])
# arr = np.array([[1, 2, 3], [4, 5, 6]])

# newArr = arr.astype(bool)
# print(arr.reshape(2,5))

# for x  in np.nditer(arr):

#     print(x)


# print(newArr)


for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)