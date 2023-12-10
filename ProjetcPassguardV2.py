#-------------------------------------------------------------------------------
# Name:        PassGuard
# Purpose:
#
# Author:      Joshua
#
# Created:     22/06/2023
# Copyright:   (c) Josh 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------

# Name:        PassGuard

# Purpose:

#

# Author:      Joshua

#

# Created:     22/06/2023

# Copyright:   (c) Josh 2023

# Licence:     <your licence>

#-------------------------------------------------------------------------------

import sys
import os
User_Data = []



# list where the user data will be stored

def menu():
    while True: #keep menu open
        choice = input("""
           1. Register
           2. Login
           3. Exit
           Please enter your choice:""")
        if choice == "1":
            return register()
        elif choice == "2":
            return login()
        elif choice == "3":
            sys.exit(" You have chosen to quit")
            quit()
        else:
            print("please select either 1, 2 or 3 ")
            print(" Please try again ")
        #menu() don't use a recursive call to keep the menu running, an infinite loop it better

def register():
    username = str(input(" Please create a username "))
    password = str(input( " please enter a password "))
    collect_data()
    f = open("tester1projectpass.txt",'r')
    info = f.read()
    if username in info:
        print( "Userame Unavailable. Please Try Again"  )
        #menu() don't open the menu or the file won't be written to
        f.close()
    else:
        f = open("tester1projectpass.txt",'w')
        info = info + username + "," + password
        for i in range(0,len(User_Data)):
            info = info +","+str(User_Data[i])#join the data from the list into the string to avoid have the [] in the text file
        f.write(info)
        f.write("\n")
        f.close()
#need to fix this function so that when username and password is entered it actually logs in


# ...

def login():
    print("Please enter your credentials:")
    username = str(input("Please enter your username: "))
    password = str(input("Please enter your password: "))
    f = open("tester1projectpass.txt", 'r')
    info = f.readlines()

    for i, row in enumerate(info):
        row = row.strip().split(",")
        if username in row:
            index = row.index(username) + 1
            usr_password = row[index]
            if usr_password == password:
                print("Welcome back, " + username)
                view_data = input("Do you want to see your user data? (yes/no): ")
                if view_data.lower() == "yes":
                    print("User Data:")
                    for i in range(0, len(User_Data), 5):
                        print("Forename:", User_Data[i])
                        print("Surname:", User_Data[i+1])
                        print("Age:", User_Data[i+2])
                        print("Height:", User_Data[i+3])
                        print("Sex:", User_Data[i+4])
                        print()
                change_password = input("Do you want to change your password? (yes/no): ")
                if change_password.lower() == "yes":
                    new_password = input("Enter your new password: ")
                    confirm_password = input("Confirm your new password: ")
                    if new_password == confirm_password:
                        row[index] = new_password
                        info[i] = ",".join(row) + "\n"
                        f = open("tester1projectpass.txt", 'w')
                        f.writelines(info)
                        f.close()
                        print("Password changed successfully!")
                    else:
                        print("Passwords do not match. Password change aborted.")
                break
            else:
                print("Incorrect password.")
    else:
        print("Name not found. Please sign up.")

# ...


def collect_data():
    # asks users for their data and  collects it
    name = input("What is your forename? ")
    Surename = input("what is your surename? ")
    Age = int(input(" What is your current age? "))
    Height = float(input( "What is your height in centemitres? (e.g 100.5 or 165.0 )"))
    Sex = input(" Are you Male or Female? ")
    # appends user data into the list
    User_Data.append(name)
    User_Data.append(Surename)
    User_Data.append(str(Age))
    User_Data.append(str(Height))
    User_Data.append(Sex)



#"tester1projectpass.txt" - test file name

menu()