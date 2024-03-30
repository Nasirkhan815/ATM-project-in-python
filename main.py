print('~~~~~~~~! Welcome to ATM !~~~~~~~~')
balance = 1000  # Available balance in account
pin = '1234'  # ATM pin
entered_pin = input('please Enter Your Pin: ')
if entered_pin != pin:
    print('Sorry you Enter Wrong PIN')
    ATM_ON = False

else:
    ATM_ON = True
# Menus
while ATM_ON:
    print('__________________________________________________________________')
    print('                         Main Menu')
    print('__________________________________________________________________')

    print('1. Check Balance')
    print('2. Deposit Money')
    print('3. Withdrawal Money')
    print('4. Exit')
    print('__________________________________________________________________')

    choice = input("Please Select one option: ")
    # menu Selection

    if choice == '1':
        print('Your Balance is: $ ' + str(balance))

    elif choice == '2':
        amount = float(input('Enter the Amount you want to Deposit: $ '))
        balance += amount
        print('Your Money is Deposed Your New Balance is: $ ' + str(balance))

    elif choice == "3":
        amount = float(input('Enter the Amount you Want to Withdrawal:$ '))
        if amount > balance:
            print('Your Entered Money is Less than your Balance')

        else:
            balance -= amount
        print('Your Withdrawal is Successfully done Your New Balance is: $ ' + str(balance))

    elif choice == '4':
        print('THANKS FOR USING ATM')
        print('Goodbye')
        ATM_ON = False

    else:
        print('You Entered invalid Option Please Try Again')



