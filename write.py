import csv
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
            account_data[account_numeber] = [pin,name,balance]
        return account_data

def write_atm_data(file_name, data):
    """
    This function write the data in dictionary `data` to the file named in the
    parameter `file_name`. The dictionary passed into this function is the same
    as returned by `read_atm_data` and the file format it writes should be the
    same as the one `read_atm_data` read
    
    data1= dict()
    data1= data.copy()
    with open(file_name,'a') as f:
        for key in data.keys():
            f.write("%s, %s\n" % (key, data1[key]))  
     """
getaways = {'Switzerland': 'Windmill', 'Canada': 'Igloo',  'Sweden': 'Treehouse', 'US': 'Lighthouse'}

first_val = list(getaways.values())[0]

print(first_val)
    
        
        
            


write_atm_data("atm_data.csv", {123456: ['1234', 'No One', -1]})