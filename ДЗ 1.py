class Pasport:
    def __init__(self, country, name, surname, birth_date):
        self.country = country
        self.name = name
        self.surname = surname
        self.birth_date = birth_date

    def show_info(self):
        print(f"country: {self.country}")
        print(f"name: {self.name}")
        print(f"surname: {self.surname}")
        print(f"birth_date: {self.birth_date}")

class ForeignPassport(Pasport):
    def __init__(self, country, name, surname, birth_date, pasportnumber, visadatanumber):
        super().__init__(country, name, surname, birth_date)
        self.pasportnumber = pasportnumber
        self.visadatanumber = visadatanumber

    def show_info(self):
        super().show_info()
        print(f"Pasport_Number: {self.pasportnumber}")
        print(f"Visa_Number: {self.visadatanumber}")

foreign_passport = ForeignPassport("Ukraine", "Maks", "Moskalenko", "23.08.2008", "6745867648353576", "993987123")
foreign_passport.show_info()
