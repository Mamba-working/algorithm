"""
选择排序
"""
def find_small(arr):
    small = arr[0]
    small_index = 0
    for i in range(len(arr)):
        if arr[i] <small :
            small = arr[i]
            small_index = i
        else:
            continue
    return small_index

def selectSort(arr):
    newarr = []
    for i in range(len(arr)):
        small = find_small(arr)
        newarr.append(arr.pop(small))
    return newarr
"""
test
arr = [1,3,6,12,15,345,222,23,44,233,33]
print(selectSort(arr))
"""