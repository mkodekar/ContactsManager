"""
CONTACT MANAGER
@VERSION 2
@author Rehan Kodekar
@DATE 2017-04-21

"""


def main():
    friends = []
    for i in range(2):
        print("Contacts manager")
        name = input("Enter name : ")
        phone = input("Enter phone number : ")
        email = input("Enter email address : ")
        friends.append([name, phone, email])

    for i in range(len(friends)):
        print('Contacts info')
        for j in range(len(friends[i])):
            print(friends[i][j])


if __name__ == '__main__':
    main()
