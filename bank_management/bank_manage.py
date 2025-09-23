import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'      # path of data.json file
    data = []
    
    def __init__(self):
        try:
            if Path(Bank.database).exists():
                with open(Bank.database) as fs:
                    Bank.data = json.load(fs)
            else:
                print("no such file exists")
        except Exception as err:
            print(f"an exception occured {err}")


    @classmethod
    def __update(cls):
        with open(cls.database,"w") as fs:
            json.dump(Bank.data,fs)


    @classmethod
    def __accGen(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=3)
        special = random.choices("@#$%^&*")

        id = alpha+num+special
        random.shuffle(id)             # returns an object
        
        return "".join(id)             # converted to string


    def createaccount(self):
        info = {"name":input("\nEnter full name-"),
                "age":int(input("Enter your age- ")),
                "email":input("Enter email id- "),
                "pin":input("Create a 4 digit pin for your account- "),
                "accountNo.":Bank.__accGen(),
                "balance":0}


        if info['age'] < 18 or len(info['pin']) != 4:
            print("\nInvalid details! Sorry you cannot create an account")
        else:
            print("\nYour account has been created. Please note your Account No.")

            for i in info:
                print(f"{i}:{info[i]}")

            
            Bank.data.append(info)
            Bank.__update()                     # update data in json file


    
    def depositmoney(self):
        # print("Current Bank data:", Bank.data)
        accnum = input("Enter your account number- ")
        accpin = input("Enter your account pin- ")

        # stop at first match
        userdata = next((i for i in Bank.data if i["accountNo."] == accnum and i["pin"] == accpin), None)

        if userdata is None:
            print("Sorry, no data found!")
            return

        amount = int(input("Enter amount to deposit- "))

        if amount <= 0:
            print("Invalid amount")
        elif amount > 50000:
            print("Amount limit exceeded. Deposit up to 50,000 only")
        else:
            userdata['balance'] += amount

            Bank.__update()
            print("\nAmount deposited successfully")


    
    def withdrawmoney(self):
        accnum = input("Enter your account number- ")
        accpin = input("Enter your account pin- ")

        # stop at first match
        userdata = next((i for i in Bank.data if i["accountNo."] == accnum and i["pin"] == accpin),None)

        
        if userdata is None:
            print("sorry no data found!")
            return
        
        amount = int(input("Enter amount to withdraw- "))

        if amount <= 0:
            print("Enter amount greater than 0")
        elif userdata["balance"] < amount:
            print("Out of balance!")
        else:
            userdata["balance"] -= amount

            Bank.__update()
            print("\nAmount withdrew successfully")



    def showdetails(self):
        accnum = input("Enter your account number- ")
        accpin = input("Enter your account pin- ")

        # stop at first match
        userdata = next((i for i in Bank.data if i["accountNo."] == accnum and i["pin"] == accpin),None)
        
        print("\nYour details,")
        for i in userdata:
            print(f"{i}:{userdata[i]}")



    def updateDetails(self):
        accnum = input("Enter your account number- ")
        accpin = input("Enter your account pin- ")

        # stop at first match
        userdata = next((i for i in Bank.data if i["accountNo."] == accnum and i["pin"] == accpin),None)

        if userdata is None:
            print("sorry no data found!")
            return

        print("\nDetails like age, accountNo and balance cannot be changed")
        print("If no change press enter to skip")


        newdata = {"name":input("Enter new name- "),
                   "email":input("Enter your new email- "),
                   "pin":input("Enter your new pin- ")}

        if newdata["name"] == "":
            newdata["name"] = userdata["name"]
        elif newdata["email"] == "":
            newdata["email"] = userdata["email"]
        elif newdata["pin"] == "":
            newdata["pin"] = userdata["pin"]

        newdata["age"] = userdata["age"]
        newdata["accountNo."] = userdata["accountNo."]
        newdata["balance"] = userdata["balance"]

        for i in newdata:
            if newdata[i] == userdata[i]:
                continue
            else:
                userdata[i] = newdata[i]

        Bank.__update()
        print("\nDetails updated successfully")



    def delete(self):
        accnum = input("Enter your account number- ")
        accpin = input("Enter your account pin- ")

        # stop at first match
        userdata = next((i for i in Bank.data if i["accountNo."] == accnum and i["pin"] == accpin),None)

        if userdata is None:
            print("sorry no data found!")
            return
        
        check = input("\nEnter 'y' if you are sure to delete account else enter 'n': ").lower()

        if check == "n":
            pass
        elif check == "y":
            index = Bank.data.index(userdata)

            Bank.data.pop(index)
            print("\nAccount deleted successfully")
        else:
            print("Invalid entry")

        Bank.__update()


user = Bank()


while True:
    print("\n1: Create account\n2: Deposit money\n3: Withdraw money\n4: Details\n5: Update details\n6: Delete account\n7: Exit")

    choice = int(input("\nEnter your choice- "))

    if choice == 1:
        user.createaccount()
    elif choice == 2:
        user.depositmoney()
    elif choice == 3:
        user.withdrawmoney()
    elif choice == 4:
        user.showdetails()
    elif choice == 5:
        user.updateDetails()
    elif choice == 6:
        user.delete()
    elif choice == 7:
        print("\nExiting program...")
        break
    else:
        print("Invaild choice")
        