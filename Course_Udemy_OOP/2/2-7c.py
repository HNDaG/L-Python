class Person:
    pass

class Program:
    lang = "Py"
    ver = "3.6"

print(Program.lang, getattr(Program, "ver"))
Program.ver = "3.7"
print(Program.lang, getattr(Program, "ver"))
print(Program.lang, getattr(Program, "id", "NA"))
