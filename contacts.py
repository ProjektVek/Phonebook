from replit import db #Allows to use replit db

def add_contact(name, phone_number):
    if name in db: #if finds this name in database
        print('Name Already Exists')
    else:
        db[name] = phone_number #inserts data into db