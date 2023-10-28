# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.countLife = 9
#
#     def show_info(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.name}")
#         print(f"Count life: {self.countLife}")
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.devotion = 100
#
#     def show_info(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.name}")
#         print("Counter devotion:", self.devotion)

class Animal:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.name}")

    def golos(self):
        pass

class Cat(Animal):
    def __init__ (self, name, age):
        super().__init__(name, age)
        self.counterLife = 9

    def show_info(self):
        super().show_info()
        print("hello i am cat!")
        print("Counter life:", self.countLife)

    def service(self):
        print("mau mau")



cat = Cat("barsik", 10)
cat.show_info()
cat.golos()


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.devotion = 100

    def show_info(self):
        print("hello i am dog!")
        super().show_info()
        print("Counter devotion:", self.devotion)

    def golos(self):
        print("gaw gaw")


dog = Dog("Bobik", 6)
Dog.show_info()
Dog.golos()


