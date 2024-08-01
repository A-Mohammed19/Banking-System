import csv

# The fee that is charged the user's account with every transaction. If the fee
# would cause the user to go into a negative balance, their transaction must be
# prevented just like if they had requested too large of a withdraw.
ATM_FEE = 0.50


def read_atm_data(file_name):
    """
    This function reads the file named by the parameter `file_name` builds a
    dictionary of account data from the file. The file should be CSV format
    with the account number as the 1st column, the account pin as the second
    column, the account holder's name as the third column, and the account
    balance as the fourth column. The resulting dictionary should have the
    account number (converted to an int) as the key and a list of the other 3
    cells as the value. The dictionary is returned at the end of the function.
    """
    account_data = {}
    with open(file_name,'r') as file:
        
        for line in csv.reader(file):
            account_number = int(line[0])
            pin = line[1]
            name = line[2]
            balance = float(line[3])
            account_data[account_number] = [pin,name,balance]
    return account_data


def write_atm_data(file_name, data):
    """
    This function write the data in dictionary `data` to the file named in the
    parameter `file_name`. The dictionary passed into this function is the same
    as returned by `read_atm_data` and the file format it writes should be the
    same as the one `read_atm_data` read.
    data ={}
    """        
    with open(file_name,'w', newline='') as file: 
        writer = csv.writer(file)
        for key ,value in data.items():
            pin = value[0]
            name = value[1]
            balance = value[2]
            row = [key, pin, name, balance]
            writer.writerow(row)
    '''
    data1= dict()
    data1= data.copy()
    with open(file_name,'a') as f:
        for key in data.keys():
            f.write("%s, %s\n" % (key, data1[key]))      
    return data 
    '''

def ask_for_action():
    """
    Prompts the user with 'Would you like to withdraw or exit?' and receives
    keyboard input from them. If they enter either 'exit' or 'withdraw', then
    that value is returned. Otherwise, they are told 'Sorry, I don't know how
    to do that.' and are given the text prompt again. (You probably want a
    while loop here.)
    """
    user_input =input('Would you like to withdraw or exit? ')
    
    while user_input == 'withdraw' or 'exit':
        if user_input== 'withdraw':
            return(user_input)
        elif user_input =="exit": 
            return(user_input)
             
        else:
            print('Sorry, I don\'t know how to do that')
            user_input=input('Would you like to withdraw or exit?')


def ask_for_account_number(account_data):
    """
    Prompts the user with 'Enter your account number or -1 to exit: ' and
    receives keyboard input from them. The input value should be converted to
    an integer. If they entered -1, this function print 'Ah, never mind.' and
    then should return -1. If they entered any other value, the function should
    check if it is a valid account number using the `account_data` parameter.
    If it is a valid, account number, that number should be returned.
    Otherwise, the user is told 'Sorry, we don't have an account matching that
    number.\nPlease try again.' and the prompt is displayed again. (This
    function also needs a while loop.)
    """
    
    a = int(input('Enter your account number or -1 to exit: '))
    
    while a != '-1': 
        if a==-1: 
            print('Ah, never mind.')
            return(-1)
        elif a!= -1:
            if a in account_data:
                return(a)
            else: 
                print('Sorry, we don''t have an account matching that number.\nPlease try again.') 
                a = int(input('Enter your account number or -1 to exit: '))          
            
        


def ask_for_pin(account_data, account_number):
    """
    This function asks the user to enter the PIN that matches `account_number`
    and gives them 5 attempts to do so. It prompts the user with 'Attempt
    {attempt}/5 Enter the PIN for the account: ' each time, where {attempt} is
    the current attempt number. If they enter the correct PIN, the function
    prints 'Correct PIN' and returns True. When an incorrect PIN is entered,
    the function prints 'Incorrect PIN' and displays the prompt again for the
    user. After 5 failed attempts, the functions should print 'Sorry, you've
    exhausted your attempts.' and return False.
    """
    
   # acc= list(account_data.values()) 
    #print(acc)

    enter_pin = input('Enter the PIN for your account. ')
    attempts = 0 
    while attempts <= 5: 
        if enter_pin != account_data[account_number][0] :
            print('Incorrect PIN')
            attempts += 1
            print(f"Attempts {attempts}/5")
            enter_pin = input('Enter the PIN for your account. ')
            if attempts == 5: 
                print('Sorry, you\'ve exhausted your attempts')
                return False 
        if enter_pin == account_data[account_number][0]:
            print('Correct PIN')
            return True
    
    


