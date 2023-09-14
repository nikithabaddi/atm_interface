import time as t


user_pin = 1234
user_balance = 97432.50
user_name = "nikitha"
print("Welcome to your bank account", user_name, end = "\n\n")

choice = 9

while (True):
    print("\t\t1. transaction history")
    print("\t\t2. withdraw")
    print("\t\t3. deposit")
    print("\t\t4. transfer")
    print("\t\t5. exit")
    choice = int(input("Enter your option > "))
    print("\n\n")

    if choice == 5:
        print("exiting..")
        t.sleep(2)
        print("You have been logged out. Thank you!\n\n")
        break

    elif choice in (1,2,3,4,):
        num_of_tries = 3
        while (num_of_tries!=0):
            input_pin = int(input("Please enter your 4-digit PIN > "))

            if input_pin == user_pin:
                print("Account auhtorized!\n\n")

                if choice == 1:
                    print("balance after transaction is...")
                    t.sleep(1.5)
                    print("Your current balance is Rs.", user_balance, end = "\n\n\n")
                    break
                elif choice == 2:
                    print("Opening Cash Withdrawal...")
                    t.sleep(1.5)

                    while(True):
                        withdraw_amt = float(input("Enter the amount you wish to withdraw > "))

                        if withdraw_amt>user_balance:
                            print("Can't withdraw Rs.", withdraw_amt)
                            print("Please enter a lower amount!")
                            continue

                        else:
                            print("Withdrawing Rs.", withdraw_amt)
                            confirm = input("Confirm? Y/N > ")
                            if confirm in ('Y', 'y'):
                                user_balance-=withdraw_amt
                                print("Amount withdrawn - Rs.", withdraw_amt)
                                print("Remaining balance - Rs.", user_balance, end = "\n\n\n")
                                break

                            else:
                                print("Cancelling transaction...")
                                t.sleep(1)
                                print("Transaction Cancelled!\n\n")
                                break

                    break

                elif choice == 3:
                    print("Loading Cash Deposit...")
                    t.sleep(1.5)

                    deposit_amt = float(input("Enter the amount you wish to deposit > "))
                    print("Depositing Rs.", deposit_amt)
                    confirm = input("Confirm? Y/N > ")
                    if confirm in ('Y', 'y'):
                        user_balance+=deposit_amt
                        print("Amount deposited - Rs.", deposit_amt)
                        print("Updated balance - Rs.", user_balance, end = "\n\n\n")
                    else:
                        print("Cancelling transaction...")
                        t.sleep(1)
                        print("Transaction Cancelled!\n\n")

                    break


                elif choice == 4:
                    print("Transfer cash..")
                    t.sleep(1.5)
                    trans_from = float(input("account transfer from\n 1.nikitha "))
                    transfer_amt = float(input("amount you want to transfer?:"))
                    transfer_to = float(input("To which account you want to transfer\n 1.pavan 2.sona 3.megha"))
                    confirm = input("Confirm? Y/N >")
                    if confirm in ('Y', 'y'):
                        if(trans_from == 1):
                            if(transfer_amt > user_balance):
                                print("insufficient balance")
                            else:
                                user_balance = user_balance - transfer_amt
                                if transfer_to == 1:
                                    user_balance = user_balance - transfer_amt
                                    print("you have transfered amount from nikitha account to pavan. balance of "
                                          "nikitha's account is "+str(user_balance)+". Thankyou " )
                                elif transfer_to == 2:
                                    user_balance = user_balance - transfer_amt
                                    print("you have transferred amount from nikitha account to sona. balance of "
                                          "nikitha's account is "+str(user_balance)+".thankypu")
                                elif transfer_to == 3:
                                    user_balance = user_balance - transfer_amt
                                    print("you have transferred amount from nikitha account to sona. balance of "
                                          "nikitha's account is " + str(user_balance) + ".thankypu")
                                else:
                                    print("please check account ")
                    else:
                        print("Cancelling transfer...")
                        t.sleep(1)
                        print("Transaction cancelled!", end="\n\n\n")

                    break


            else:
                num_of_tries-=1
                print("PIN incorrect! Number of tries left -", num_of_tries, end = "\n\n")

        else:
            print("Exiting...")
            t.sleep(2)
            print("You have been logged out. Thank you!\n\n")
            break


    else:
        print("Invalid input!")
        print("\t\t0. Enter 0 to Logout and Exit!")
        continue