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

#function to get contact
def prompt_get_contact():
    name = input("Please enter the name to find: ")
    number = contacts.get_contact(name)
    if number:
        print(f"{name}'s number is {number}")
    else:
        print(f"{name}'s number not found")

#Creating Menu
main_message = 'Welcome to Phonebook\n'
main_message += '-----------------------------\n'
main_message += 'Please choose:\n'
main_message += '1 - Add a new Contact\n'
main_message += '2 - Find a Contact\n'
main_message += '-----------------------------\n'

#Defining main function
def main():
    print(main_message)
    choice = input("Please make your choice: ").strip() #strip() removes any spaces at the start or end of string
    if choice == '1':
        prompt_add_contact()
    elif choice == '2':
        prompt_get_contact()
    else:
        print("Invalid input. Please try again.")

#Execution The Program
while True:
    system("clear")
    main()
    input("Press enter to continue:")


#Executing code
prompt_add_contact()