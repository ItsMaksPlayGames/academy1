class Cat:
    def __self__(self, name):
        print("start creating cat")
        self.name = name
        self.hp = 100
        self.sleep = 0
        print("finish creating the cat")

    def show_info(self):
        print("Name:", self.name)
        print("Hp:", self.hp)
        print("Sleep energy:", self.sleep)

    def set_name(self, new_name):
        self.name = new_name

    def set_hp(self, hp):
        if hp < 100 and hp > 0:
            self.hp = hp
        else:
            print("error hp")

    def set_sleep(self, sleep):
        if sleep > 0:
            self.sleep - sleep

    def is_alive(self):
        return self.hp > 0

    def damage(self, amount):
        self.sleep-=amount
        self.hp-=self.sleep
        if self.hp<0:
            print("Cat died")


    def add_sleep(self, amount):
        self.sleep += amount

    def heal(self, hp):
        if self.sleep > 15:
            self.hp += hp



from random import randint

cat = Cat("Dog")
cat.show_info()

while cat.is_alive():
    num =randint(1, 2)
    if num == 1:
        cat.damage(randint(1, 20))
    elif num == 2:
        cat.add_sleep(randint(1, 10))
    if cat.hp <= 20:
        cat.heal(randint(1, 10))
    elif cat.hp > 20:
        cat.heal(randint(0, 20))

cat.show_info()