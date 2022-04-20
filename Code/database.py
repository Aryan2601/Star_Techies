import sqlite3
connection = sqlite3.connect("ElectricityBillingSystem.db")

def writeondb(userID,Name,password,aadhar,address,radio_button):
    if (radio_button == 1):
        payment = "prepaid"
    else:
        payment = "postpaid"
    
    connection = sqlite3.connect("ElectricityBillingSystem.db")
    with connection:
        cursor = connection.cursor()
    cursor.execute('Create TABLE IF NOT EXISTS Customer(userID TEXT PRIMARY KEY,  Name TEXT,Password TEXT,aadhar_number TEXT,Address TEXT,payment_mode TEXT,Units INTEGER DEFAULT 0,Months_due INTEGER DEFAULT 0,Bill REAL DEFAULT 0.0,Fine REAL DEFAULT 0.0)')
    cursor.execute('INSERT INTO Customer (userID,Name,Password,aadhar_number,Address,payment_mode) VALUES(?,?,?,?,?,?)',(userID,Name,password,aadhar,address,payment))
    connection.commit()

def making_complaint(userID,Issue):
    print(userID,Issue)
    connection = sqlite3.connect("ElectricityBillingSystem.db")
    with connection:
        cursor = connection.cursor()
    cursor.execute('Create TABLE IF NOT EXISTS Complaint(userID TEXT PRIMARY KEY,Issue TEXT)')
    cursor.execute('INSERT INTO Complaint (userID,Issue) VALUES(?,?)',(str(userID),str(Issue)))
    k=cursor.execute("Select Issue from Complaint where userID='chethan96045'")
    k=cursor.fetchone()
    print(k)
    connection.commit()

def view_complaints():
    connection = sqlite3.connect("ElectricityBillingSystem.db")
    with connection:
        cursor = connection.cursor()
    k=cursor.execute("Select * from Complaint")
    connection.commit()
    return k

def delete_complaint(ID):
    connection = sqlite3.connect("ElectricityBillingSystem.db")
    view_complaints()
    with connection:
        cursor = connection.cursor()
    cursor.execute('Delete from Complaint where userID=?',[str(ID)])
    view_complaints()
    connection.commit()

def addbill(ID,bill,fine):
    ID = (str)(ID)
    bill = (str)(bill)
    fine = (str)(fine)
    connection = sqlite3.connect('ElectricityBillingSystem.db')
    with connection:
        cursor = connection.cursor()
    cursor.execute('UPDATE Customer SET Bill = ? WHERE userID = ?',(bill,ID))
    cursor.execute('UPDATE Customer SET Fine = ? WHERE userID = ?',(fine,ID))
    connection.commit()

def update_unit(ID):
    ID = (str)(ID)
  
    connection = sqlite3.connect('ElectricityBillingSystem.db')
    with connection:
        cursor = connection.cursor()
    cursor.execute('UPDATE Customer SET Units = 0 WHERE userID = ?',[ID])
    cursor.execute('UPDATE Customer SET Months_due = 0 WHERE userID = ?',[ID])

    connection.commit()

def update_customer_admin(ID,Name,password,address,units,month):
    id = (str)(ID)
    Units = (str)(units)
    Month = (str)(month)

    
    connection = sqlite3.connect('ElectricityBillingSystem.db')
    with connection:
        cursor = connection.cursor()

    if(len(Name)>0):
        cursor.execute('UPDATE Customer SET Name = ? WHERE userID = ?',(Name,id))

    if(len(password) > 0):
         cursor.execute('UPDATE Customer SET Password = ? WHERE userID = ?',(password,id))

    if(len(address) > 0):
         cursor.execute('UPDATE Customer SET Address = ? WHERE userID = ?',(address,id))

    if(units > 0):
         cursor.execute('UPDATE Customer SET Units = ? WHERE userID = ?',(Units,id))

    if(month > 0):
         cursor.execute('UPDATE Customer SET Months_due = ? WHERE userID = ?',(Month,id))


    connection.commit()

def creating_Admin():
    connection = sqlite3.connect("ElectricityBillingSystem.db")
    with connection:
        cursor = connection.cursor()
    cursor.execute("CREATE TABLE Admin (username TEXT PRIMARY KEY , password TEXT)")
    cursor.execute("INSERT INTO Admin(username,password) VALUES ('chethan','19243')")
    cursor.execute("INSERT INTO Admin(username,password) VALUES ('charan','19232')")
    cursor.execute("INSERT INTO Admin(username,password) VALUES ('Anand','19208')")
    cursor.execute("INSERT INTO Admin(username,password) VALUES ('Aryan','19221')")
    connection.commit() 