
import sqlite3

def login_verify(userID,aadhar,password):
    conn = sqlite3.connect('ElectricityBillingSystem.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute('SELECT userID,Password,aadhar_number FROM Customer')
    records = cursor.fetchall()
    id = ''
    
    
    check =0
    for row in records:
        if((userID==row[0] and aadhar == row[2])and password == row[1]):
            id = row[0]
            check = 1
            break
    
    return id,check

    
def admin_login_verify(username,password):
    conn = sqlite3.connect('ElectricityBillingSystem.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute('SELECT username,password FROM Admin')
    records = cursor.fetchall()
    check = 0
    
    
    for row in records:
        if(username == row[0] and password == row[1]):
            
            check = 1
            break
    
    return check

    
    