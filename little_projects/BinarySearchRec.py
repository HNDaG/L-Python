from os import system
from typing import List
import random


def BinarySearch(List: list, target, left, right):
    m = int((left+right+1)/2)
    print("Current m is:", m)
    if List[left] == target: 
        return left 
    elif List[right] == target:
        return right

    if right - left <=1 or m == left or m == right:
        return -1
    
    if target >= List[m]:
        return BinarySearch(List, target, m, right)
    else:
        return BinarySearch(List, target, left, m)


for i in range(1, 100):
    randomlist = []
    for i in range(0,30):
        n = random.randint(1,30)
        randomlist.append(n)

    randomlist.sort()
    print(randomlist)
    target = randomlist[random.randint(1, len(randomlist))-1]
    print("Target is ", target)
    ans = BinarySearch(randomlist, target, 0, len(randomlist)-1)
    print(ans)
    if (randomlist[ans] != target):
        system("pause")

    

