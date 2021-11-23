import json

class Vaccination(object):

    def __init__(self, SSN, name, Vaccine, vac_date, vac_address):
        self.SSN = SSN
        self.name = name
        self.Vaccine = Vaccine
        self.vac_date = vac_date
        self.vac_address = vac_address

    def confirmation(self):
        print(f'{self.name} has been vaccinated with {self.Vaccine} \non the {self.vac_date} at {self.vac_address}.')


user1 = Vaccination(123, 'Jack Bauer', 'Pfizer', '23-May-2021', 'Salbe Hospital, Berlin')
user2 = Vaccination(456, 'Valt Meuller', 'Johnson&Johnson', '02-January-2021', 'GH Memorial hospital, Deggendorf')
user3 = Vaccination(789, 'Penny Lustig', 'Pfizer', '21-May-2021', 'Hasselbank Hospital, Pfarrkirchen')
