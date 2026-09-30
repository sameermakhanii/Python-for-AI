class Animal:
    def speak (self):
        return "....."

class dog(Animal):
    def speak(self):
        return "bark"

class cat(Animal):
    def speak(self):
        return "Meow"

cat1 = cat()
print(cat1.speak())