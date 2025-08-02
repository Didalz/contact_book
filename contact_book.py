# Contacts

#initialize
contacts = {}

#Menu
def show_menu():
    print('-----CONTACT BOOK-----')
    print('1. Add contact\n2. View contact\n3. Search contact\n4. Edit contact\n5. Delete contact\n6. exit')

# add contact
def add_contact():
    name = input('Enter new contact name: ')
    phone = input('Enther phone of new contact: ')
    email = input('Enter the email: ')
    contacts[name] = {'phone' : phone, 'email': email}
    print(f'{name} has been added to you contact book')

#view contact
def view_contact():
    if contacts:
        print('------Contact List------')
        for name, details in contacts.items():
            print(f'name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}')
    else:
        print('your contact book is empty.')


#Search contact
def search_contact():
    name = input('Enter the name of the contact: ')
    if name in contacts: 
        print(f'------Contact Details----\nName: {name}\nPhone: {contacts[name]['phone']}\nEmail: {contacts[name]['email']}')
    else: print(f'Contac {name} not found')

#edit contact

def edit_contact():
    name = input('Enter the name of the contact to edit: ')
    if name in contacts: 
        print(f'-------Editing {name}------\n1. Edit phone\n2. Edit Email')
        option = input()
        if option == 1:
            phone = input('Enter the new phone: ')
            contacts[name] = {'phone' : phone}
            print(f'Contact phone has beed changed succesfully to {phone}')
        elif option == 2:
            email = input('Enter the new email: ')
            contacts[name] = {'email' : email}
            print(f'Your email has been changeed succesfully to {email}')
        else:
            print('You choose an incorrect option')
    else: print(f'Contac {name} not found')

#delete contact

def delete_contact():
    name = input('Enter the name of the contact to delete: ')
    if name in contacts: 
        print(f'Are you sure want do delete {name}?\n1. Yes\n2. No')
        option = input
        if option == 1:
            del contacts[name]
            print(f'{name} has bees succesfully deleted')
        elif option == 2:
            None
        else: print('You didnt choose a correct option')
    else: print(f'Contac {name} not found')

#program menu

while True:
    show_menu()
    choice = int(input('Enter the option: '))
    if choice == 1: add_contact()
    elif choice == 2: view_contact()
    elif choice == 3: search_contact()
    elif choice == 4: edit_contact()
    elif choice == 5: delete_contact()
    elif choice == 6:
        print('exiting')
        break
    else: print('Invalid choice')
    