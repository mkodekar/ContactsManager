class Person(object):
    def __init__(self, name, contactNumber, emailid):
        self.name = name
        self.contact = contactNumber
        self.email = emailid

    # Accesers
    def getName(self):
        return self.name

    def getContact(self):
        return self.contact

    def getEmail(self):
        return self.email

    # Mutators

    def setName(self, newName):
        self.name = newName

    def setContact(self, newPhone):
        self.contact = newPhone

    def setEmail(self, newemail):
        self.email = newemail

    def __str__(self) -> str:
        return '[' + self.getName() + ', ' + self.getContact() + ', ' + self.getEmail() + ']'


def enterAContact():
    name = input('Enter the name of the friend : ')
    contact = input('Enter contact number of the friend : ')
    email = input('Enter email id of the friend : ')
    return Person(name, contact, email)


def lookForFriend(friends):
    found = False
    name = input('Enter name of the friend to find : ')
    for friend in friends:
        if name in friend.getName():
            print(friend)
            found = True
        if not found:
            print('No friends found in the database')


def showAllFriends(friends):
    print('Showing all contacts')
    for friend in friends:
        print(friend)


def main():
    friends = []
    running = True
    while running:
        print('\nContacts manager')
        print('1) add a contact   2) find a friend')
        print('3) show all        4) end')
        option = input('>')
        if option == '1':
            friends.append(enterAContact())
        if option == '2':
            lookForFriend(friends)
        if option == '3':
            showAllFriends(friends)
        if option == '4':
            running = False
            
    print('Program ending')

if __name__ == '__main__':
    main()
