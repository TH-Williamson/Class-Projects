majors = {}



def look_up(d):
    name = input('Enter a name:')
    if name in d:
       value = d.get(name)
       print(value)
    else:
        print('Not found.')


def add(d):
    name = input('Enter a name:')
    major = input('Enter a major:')
    d[name] = major
    

def change(d):
    name = input('Enter a name:')
    if name not in d:
        print('That name is not found')
    else:
        major = input('Enter the new major:')
        d[name] = major


def delete(d):
    name = input('Enter a name:')
    if name not in d:
        print('That name is not found')
    else:
        d.pop(name)


def display(d):
    for key, value in d.items():
        print(key, 'is a wizard in', value) 


def get_menu_choice():
    print('Majors of College students')
    print('---------------------------')
    print('1. Look up a student\'s major')
    print('2. Add a new student')
    print('3. Change a major')
    print('4. Delete a student')
    print('5. Display all students')
    print('6. Quit the program')
    choice = input('Enter your choice:')
    valid_choices = ['1', '2', '3', '4', '5', '6']
    while choice not in valid_choices:
        choice = input('Enter a valid choice:')
    return choice


## The main part of your program

choice = 0

while choice != '6':

        choice = get_menu_choice()

        if choice == '1':
            look_up(majors)
        elif choice == '2':
            add(majors)
        elif choice == '3':
            change(majors)
        elif choice == '4':
            delete(majors)
        elif choice == '5':
            display(majors)
    

