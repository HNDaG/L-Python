#from posixpath import split


def main():
    email = input("Email to split: ")

    (username, domain)= email.split("@")
    (domain, extention) = domain.split(".")

    print(username, domain, extention)


main()


#split returns a list

"""
txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)

print(x)


"""