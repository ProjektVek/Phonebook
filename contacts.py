from replit import db #Allows to use replit db

#adding contact to db
def add_contact(name, phone_number):
    #print("[Debug] Entered add_contact")
    if name in db: #if finds this name in database
        print('Name Already Exists')
    else:
        db[name] = phone_number #inserts data into db
        #print("[Debug] Added on Database")

#getting contant number from db
def get_contact(name):
    number = db.get(name) #getting number from name from db
    return number

#search db by prefix
def search_contacts(search):
    match_keys = db.prefix(search)
    return {k: db[k] for k in match_keys} #return a dictionary

#function to update number
def update_number(old_name, new_number):
    db[old_name] = new_number

#function to update contact
def update_contact(old_name, new_name, new_number):
    db[new_name] = new_number
    del db[old_name]