def withdraw(account_data, account_number):
    """
    This function greets the user with their name, and then tells them their
    balance and offers to let them make a withdraw. The user then enters an
    amount to withdraw. If they enter a negative number, the function exits
    without changing their balance. If they enter a number that make their
    balance negative AFTER the ATM fee is applied, then they are told they
    don't have enough in their account and are allowed to enter a new amount.
    Finally, if they do enter an amount that they can withdraw, their balance
    is decreased and they are told their new balance. The function then exits.
    """
    name = account_data[account_number][1]
    balance = account_data[account_number][2]
    global ATM_FEE
    
    print(f"Hello{name},your current balance is {balance}.")
    
    amount_withdraw = float (input("How much money would you like to withdraw from your account today? "))
    
    if amount_withdraw + ATM_FEE > balance: 
        print("Incificent Funds.")
    else: 
        balance -= amount_withdraw + ATM_FEE
        print(f"You have completed your transcation. Your new balance is {balance}.")
        account_data[account_number][2] = balance
    
                           


def main():
    account_data = read_atm_data("atm_data.csv")

    action = ''
    while action != 'exit':
        action = ask_for_action()
        if action == 'withdraw':
            account_number = ask_for_account_number(account_data)
            if account_number == -1:
                continue

            if ask_for_pin(account_data, account_number):
                withdraw(account_data, account_number)

    print("Goodbye!")
    write_atm_data("atm_data.csv", account_data)


main()


import csv

# The fee that is charged the user's account with every transaction. If the fee
# would cause the user to go into a negative balance, their transaction must be
# prevented just like if they had requested too large of a withdraw.
ATM_FEE = 0.50


def read_atm_data(file_name):
    """
    This function reads the file named by the parameter `file_name` builds a
    dictionary of account data from the file. The file should be CSV format
    with the account number as the 1st column, the account pin as the second
    column, the account holder's name as the third column, and the account
    balance as the fourth column. The resulting dictionary should have the
    account number (converted to an int) as the key and a list of the other 3
    cells as the value. The dictionary is returned at the end of the function.
    """
    account_data = {}
    with open(file_name,'r') as file:
        
        for line in csv.reader(file):
            account_number = int(line[0])
            pin = line[1]
            name = line[2]
            balance = float(line[3])
            account_data[account_number] = [pin,name,balance]
    return account_data


def write_atm_data(file_name, data):
    """
    This function write the data in dictionary `data` to the file named in the
    parameter `file_name`. The dictionary passed into this function is the same
    as returned by `read_atm_data` and the file format it writes should be the
    same as the one `read_atm_data` read.
    data ={}
    """        
    with open(file_name,'w', newline='') as file: 
        writer = csv.writer(file)
        for key ,value in data.items():
            pin = value[0]
            name = value[1]
            balance = value[2]
            row = [key, pin, name, balance]
            writer.writerow(row)
    '''
    data1= dict()
    data1= data.copy()
    with open(file_name,'a') as f:
        for key in data.keys():
            f.write("%s, %s\n" % (key, data1[key]))      
    return data 
    '''

