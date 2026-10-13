def shout(func):
    def inner(name):
        return func(name).upper()
    return inner

name = input ("enter name ")

@shout
def greet(name):
    return f"hello {name}"

print (greet(name))
    
