import sqlite3
connection = sqlite3.connect("ElectricityBillingSystem.db")

def writeondb(username,password,aadhar,address,radio_button):
    if (radio_button == 1):
        payment = "prepaid"
    else:
        payment = "postpaid"
    
    connection = sqlite3.connect("ElectricityBillingSystem.db")
    with connection:
        cursor = connection.cursor()
    
    cursor.execute('Create TABLE IF NOT EXISTS Customer(ID integer PRIMARY KEY AUTOINCREMENT,  Username TEXT,Password TEXT,aadhar_number TEXT,Address TEXT,payment_mode TEXT,Units INTEGER DEFAULT 0,Months_due INTEGER DEFAULT 0,Bill REAL DEFAULT 0.0,Fine REAL DEFAULT 0.0)')
    cursor.execute('INSERT INTO Customer (Username,Password,aadhar_number,Address,payment_mode) VALUES(?,?,?,?,?)',(username,password,aadhar,address,payment))
    connection.commit()

def making_complaint(ID,username,text):
    connection = sqlite3.connect("ElectricityBillingSystem.db")
    with connection:
        cursor = connection.cursor()
    cursor.execute('Create TABLE Complaint(ID integer PRIMARY KEY AUTOINCREMENT, Issue TEXT')
    cursor.execute('INSERT INTO Complaint(ID,Issue) VALUES(?,?)')
    connection.commit()

def view_complaints():
    connection = sqlite3.connect("ElectricityBillingSystem.db")
    with connection:
        cursor = connection.cursor()
    cursor.execute('Select * from Complaint')
    connection.commit()

def delete_complaint(ID):
    connection = sqlite3.connect("ElectricityBillingSystem.db")
    with connection:
        cursor = connection.cursor()
    cursor.execute('Delete * from Complaint where ID=?',(ID))
    connection.commit()

def addbill(ID,bill,fine):
    ID = (str)(ID)
    bill = (str)(bill)
    fine = (str)(fine)
    connection = sqlite3.connect('ElectricityBillingSystem.db')
    with connection:
        cursor = connection.cursor()
    cursor.execute('UPDATE Customer SET Bill = ? WHERE ID = ?',(bill,ID))
    cursor.execute('UPDATE Customer SET Fine = ? WHERE ID = ?',(fine,ID))
    connection.commit()

def update_unit(ID):
    ID = (str)(ID)
  
    connection = sqlite3.connect('ElectricityBillingSystem.db')
    with connection:
        cursor = connection.cursor()
    cursor.execute('UPDATE Customer SET Units = 0 WHERE ID = ?',(ID))
    cursor.execute('UPDATE Customer SET Months_due = 0 WHERE ID = ?',(ID))

    connection.commit()

def update_customer_admin(ID,username,password,address,units,month):
    id = (str)(ID)
    Units = (str)(units)
    Month = (str)(month)

    
    connection = sqlite3.connect('ElectricityBillingSystem.db')
    with connection:
        cursor = connection.cursor()

    if(len(username)>0):
        cursor.execute('UPDATE Customer SET Username = ? WHERE ID = ?',(username,id))

    if(len(password) > 0):
         cursor.execute('UPDATE Customer SET Password = ? WHERE ID = ?',(password,id))

    if(len(address) > 0):
         cursor.execute('UPDATE Customer SET Address = ? WHERE ID = ?',(address,id))

    if(units > 0):
         cursor.execute('UPDATE Customer SET Units = ? WHERE ID = ?',(Units,id))

    if(month > 0):
         cursor.execute('UPDATE Customer SET Months_due = ? WHERE ID = ?',(Month,id))


    connection.commit()