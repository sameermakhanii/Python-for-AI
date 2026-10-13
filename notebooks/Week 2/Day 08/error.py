def shout(func):
  def wrapper(name):
    if isinstance(name,str):
      return name.upper()
  return wrapper
name = input("enter name ")

@shout
def greet( name ):
   return name


print (greet(name))
print (f"hello{name}")