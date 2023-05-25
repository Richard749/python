name = input("What is your name:")
password = input("Insert Password:")
retype_password = input("retype Password:")

if password == retype_password:
    print(" password correct")
else:
    while password != retype_password:
        print("retry password")
        password = input("Insert Password:")
        confirm_password = input("confirm Password:")

    if password == retype_password:
        print("password correct")