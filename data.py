data={}
with open("atm_data.csv",'w') as file: 
    writer = csv.writer(file)
    for key ,value in acount_data():
        writer.writerow([key],[value])
 
with open(file_name,'w') as f: 
    for account_number, account_data in data.items(): 
        f.write(f'{account_number}, {account_data[pin]},{account_data[name], account_data[balace]}')
