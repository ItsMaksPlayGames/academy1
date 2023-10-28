class Humans:
    def __init__(self, job, name,  salary):
        self.job = job
        self.name = name
        self.counterSalary = salary

    def show_info(self):
        print(f"Job: {self.job}")
        print(f"Name: {self.name}")
        print(f"Counter salary: {self.salary}")

class Pilot(Humans):
    def __init__ (self, job, name, salary):
        super().__init__(job,name,salary)
        self.counterSalary = 300

    def show_info(self):
        super().show_info()
        print("hello I am a Pilot!")
        print(f"Counter salary: {self.salary}")

    def SERVICE(self):
        print("its cost 100$")
class Builder(Humans):
    def __init__ (self, job, name, salary):
        super().__init__(job,name,salary)
        self.counterSalary = 200

    def show_info(self):
        super().show_info()
        print("hello I am a Builder!")
        print(f"Counter salary: {self.salary}")

    def SERVICE(self):
        print("its cost 80$")

class Sailor(Humans):
    def __init__ (self, job, name, salary):
        super().__init__(job,name,salary)
        self.counterSalary = 400

    def show_info(self):
        super().show_info()
        print("hello I am a Sailor!")
        print(f"Counter salary: {self.salary}")
    def SERVICE(self):
        print("its cost 100$")



