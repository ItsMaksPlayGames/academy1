class Pet:
    def __init__(self, name):
        self.name = name
        self.happiness = 50

    def play(self):
        self.happiness += random.randint(5, 15)

    def feed(self):
        self.happiness += random.randint(1, 10)

    def adopt_pet(self, pet_name):
        self.pet = Pet(pet_name)
        print(f"{self.name} adopted a pet named {pet_name}!")

    def play_with_pet(self):
        if self.pet:
            self.pet.play()
            print(f"{self.name} played with {self.pet.name}!")
        else:
            print(f"{self.name} doesn't have a pet to play with.")

    def feed_pet(self):
        if self.pet:
            self.pet.feed()
            print(f"{self.name} fed {self.pet.name}.")
        else:
            print(f"{self.name} doesn't have a pet to feed.")


class Human:
    def __init__(self, name="Human", job=None, home=None,car=None):
        self.name = name
        self.money = 100
        self.job = job
        self.car = car
        self.home = home
        self.gladness = 50
        self.pet = Pet


    def get_car(self):
        self.car =Car("audi")

    def get_home(self):
        self.home = House()

    def get_job(self):
        self.job = Job()

    def get_pet(self):
        self.pet = Pet("Robert")

    def work(self):
        self.money += self.job.salary
        self.gladness -= random.randint(1,10)

    def chill(self):
        self.gladness += random.randint(5, 15)
        self.money -= random.randint(10, 20)

    def clean_home(self):
        if self.gladness < 25:
            print("it time to clean the house!")


    def is_alive(self):
        if self.gladness <=0:
            print("Depression")
            return False
        elif self.money < 100:
            print("Bankrupt")
            return False

    def live(self):
        if self.is_alive():
            return False
        elif self.home is None:
            print("Settled in the house")
            self.get_home()
        elif self.car in None:
            self.get_car()
            print("Bought new car -", self.car.brand)

        if self.job is None:
            self.get.job()
            print("I have got a new job", self.job.job, "with salary", self.job.salary)

        if self.money <= 0:
            self.work()
            print("go to work!")
        elif self.gladness < 20:
            self.chill()

        dice =random.randint(1, 2)
        if dice == 1:
            self.work()
        elif dice == 2:
            self.chill()


import random

class Job:
    def __init__(self):
        self.job = random.choice(("developer", "driver", "teacher", "taxi"))
        self.salary = random.randint(100, 200)

class House:
    def __init__(self):
        self.food = 0
        self.mess = 0


class Car:
    def __init__(self, brand):
        self.brand = brand
        self.countHuman = 2
        self.passengers = []

    def add_passenger(self, *args):
        for human in args:
            self.passengers.append(human)

    def show_passengers(self):
        if self.passengers != []:
            print("Model: ", self.brand)
            for human in self.passengers:
                print(human.name)
        else:
            print("There are no passengers in car!")

nick = Human("Nick")
kate = Human("Kate")
car = Car("audi")
car.add_passenger(nick, kate)
car.show_passengers()

nick = Human("Nick")
nick.adopt_pet("Robert")
while nick.is_alive():
    nick.live()
    if nick.is_alive() is False:
        break


