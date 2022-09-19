# In general can be said that there is global and  local 
# global keyword can be used 
# if name is the same in func it will be treated as different 

x = 300

def myfunc():
  x = 200 
  print(x)  # 200

myfunc()

print(x) # 300


#global
def myfunc():
  global x
  x = 300

myfunc()

print(x)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)