import data
import sqlite3

def bill_calculation(id):
    conn = sqlite3.connect('ElectricityBillingSystem.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute('SELECT Units,Months_due,Bill,Fine FROM Customer WHERE ID='+(str)(id))
    records = cursor.fetchall()
    
    record = []
    for i in range(0,len(records[0])):
        record.append(records[0][i])

    #bill generation
    units=record[0]

    if(record[1] > 0):
        fine = 100*record[1]

    else:
        fine  = 0

    if(units > 0):

        if(units<=100):
            payAmount=units*1.5
            fixedcharge=25.00
        elif(units<=200):
            payAmount=(100*1.5)+(units-100)*2.5
            fixedcharge=50.00
        elif(units<=300):
            payAmount=(100*1.5)+(200-100)*2.5+(units-200)*4
            fixedcharge=75.00
        elif(units<=350):
            payAmount=(100*1.5)+(200-100)*2.5+(300-200)*4+(units-300)*5
            fixedcharge=100.00
        else:
            payAmount=0
            fixedcharge=1500.00

        Total=payAmount+fixedcharge+fine
        

    else:
        Total = 0

    

    return Total,fine