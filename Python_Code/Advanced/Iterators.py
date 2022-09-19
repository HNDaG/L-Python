'''
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol, 
which consist of the methods __iter__() and __next__().

Iterator vs Iterable
Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

All these objects have a iter() method which is used to get an iterator:
'''

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#can be used with strings too 

mystr = "banana"
myit = iter(mystr)

next(myit)
print(next(myit))

#while looping throught list/.../... for acctualy creates an iterator

#to create an iterator in your class _iter_() and _next_() shoud be inplemented
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))

MYclasss = MyNumbers()
MYiterr = iter(MYclasss)
print(next(MYiterr))


#Adding a stopper 

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration  # HERE

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)