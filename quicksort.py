import random
def quicksort(list):
    if len(list)<2:
        return list
    else:
        rad = random.randint(0,len(list)-1) 
        pivot = list[rad]
        smaller = [i for i in list[1:] if i<pivot]
        bigger = [i for i in list[1:] if i>=pivot]
        return quicksort(smaller) + [pivot] + quicksort(bigger)
list1 = [4,12,33,1,55,2,7,34,4]
print(quicksort(list1))