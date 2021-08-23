money = 1000
choice = 0
i = 0
while i != 3:
    login = str(input("Login: "))
    password = str(input("password: "))
    registeredlogin = "joao"
    registeredpassword = "abc123"
    if login == registeredlogin and password == registeredpassword:
        break
    else:
        i = i + 1
        if i == 3:
            print("Too many invalid attempts, leaving...")
            choice = 4

while choice != 4:
    print("-------------------------")
    print("| 1----------- Withdraw |")
    print("| 2------------- Balance|")
    print("| 3------------- Deposit|")
    print("| 4-------------- Logout|")
    print("-------------------------")

    choice = int(input("Choose an option: "))
    if choice == 1:
        print("Withdraw")
        amountWithdrawn = float(input("How many do you want to withdraw?\n"))
        if amountWithdrawn <= money:
            print("Authorized withdrawal!")
            money = money - amountWithdrawn
            print("Withdrawal amount R$ %.2f" % amountWithdrawn)
        else:
            print("Insufficient funds :(")

    elif choice == 2:
        print("Balance")
        print("Balance: R$ %0.2f" % money)

    elif choice == 3:
        print("Deposit")
        print("-----------------------------------------")
        print("| 1-------------- Deposit to your account|")
        print("| 2---- Deposit to another user's account|")
        print("-----------------------------------------")
        deposit = int(input(""))
        if deposit == 1:
            amountDeposited = float(input("Enter balance amount: "))
            if amountDeposited >= 10:
                money = money + amountDeposited
                print("You have deposited R$ {} into your account.".format(
                    amountDeposited))
            else:
                print("Deposit valid only for amounts greater than or equal to 10.")
        elif deposit == 2:
            amountDeposited = float(input("Enter deposit amount: "))
            if amountDeposited >= 10:
                money = money - amountDeposited
                print("You deposited R$ {} in the account XXXXXX XXXXX XXXX.".format(
                    amountDeposited))
            else:
                print("Deposit valid only for amounts greater than or equal to 10.")

    elif choice == 4:
        print("Closing session...")