def ask_for_action():
    """
    Prompts the user with 'Would you like to withdraw or exit?' and receives
    keyboard input from them. If they enter either 'exit' or 'withdraw', then
    that value is returned. Otherwise, they are told 'Sorry, I don't know how
    to do that.' and are given the text prompt again. (You probably want a
    while loop here.)
    """
    user_input =input('Would you like to withdraw or exit? ')
    
    while user_input == 'withdraw' or 'exit':
        if user_input== 'withdraw':
            return(user_input)
        elif user_input =="exit": 
            return(user_input)
             
        else:
            print('Sorry, I don\'t know how to do that')
            user_input=input('Would you like to withdraw or exit?')


def ask_for_account_number(account_data):
    """
    Prompts the user with 'Enter your account number or -1 to exit: ' and
    receives keyboard input from them. The input value should be converted to
    an integer. If they entered -1, this function print 'Ah, never mind.' and
    then should return -1. If they entered any other value, the function should
    check if it is a valid account number using the `account_data` parameter.
    If it is a valid, account number, that number should be returned.
    Otherwise, the user is told 'Sorry, we don't have an account matching that
    number.\nPlease try again.' and the prompt is displayed again. (This
    function also needs a while loop.)
    """
    
    a = int(input('Enter your account number or -1 to exit: '))
    
    while a != '-1': 
        if a==-1: 
            print('Ah, never mind.')
            return(-1)
        elif a!= -1:
            if a in account_data:
                return(a)
            else: 
                print('Sorry, we don''t have an account matching that number.\nPlease try again.') 
                a = int(input('Enter your account number or -1 to exit: '))          
            
        


def ask_for_pin(account_data, account_number):
    """
    This function asks the user to enter the PIN that matches `account_number`
    and gives them 5 attempts to do so. It prompts the user with 'Attempt
    {attempt}/5 Enter the PIN for the account: ' each time, where {attempt} is
    the current attempt number. If they enter the correct PIN, the function
    prints 'Correct PIN' and returns True. When an incorrect PIN is entered,
    the function prints 'Incorrect PIN' and displays the prompt again for the
    user. After 5 failed attempts, the functions should print 'Sorry, you've
    exhausted your attempts.' and return False.
    """
    
   # acc= list(account_data.values()) 
    #print(acc)

    enter_pin = input('Enter the PIN for your account. ')
    attempts = 0 
    while attempts <= 5: 
        if enter_pin != account_data[account_number][0] :
            print('Incorrect PIN')
            attempts += 1
            print(f"Attempts {attempts}/5")
            enter_pin = input('Enter the PIN for your account. ')
            if attempts == 5: 
                print('Sorry, you\'ve exhausted your attempts')
                return False 
        if enter_pin == account_data[account_number][0]:
            print('Correct PIN')
            return True
    
    


def withdraw(account_data, account_number):
    """
    This function greets the user with their name, and then tells them their
    balance and offers to let them make a withdraw. The user then enters an
    amount to withdraw. If they enter a negative number, the function exits
    without changing their balance. If they enter a number that make their
    balance negative AFTER the ATM fee is applied, then they are told they
    don't have enough in their account and are allowed to enter a new amount.
    Finally, if they do enter an amount that they can withdraw, their balance
    is decreased and they are told their new balance. The function then exits.
    """
    name = account_data[account_number][1]
    balance = account_data[account_number][2]
    global ATM_FEE
    
    print(f"Hello{name},your current balance is {balance}.")
    
    amount_withdraw = float (input("How much money would you like to withdraw from your account today? "))
    
    if amount_withdraw + ATM_FEE > balance: 
        print("Incificent Funds.")
    else: 
        balance -= amount_withdraw + ATM_FEE
        print(f"You have completed your transcation. Your new balance is {balance}.")
        account_data[account_number][2] = balance
    
                           


def main():
    account_data = read_atm_data("atm_data.csv")

    action = ''
    while action != 'exit':
        action = ask_for_action()
        if action == 'withdraw':
            account_number = ask_for_account_number(account_data)
            if account_number == -1:
                continue

            if ask_for_pin(account_data, account_number):
                withdraw(account_data, account_number)

    print("Goodbye!")
    write_atm_data("atm_data.csv", account_data)


main()





