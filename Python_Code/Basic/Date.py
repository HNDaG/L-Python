import datetime

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A"))  # return week day


# To create a date, we can use the datetime() class (constructor) of the datetime module.

# The datetime() class requires three parameters to create a date: year, month, day.


y = datetime.datetime(2020, 5, 17)   # Timezone par can be used
print(y)
del y


z = input("Pause")
del z

print(x)  # Means that date is static

# Formatting 
# The datetime object has a method for formatting date objects into readable strings.
# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
print(x.strftime("%B"))



"""

"""