import random
print("\n\t", '\\'*55, "\n\t\tWelcome you to our random password generator\n\n\t\t","**"*4, "Coded by TechLead Co. LTD", "**"*4,"\n\t",'\\'*55, "\n" )

pwdlenth = int(input("Enter the length of password: "))
lib="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
pwd =  "".join(random.sample(lib, pwdlenth ))
print ("Your password is: ", pwd)
input("\n\tPress enter key to exit the program...\a",)
