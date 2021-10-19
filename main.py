from replit import db #Importing replit database - In replit workspace, you dont need to login

#Storing and retrieving data from database
db["Harris, Steve"] = "12345666" #Defining the key value in the database
print(db["Harris, Steve"]) #Retrieving key value in the database

#Comparing with python dictionary
dictionary = {} #defining dictionary
d["Harris, Steve"] = "12345666"
print(d["Harris, Steve"])