

from string import ascii_lowercase


list1 = list(map(chr, (range(ord('a'), ord('z')+1))))
list1 = list(reversed(list1))
list2 = list(map(chr, (range(ord('a'), ord('z')+1))))
print(list1)
print(list2)

dict1 =dict(zip(list1, list2))
print(dict1)

# One line solution
# dict2 = dict(zip(list(ascii_lowercase), reversed(list((ascii_lowercase)))))
# print(dict2)

while True:
    i = input("Enter char:  ")
    i = i.lower()
    print("{}  - - - {}".format(i, dict1[i]))

