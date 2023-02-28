import psycopg2

def initApp():
    print("App Initializing...")

    conn.autocommit=True

    try:
        cursor.execute("create table if not exists phonebook(ContactID serial primary key,FirstName text,LastName text,PhoneNumber text,Email text)")
        cursor.execute("create table if not exists account(username text primary key,password text)")
    except:
        print("Database query create failed")


def closeapp():
    print("App Closing...")

    cursor.close()
    conn.close()



def viewonecontact():
    name=input("Enter first name of contact: ")
    try:
        cursor.execute("select FirstName,LastName,PhoneNumber,Email from phonebook where FirstName='%s'"%name)
        e=cursor.fetchone()
        print("\nFirstName: ",e[0],"\nLastName: ",e[1],"\nPhoneNumber: ",e[2],"\nEmail: ",e[3])
        print()
    except:
        print("Contact Not Found")


def viewallcontacts():
    try:
        cursor.execute("select FirstName,LastName,PhoneNumber,Email from phonebook")
        for e in cursor.fetchall():
            print("\nFirstName: ",e[0],"\nLastName: ",e[1],"\nPhoneNumber: ",e[2],"\nEmail: ",e[3])
            print()
    except:
        print("View all contacts failed")

def addcontact():
    user_first_name=input("Enter first name: ")
    user_last_name=input("Enter last name: ")
    user_phone_number=input("Enter phone number: ")
    user_email_id=input("Enter email id: ")
    try:
        cursor.execute("insert into phonebook(FirstName,LastName,PhoneNumber,Email) values(%s,%s,%s,%s)",(user_first_name,user_last_name,user_phone_number,user_email_id))
        print("Contact added successfully")
    except:
        print("Adding contact failed")

def deleteContact():
    name=input("Enter first name of contact to be delected: ")
    try:
        cursor.execute("delete from phonebook where FirstName='%s'"%name)
        print("Contact deleted successfully")
    except:
        print("Delete Contact Failed")

def deleteAllContact():
    try:
        cursor.execute("delete from phonebook")
        print("All Contacts deleted successfully")
    except:
        print("Delete Contacts Failed")

def updatecontact():
    firstname=input("Enter first name of contact to be updated: ")
    user_first_name=input("Enter new first name: ")
    user_last_name=input("Enter new last name: ")
    user_phone_number=input("Enter new phone number: ")
    user_email_id=input("Enter new email id: ")
    try:
        cursor.execute("update phonebook set FirstName=%s,LastName=%s,Email=%s,PhoneNumber=%s where FirstName=%s",(user_first_name,user_last_name,user_phone_number,user_email_id,firstname))
    except:
        print("Update Contact Failed")

def show_menu():
    print("What do you want to do?")
    print("[view -a]            to view all saved contacts")
    print("[view]               to view a specific contact")
    print("[add]                to add a new contact")
    print("[del]                to delete a contact")
    print("[del -a]             to delete all contact")
    print("[update]             to update an existing contact")
    print("[exit]               to exit the program")

def parse_selection():
    while True:
        show_menu()
        selection=input()
        match selection:
            case 'view -a':
                viewallcontacts()
            case 'view':
                viewonecontact()
            case 'add':
                addcontact()
            case 'del':
                deleteContact()
            case 'del -a':
                deleteAllContact()
            case 'update':
                updatecontact()
            case 'exit':
                closeapp()
                break
        input("Press Enter to Continue...")

def register():
    print("Enter Registration details: ")
    user_name=input("Enter user name: ")
    password=input("Enter password: ")
    try:
        cursor.execute("insert into account(username,password) values(%s,%s)",(user_name,password))
        print("User added successfully")
    except:
        print("Adding user failed")
        return False
    return True

def login():
    user_name=input("Enter user name: ")
    password=input("Enter password: ")
    try:
        cursor.execute("select username from account where username=%s and password=%s",(user_name,password))
        if user_name==cursor.fetchone()[0]:
            print("Login successful")
        else:
            print("User not found")
            return False
    except:
        print("Login failed")
        return False
    return True



print("\n")
print("==============================")
print("DIGITAL PHONE BOOK APPLICATION")
print("==============================")
print("\n")

try:
    conn=psycopg2.connect(dbname="postgres",
                        host="127.0.0.1",
                        user="postgres",
                        password="amar2181",
                        port="5432")
    cursor=conn.cursor()
except:
    print("Database connection failed")

initApp()

print("Are you a registred user? (yes/no)")
user_yes_no=input()
if user_yes_no.lower()=='yes':
    parse_selection() if True==login() else print("Invalid login")
elif user_yes_no.lower()=='no':
    if True==register():
        print("Now login to your account")
        if True==login():
            parse_selection()
        else:
            print("Invalid login")
    else:
        print("Registration failed")
else:
    print("Enter valid input")



