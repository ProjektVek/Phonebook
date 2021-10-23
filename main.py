from replit import db #Importing replit database - In replit workspace, you dont need to login
import contacts #Importing contacts archive
from os import system #importing function to help create the menu

"""
#Storing and retrieving data from database
db["Harris, Steve"] = "12345666" #Defining the key value in the database
print(db["Harris, Steve"]) #Retrieving key value in the database

#Comparing with python dictionary
dictionary = {} #defining dictionary
dictionary["Harris, Steve"] = "12345666"
print(dictionary["Harris, Steve"])
"""

#function to get contact input
def prompt_add_contact():
    name = input("Please enter the contact's name: ") #getting name
    number = input("Please enter the contact's number: ") #getting number
    print(f"Adding {name} with {number}") #printing the input (python's f-string)
    contacts.add_contact(name,number)
"""
#function to get contact
def prompt_get_contact():
    name = input("Please enter the name to find: ")
    number = contacts.get_contact(name)
    if number != '':
        print(f"{name}'s number is {number}")
    else:
        print(f"{name}'s number not found")
"""

#function to search a contact
def prompt_get_contact():
    name = input("Please enter the name to find: ")
    number = contacts.get_contact(name)
    if number: # if there is a number
        print(f"{name}'s number is {number}")
    else:
        matches = contacts.search_contacts(name) #get all matches
        if matches: # if there is a match
            for k in matches: #get values of match in k
                print(f"{k}'s number is {matches[k]}")
        else:
            print(f'It looks like {name} does not exist')

#function to update a contact
def prompt_update_contact():
    old_name = input("Please enter the name of the contact to update: ")
    old_number = contacts.get_contact(old_name)
    if old_number: #if the number isn't empty
        new_name = input(f'Please enter the new name for this contact (leave blank to keep {old_name}):').strip()
        new_number = input(f'Please enter the new number for this contact (leave blank to keep {old_number}):').strip()

        if not new_number:
            new_number = old_number

        if not new_name:
            contacts.update_number(old_number, new_number)
        else:
            contacts.update_contact(old_name, new_name, new_number)
    else:
        print(f'It looks like {old_name} does not exist')

#Creating Menu
main_message = 'Welcome to Phonebook\n'
main_message += '-----------------------------\n'
main_message += 'Please choose:\n'
main_message += '1 - Add a new Contact\n'
main_message += '2 - Find a Contact\n'
main_message += '3 - Find a Contact\n'
main_message += '-----------------------------\n'

#Defining main function
def main():
    print(main_message)
    choice = input("Please make your choice: ").strip() #strip() removes any spaces at the start or end of string
    if choice == '1':
        prompt_add_contact()
    elif choice == '2':
        prompt_get_contact()
    elif choice == '3':
        prompt_update_contact()
    else:
        print("Invalid input. Please try again.")

#Execution The Program
while True:
    system("clear")
    main()
    input("Press enter to continue:")


#Executing code
prompt_add_contact()