def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          ")
name = input("Enter name to register: ")
pin = input("Enter PIN: ")
balance = str(0)
print(name, "has been registered with a starting balance of $", balance)

print("          === Automated Teller Machine ===          ")
print("LOGIN")
name_to_validate = input("Enter name:")
pin_to_validate = input("Enter pin:")

