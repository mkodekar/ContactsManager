"""
CONTACT MANAGER
@VERSION 2
@author Rehan Kodekar
@DATE 2017-04-21
@:type object oriented approach
"""


class Person(object):
    def __init__(self, name, phoneNumber, emaild):
        self.name = name
        self.phone = phoneNumber
        self.email = emaild

    # Accesers
    def getName(self):
        return self.name

    def getPhone(self):
        return self.phone

    def getEmail(self):
        return self.email

    # Mutators
    def setName(self, newName):
        self.name = newName

    def setPhone(self, newPhone):
        self.phone = newPhone

    def setEmail(self, newemail):
        self.email = newemail

    def __str__(self) -> str:
        return '[' + self.getName() + ', ' + self.getPhone() + ', ' + self.getEmail() + ']'


def main():
    print('Contacts manager')
    friend1 = Person('Rehan Kodekar', '9167836937', 'mkodekar@zoho.com')
    print(friend1.getName())
    print(friend1)

if __name__ == '__main__':
    main()
