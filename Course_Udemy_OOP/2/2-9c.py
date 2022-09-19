class program:
    lan = "PY"
    def hello():
        print(f"Hello from {program.lan}")

program.hello()
getattr(program, "hello") # func  -> no call
getattr(program, "hello")() # call




