class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print(f"The First Person name is {self.name} having age {self.age}")

p1 = Person("John", 36)
print(p1.name)
print(p1.age)
p1.myfunc()
