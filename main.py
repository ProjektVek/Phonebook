from replit import db #Importing replit database - In replit workspace, you dont need to login
import contacts #Importing contacts archive

#Storing and retrieving data from database
db["Harris, Steve"] = "12345666" #Defining the key value in the database
print(db["Harris, Steve"]) #Retrieving key value in the database

#Comparing with python dictionary
dictionary = {} #defining dictionary
dictionary["Harris, Steve"] = "12345666"
print(dictionary["Harris, Steve"])

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

#Executing code
prompt_add_contact()