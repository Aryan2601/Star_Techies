import sqlite3

def get_data(id):
    conn = sqlite3.connect('ElectricityBillingSystem.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute('SELECT UserID,Name,aadhar_number,Address,payment_mode,Units,Months_due,Bill,Fine FROM Customer WHERE userID=?',[id])
    records = cursor.fetchall()
    return(records)