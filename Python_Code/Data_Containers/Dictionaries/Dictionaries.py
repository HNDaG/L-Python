thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("---1---")
print(thisdict)
#Dictionary items are ordered, changeable, and does not allow duplicates.

#Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

#Getting acces
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("---2---")
#It's the same as using .get("brand") method 
print(thisdict["brand"])

#Keys
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
print("---3.1---")
print(x) #before the change

car["color"] = "white"
print("---3.2---")
print(x) #after the change

#Values
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
print("---4.1---")
print(x) #before the change

car["year"] = 2020
print("---4.2---")
print(x) #after the change


#If present 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "Ford" in thisdict:#At the moment it wont print anything, but if looking for model it will be the differt story
  print("---5---")
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#for X in thisdict.values():
#   print(X)