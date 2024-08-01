'''import csv 
file_name = input("Enter file name ")
with open(file_name,'r') as data:
    reader = csv.reader(file_name)
    for line in csv.DictReader(data):
        print(line)
  

user_input =input('Would you like to withdraw or exit? ')

while user_input== "exit" or "withdraw":
    if user_input=="exit": 
        print('Goodbye!')
        break
    elif user_input== "withdraw":
        pass
    else:
        print('Sorry, I don\'t know how to do that')
        user_input=input('Would you like to withdraw or exit?')
   


acc_num= input('Enter your account number or -1 to exit: ') 

while acc_num == '-1' or 

'''
import csv
account_data = {}


file_name = "atm_data.csv"

with open(file_name,'r') as file:
    
    for line in csv.reader(file):
        account_number = int(line[0])
        pin = line[1]
        name = line[2]
        balance = float(line[3])
        account_data[account_number] = [pin,name,balance]
print(account_data)
'''
with open(file_name,'w') as file: 
    writer = csv.writer(file)
    for key ,value in acount_data():
        writer.writerow([key],[value])

a = int(input('Enter your account number or -1 to exit: '))

while a != '-1' or account_data[account_number] : 
    if a==-1: 
        print('Ah, never mind.')
        print("-1")
        break    
    if a!= -1:
        if a in account_data:
            print(a)   
            break
        else: 
            print('Sorry, we don''t have an account matching that number.\nPlease try again.') 
            a = int(input('Enter your account number or -1 to exit: '))            
            
            


def ask_for_pin(account_data, account_number):
    enter_pin = int(input('Enter the PIN for your account. '))
    attempt =0 
    while attempt != 5: 
        if enter_pin != account_number[1]:
            print('Incorrect PIN')
            attempt += 1
            print(" Enter the PIN for the account")
            if attempt == 5: 
                print('Sorry, you\'ve exhausted your attempts')
                return False
            
        if enter_pin == account_number[pin]:
            print('Correct PIN')
            return True
ask_for_pin(account_data, account_number)

'''
 


        



