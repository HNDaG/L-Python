#classes ara callable

class Program:
    lan = "PY"

    def hello():
        print("Hello", Program.lan)

p = Program()
print(type(p))
print(isinstance(p, Program))