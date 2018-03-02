"""
二分查找
"""
def binary_search(list,item):
    low = 0
    high = len(list)-1

    while low<=high:
        mid = int((low+high)/2)
        guss = list[mid]
        if guss == item:
            return mid
        elif guss>item:
            high = mid - 1
        else:
            low = mid + 1
    return 'no result'
"""
This is a test.
test = [1,4,8,12,15,17,22,26,28,33,35,46,58,66,78]
print(binary_search(test,46))
"""

