import logic as lg

if lg.login():
    print("Welcome to ATM")

    while True:
        lg.menu()   
        ch = input("Enter your choice: ").upper()
        if ch=='D':
            lg.deposit()
        elif ch=='W':
            lg.withdraw()
        elif ch=='C':
            lg.checkBalance()
        elif ch=='V':
            lg.viewTrasactions()
        elif ch=='E':
            print("Thankyou")
            break
        else:
            print("Invalid Input")
    
