import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$5^&*()-_+=[]<>,/?;:")

def generate_password():
    lenght = int(input("Lenght: "))
    random.shuffle(characters)

    password= []

    for x in range(lenght):
        password.append(random.choice(characters))
    return "".join(password)

print("Here it is:  %s    ---formatted output" % generate_password())
