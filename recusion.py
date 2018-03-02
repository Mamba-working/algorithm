
def sum(list):
    if list == []:
        return 0;
    return list[0]+sum(list[1:])

def count(arr):
    if arr == []:
        return 0
    else:
        return count(arr[1:])+1

arr = [1,2,3,4,5,6,7]


print(sum(arr))
print(count(arr))