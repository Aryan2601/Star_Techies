from tkinter import *
from tkinter import ttk
import tkinter
from colorama import Cursor
from numpy import delete
from database import *
from verification import *
from data import *
from calc import *
from PIL import ImageTk,Image
from functools import partial



def enter_all_details():
    global enter_all_details_screen
    enter_all_details_screen = Toplevel(register_Screen)
    enter_all_details_screen.title("Unscuccessful")
    enter_all_details_screen.geometry("300x100")
    Label(enter_all_details_screen,text = "Enter all fields.").pack()
    Button(enter_all_details_screen,text = "OK",command = delete_enter_all_details_screen).pack()

def delete_enter_all_details_screen():
    enter_all_details_screen.destroy()



def register_success():
    global register_success_screen
    register_success_screen = Toplevel(register_Screen)
    register_success_screen.title("Success!!!")
    register_success_screen.geometry("300x100")
    Label(register_success_screen,text = "Registration successful,You can login NOW!").pack()
    Button(register_success_screen,text = "OK",command = delete_register_success_screen).pack()


def delete_register_success_screen():
    register_success_screen.destroy()
    register_Screen.destroy()

 

def invalid_aadhar_register():
    global invalid_aadhar_screen
    invalid_aadhar_screen = Toplevel(register_Screen)
    invalid_aadhar_screen.title("Unscuccessful")
    invalid_aadhar_screen.geometry("300x100")
    Label(invalid_aadhar_screen,text = "Enter valid UID").pack()
    Button(invalid_aadhar_screen,text = "OK",command = delete_invalid_aadhar_register).pack()

def delete_invalid_aadhar_register():
    invalid_aadhar_screen.destroy()


        
       

def invalid_password_register():
    global invalid_password_screen
    invalid_password_screen = Toplevel(register_Screen)
    invalid_password_screen.title("Unsuccessful")
    invalid_password_screen.geometry("300x100")
    Label(invalid_password_screen,text = "Minimum 8 character password").pack()
    Button(invalid_password_screen,text = "OK",command = delete_invalid_password_register).pack()


def delete_invalid_password_register():
    invalid_password_screen.destroy()

    



def register():
    def register_user():
        c = 0
        userID_info = userID_entry.get()
        Name_info = Name_entry.get()
        password_info = password_entry.get()
        address_info = address_entry.get()
        aadhar_info = aadhar_entry.get()
        radiobutton_info = var.get()
        if( len(userID_info)>0 and len(Name_info)>0  and len(password_info)>0 and len(address_info)>0  and len(aadhar_info)>0  and radiobutton_info !=0):

            if(len(password_info)<8):
                invalid_password_register()
            else:
                c = 1
            

            if(len(str(aadhar_info))!=12):
                invalid_aadhar_register()
            else:
                c = 1

            if(c == 1):
                
                writeondb(userID_info,Name_info,password_info,aadhar_info,address_info,radiobutton_info)
                #print("registeration success")
                register_success()

        else:
            enter_all_details()
    global register_Screen
    register_Screen = Toplevel(main_screen)
    register_Screen.title('Register page')
    screen_width = register_Screen.winfo_screenwidth()
    screen_height = register_Screen.winfo_screenheight()
    global Name
    Name = StringVar()
    global password 
    password = StringVar()
    global address 
    address = StringVar()
    global aadhar 
    aadhar = StringVar()
    global userID
    userID = StringVar()
    global var
    var = IntVar()
    window_width = (5*screen_width)//7
    window_height = (5*screen_height)//7

    center_x = int(screen_width/2-window_width/2)
    center_y = int(screen_height/2-window_height/2)

    register_Screen.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    register_Screen.resizable(False,False)

   # main_screen.iconbitmap('Images/logo.ico')
    background_image = ImageTk.PhotoImage(Image.open('C:\Chethan\My first git project\Star_Techies\Code\Register_page.jpg').resize((window_width+100,window_height),Image.ANTIALIAS))
    background_image_label = tkinter.Label(register_Screen, image=background_image)
    background_image_label.image = background_image
    background_image_label.place(x=0, y=0)
    
    register_frame = Frame(register_Screen, bg="white")
    register_frame.place(x=window_width // 30, y=(window_height // 4), height=4*window_height //5,
                      width=4 * window_width // 9)
    heading_label =Label(register_Screen,text="REGISTER PAGE", width="30", height="2", font=("Calibri", 13))
    heading_label.place(y=1* window_height // 20, x=7 * window_width // 20)
    userID_label = Label(register_frame, text="userID", font=("Goudy old style", 15, "bold"), fg="grey", bg="white")
    userID_entry = Entry(register_frame, font=("times new roman", 15), bg="lightgray")
    userID_entry.focus()
    Name_label = Label(register_frame, text="Name", font=("Goudy old style", 15, "bold"), fg="grey", bg="white")
    Name_entry = Entry(register_frame, font=("times new roman", 15), bg="lightgray")
    aadhar_label = Label(register_frame, text="Aadhar no.", font=("Goudy old style", 15, "bold"), fg="grey", bg="white")
    aadhar_entry = Entry(register_frame, font=("times new roman", 15), bg="lightgray")
    password_label = Label(register_frame, text="password", font=("Goudy old style", 15, "bold"), fg="grey", bg="white")
    password_entry = Entry(register_frame, font=("times new roman", 15), bg="lightgray",show = "*")
    address_label = Label(register_frame, text="Address", font=("Goudy old style", 15, "bold"), fg="grey", bg="white")
    address_entry = Entry(register_frame, font=("times new roman", 15), bg="lightgray")
    userID_label.place(y=1 * window_height // 20, x=window_width // 30)
    userID_entry.place(y=1 * window_height // 20, x=2.2 * window_width // 20, width=2 * window_width // 5 - 130)
    Name_label.place(y=2.5 * window_height // 20, x=window_width // 30)
    Name_entry.place(y=2.5 * window_height // 20, x=2.2 * window_width // 20, width=2 * window_width // 5 - 130)
    aadhar_label.place(y=4 * window_height // 20, x=window_width // 30)
    aadhar_entry.place(y=4 * window_height // 20, x=2.2 * window_width // 20, width=2 * window_width // 5 - 130)
    password_label.place(y=5.5 * window_height // 20, x=window_width // 30)
    password_entry.place(y=5.5 * window_height // 20, x=2.2 * window_width // 20, width=2 * window_width // 5 - 130)
    address_label.place(y=7 * window_height // 20, x=window_width // 30)
    address_entry.place(y=7 * window_height // 20, x=2.2 * window_width // 20, width=2 * window_width // 5 - 130)

    p=Label(register_frame, text="Enter payment mode", font=("Goudy old style", 15, "bold"), fg="grey", bg="white")
    p.place(y=8.5 * window_height // 20, x=2.2 * window_width // 20)

    R1 = Radiobutton(register_frame, text="Prepaid", variable=var, value=1)
    R1.place(y=10 * window_height // 20, x=2.2 * window_width // 20)
    R2 = Radiobutton(register_frame, text="Postpaid", variable=var, value=2)
    R2.place(y=11.5 * window_height // 20, x=2.2 * window_width // 20)
    
    t=Label(register_frame, text="")
    t.place(y=12.5 * window_height // 20, x=2.2 * window_width // 20)
    
    # Set register button
    register_button=Button(register_frame, text="Register", command=register_user, font=("Ariel 15 bold"))
    register_button.place(x=2.2*window_width // 30, y=14 * window_height // 20, height=window_height // 15,
                       width=2 * window_width // 5 - 35)
    
        
'''
# Set text variables
    global Name
    Name = StringVar()
    global password 
    password = StringVar()
    global address 
    address = StringVar()
    global aadhar 
    aadhar = StringVar()
    global userID
    userID = StringVar()
 
# Set label for user's instruction
    Label(register_Screen, text="Please enter details below", bg="#fcb603").pack()
    Label(register_Screen, text="").pack()
    
    userID_lable = Label(register_Screen, text="UserID ")
    userID_lable.pack()
 
# Set username entry
# The Entry widget is a standard Tkinter widget used to enter or display a single line of text.
    
    userID_entry = Entry(register_Screen, textvariable=userID)
    userID_entry.pack()
# Set username label
    Name_lable = Label(register_Screen, text="Name ")
    Name_lable.pack()
 
# Set username entry
# The Entry widget is a standard Tkinter widget used to enter or display a single line of text.
    
    Name_entry = Entry(register_Screen, textvariable=Name)
    Name_entry.pack()
   
# Set password label
    password_lable = Label(register_Screen, text="Password * ")
    password_lable.pack()
    
# Set password entry
    password_entry = Entry(register_Screen, textvariable=password, show='*')
    password_entry.pack()


#  set address label
    address_lable = Label(register_Screen,text = "Billing Address")
    address_lable.pack()


#set address entry
    address_entry = Entry(register_Screen,textvariable=address)
    address_entry.pack()


#set Aadhar label
    aadhar_lable = Label(register_Screen,text = "Aadhar Number")
    aadhar_lable.pack()

#set Aadhar entry
    aadhar_entry = Entry(register_Screen,textvariable=aadhar)
    aadhar_entry.pack()


#set radio button and label
    set_radioButton()

    
    Label(register_Screen, text="").pack()
    
    # Set register button
    Button(register_Screen, text="Register", width=10, height=1, bg="#fcb603",command = register_user).pack()
'''
'''
def set_radioButton():
    global var
    var = IntVar()

    Label(update_customer_frame,text = "Enter Payment mode").pack()

    R1 = Radiobutton(register_Screen, text="Prepaid", variable=var, value=1)
    R1.pack()
    R2 = Radiobutton(register_Screen, text="Postpaid", variable=var, value=2)
    R2.pack()
active_account_status = 0

'''
active_account_status = 0

def log_out_previous():
    global prev_log_out_screen
    prev_log_out_screen = Toplevel(login_screen)
    prev_log_out_screen.title("INVALID")
    prev_log_out_screen.geometry("300x100")
    Label(prev_log_out_screen,text = "Log out of currently logged in account!").pack()
    Button(prev_log_out_screen,text = "OK",command = destroy_prev_log_out_screen).pack()

def destroy_prev_log_out_screen():
    prev_log_out_screen.destroy()


def login_successful():
    global complaint_successful_screen
    complaint_successful_screen = Toplevel(login_screen)
    complaint_successful_screen.title("Login successful")
    complaint_successful_screen.geometry("300x100")
    Label(complaint_successful_screen,text = "Login Successful!").pack()
    Button(complaint_successful_screen,text = "Proceed",command = destroy_login_successful_screen).pack()


def destroy_login_successful_screen():
    complaint_successful_screen.destroy()
    login_screen.destroy()



def User_account_screen(ID):
    global user_screen
    user_screen = Toplevel(main_screen)
    user_screen.title('User account details')

    screen_width = user_screen.winfo_screenwidth()
    screen_height = user_screen.winfo_screenheight()
   
    window_width = (5*screen_width)//7
    window_height = (5*screen_height)//7

    center_x = int(screen_width/2-window_width/2)
    center_y = int(screen_height/2-window_height/2)

    user_screen.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    user_screen.resizable(False,False)

    # main_screen.iconbitmap('Images/logo.ico')
    background_image = ImageTk.PhotoImage(Image.open('C:\Chethan\My first git project\Star_Techies\Code\index.jpg').resize((window_width+100,window_height),Image.ANTIALIAS))
    background_image_label = tkinter.Label(user_screen, image=background_image)
    background_image_label.image = background_image
    background_image_label.place(x=0, y=0)
    user_frame = Frame(user_screen, bg="white")
    user_frame.place(x=window_width // 4, y=(window_height // 8), height=4*window_height //5,
                        width=4 * window_width // 9)
    record = []
    records = get_data(ID)
    print(records[0])
    for i in range(0,len(records[0])):
        record.append(records[0][i])
    print(record)
    userID_display_label = Label(user_frame,text = "USERID:"+str(record[0]),bg="#f7f2b7", width="50", height="2", font=("Calibri", 10))
    Name_display_label =Label(user_frame,text = "NAME:"+str(record[1]),bg="#f7f2b7", width="50", height="2", font=("Calibri", 10))
    aadhar_display_label=Label(user_frame,text = "UNIQUE IDENTIFICATION NUMBER:"+str(record[2]),bg="#73d6e6", width="50", height="2", font=("Calibri", 10))
    address_display_label =Label(user_frame,text = "CUSTOMER ADDRESS:"+str(record[3]),bg="#f7f2b7", width="50", height="2", font=("Calibri", 10))
    paymentmode_display_label =Label(user_frame,text = "PAYMENT MODE: "+str(record[4]),bg="#73d6e6", width="50", height="2", font=("Calibri", 10))
    units_display_label =Label(user_frame,text = "UNITS USED:  "+(str)(record[5]),bg="#f7f2b7", width="50", height="2", font=("Calibri", 10))
    month_display_label =Label(user_frame,text = "MONTHS DUE:  "+(str)(record[6]),bg="#73d6e6", width="50", height="2", font=("Calibri", 10))
    
    calculate_button =Button(user_frame,text="CALCULATE BILL",bg = "#f57e07",height="2", width="50", command = partial(calculate_bill,ID))
    complaint_box =Button(user_frame,text="Complaint box",bg = "#f57e07",height="2", width="50", command = make_complaint)
    logout_button = Button(user_frame,text="LOGOUT",bg = "#f57e07",height="2", width="50", command =logout_dialog)

    userID_display_label.place(y=1 * window_height // 20, x=window_width // 30)
    Name_display_label.place(y=2.5 * window_height // 20, x=window_width // 30)
    aadhar_display_label.place(y=4 * window_height // 20, x=window_width // 30)
    address_display_label.place(y=5.5 * window_height // 20, x=window_width // 30)
    paymentmode_display_label.place(y=7 * window_height // 20, x=  window_width // 30)
    units_display_label.place(y=8.5 * window_height // 20, x=window_width // 30)
    month_display_label.place(y=10 * window_height // 20, x= window_width // 30)
    calculate_button.place(y=11.5 * window_height // 20, x= window_width // 20, width=2 * window_width // 5 - 130)
    complaint_box.place(y=13 * window_height // 20, x= window_width // 20, width=2 * window_width // 5 - 130)
    logout_button.place(y=14.5 * window_height // 20, x= window_width // 20, width=2 * window_width // 5 - 130)


def logout_dialog():
    print("Enter")
    global active_account_status
    active_account_status = 0
    user_screen.destroy()
    
def admin_options():
    global admin_options_screen
    admin_options_screen = Toplevel(main_screen)
    admin_options_screen.title('User account details')

    screen_width = admin_options_screen.winfo_screenwidth()
    screen_height = admin_options_screen.winfo_screenheight()
   
    window_width = (5*screen_width)//7
    window_height = (5*screen_height)//7

    center_x = int(screen_width/2-window_width/2)
    center_y = int(screen_height/2-window_height/2)

    admin_options_screen.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    admin_options_screen.resizable(False,False)

    # main_screen.iconbitmap('Images/logo.ico')
    background_image = ImageTk.PhotoImage(Image.open('C:\Chethan\My first git project\Star_Techies\Code\windmills.jpg').resize((window_width+100,window_height),Image.ANTIALIAS))
    background_image_label = tkinter.Label(admin_options_screen, image=background_image)
    background_image_label.image = background_image
    background_image_label.place(x=0, y=0)
    admin_options_frame = Frame(admin_options_screen, bg="white")
    admin_options_frame.place(x=window_width // 4, y=(window_height // 8), height=4*window_height //5,
                        width=4 * window_width // 9)
    print("correct")
    heading_label =Label(admin_options_screen,text="ADMIN OPTIONS", width="30", height="2", font=("Calibri", 13))
    heading_label.place(y=1* window_height // 20, x=7 * window_width // 20)
    Label(admin_options_frame,text = "Choose from below").place(y=1 * window_height // 20, x=window_width // 12)
    Button(admin_options_frame,bg = "#f57e07",height="2", width="50",text = "Update customer details:",command = update_customer).place(x=window_width // 13, y=2 * window_height // 20, height=window_height // 15,
                        width=2 * window_width // 5 - 130)
    Button(admin_options_frame,bg = "#f57e07",height="2", width="50",text = "  View complaint box:  ",command = seeing_complaints).place(x=window_width // 13, y=5 * window_height // 20, height=window_height // 15,
                        width=2 * window_width // 5 - 130)
    Button(admin_options_frame,bg = "#f57e07",height="2", width="50",text = "Delete complaint:",command = deleting_complaint).place(x=window_width // 13, y=8 * window_height // 20, height=window_height // 15,
                        width=2 * window_width // 5 - 130)
    Button(admin_options_frame,bg = "#f57e07",height="2", width="50",text = "LOGOUT",command = admin_logout).place(x=window_width // 13, y=11 * window_height // 20, height=window_height // 15,
                        width=2 * window_width // 5 - 130)


def admin_logout():
    global active_account_status
    active_account_status = 0
    admin_options_screen.destroy()




def calculate_bill(ID):
    bill,fine  = bill_calculation(ID)
    addbill(ID,bill,fine)
    global bill_screen
    bill_screen = Toplevel(user_screen)
    bill_screen.title("BILL")
    bill_screen.geometry("300x300")
    Label(bill_screen,text = "Bill Details",bg="#fcb603", width="300", height="2", font=("Calibri", 13)).pack()
    Label(bill_screen,text = "Total amount to be paid:"+(str)(bill),bg="#BEDAD8", width="300", height="2", font=("Calibri", 10)).pack()
    Label(bill_screen,text = "Fine included in total amount:"+(str)(fine),bg="#BEDAD8", width="300", height="2", font=("Calibri", 10)).pack()
    
    Button(bill_screen,text="PAY:"+(str)(bill),bg = "#91EAE3",height="2", width="300", command =partial(bill_payment,ID)).pack()   
    Button(bill_screen,text="CLOSE",bg = "#91EAE3",height="2", width="300", command =close_bill_screen).pack()


def make_complaint():
    global make_complaint_screen
    make_complaint_screen = Toplevel(user_screen) 
    make_complaint_screen.title("Making complaint")
    make_complaint_screen.geometry("300x300")
    global userID_make
    userID_make = StringVar()
    global complaint_make
    complaint_make = StringVar()

    userID_label = Label(make_complaint_screen,text="Enter your username")
    userID_label.pack()
    userID_entry= Entry(make_complaint_screen, textvariable=userID_make)
    userID_entry.pack()
   
# Set complaint label
    complaint_lable = Label(make_complaint_screen, text=" Enter your complaint ")
    complaint_lable.pack()
    
# Set complaint entry
    complaint_entry = Entry(make_complaint_screen, textvariable=complaint_make)
    complaint_entry.pack()
    Label(make_complaint_screen, text="").pack()
    Button(make_complaint_screen, text="Submit", width=10, height=1, bg="#fcb603",command = giving_complaint).pack()
    
    # Set register button
def giving_complaint():
    userID_info = userID_make.get()
    complaint_info = complaint_make.get()
    print(userID_info)
    print(complaint_info)
    making_complaint(userID_info,complaint_info)
    complaint_given_successful()


def complaint_given_successful():
    global complaint_successful_screen
    complaint_successful_screen = Toplevel(main_screen)
    complaint_successful_screen.title("removal successful")
    complaint_successful_screen.geometry("300x100")
    Label(complaint_successful_screen,text = "deleted Successfulyl!").pack()
    Button(complaint_successful_screen,text = "Proceed",command =make_complaint_screen.destroy()).pack()
    complaint_successful_screen.destroy() 


def seeing_complaints():
   win = Tk()
   win.geometry("700x350")
  # Create an object of Style widget
   style = ttk.Style()
   style.theme_use('clam')
   tree = ttk.Treeview(win, column=("UserID", "Issue",), show='headings', height=5)
   tree.column("# 1", anchor=CENTER)
   tree.heading("# 1", text="userID")
   tree.column("# 2", anchor=CENTER)
   tree.heading("# 2", text="Issue")
   records = view_complaints()
   for row in records:
       tree.insert('', 'end', text="1", values=(row[0],row[1]))
   tree.pack()

   win.mainloop()

    
def deleting_complaint():
    global delete_complaint_screen
    global username
    username = StringVar()
    delete_complaint_screen =Toplevel(main_screen)
    delete_complaint_screen.title("Deleting complaints")
    delete_complaint_screen.geometry("300x100")
    username_label = Label(delete_complaint_screen,text="Enter your username")
    username_label.pack()
    username_entry= Entry(delete_complaint_screen, textvariable=username)
    username_entry.pack()
    
    Label(delete_complaint_screen, text="").pack()
    
    # Set register button
    Button(delete_complaint_screen, text="Delete", width=10, height=1, bg="#fcb603",command = remove_complaint).pack()

def remove_complaint():
    userID_info = username.get()
    delete_complaint(userID_info)
    removing_successful()

def removing_successful():
    global remove_successful_screen
    remove_successful_screen = Toplevel(main_screen)
    remove_successful_screen.title("removal successful")
    remove_successful_screen.geometry("300x100")
    Label(remove_successful_screen,text = "deleted Successfulyl!").pack()
    Button(remove_successful_screen,text = "Proceed",command =delete_complaint_screen.destroy()).pack()
    remove_successful_screen.destroy() 


    
def bill_payment(ID):
    bill = 0
    fine = 0
    
    
    addbill(ID,bill,fine)
    update_unit(ID)
    global bill_payment_confirm_screen
    bill_payment_confirm_screen = Toplevel(bill_screen)
    bill_payment_confirm_screen.title("CONFIRM")
    bill_payment_confirm_screen.geometry("300x100")
    Label(bill_payment_confirm_screen,text = "Bill Successfully Paid!").pack()
    Button(bill_payment_confirm_screen,text = "OK",command = destroy_confirm_screen).pack()

def destroy_confirm_screen():
    bill_payment_confirm_screen.destroy()
    bill_screen.destroy()


def close_bill_screen():
    bill_screen.destroy()


def login_verify_failed():
    global login_verify_failed_screen
    login_verify_failed_screen = Toplevel(login_screen)
    login_verify_failed_screen.title(" Login Unscuccessful")
    login_verify_failed_screen.geometry("300x100")
    Label(login_verify_failed_screen,text = "Enter login details correctly!").pack()
    Button(login_verify_failed_screen,text = "OK",command = delete_login_verify_failed_screen).pack()

def delete_login_verify_failed_screen():
    login_verify_failed_screen.destroy()


# define login function
def login_screen():
    def login_verification():
        userID=userID_entry_login.get()
        password = password_entry_login.get()
        aadhar_number = aadhar_entry_login.get()
        global active_account_status
        
        if(active_account_status == 0):

            if((len(userID)>0 and len(aadhar_number)>0) and len(password)>0): 
                ID,check = login_verify(userID,aadhar_number,password)

                
                if(check == 1):
                    active_account_status = 1
                    login_successful()
                    User_account_screen(userID)

                else:
                    login_verify_failed()



            else:
                login_verify_failed()

        else:
            log_out_previous()
        
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title('Login page')

    screen_width = login_screen.winfo_screenwidth()
    screen_height = login_screen.winfo_screenheight()
   
    window_width = (5*screen_width)//7
    window_height = (5*screen_height)//7

    center_x = int(screen_width/2-window_width/2)
    center_y = int(screen_height/2-window_height/2)

    login_screen.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    login_screen.resizable(False,False)

    # main_screen.iconbitmap('Images/logo.ico')
    background_image = ImageTk.PhotoImage(Image.open('C:\Chethan\My first git project\Star_Techies\Code\login_page.jpg').resize((window_width+100,window_height),Image.ANTIALIAS))
    background_image_label = tkinter.Label(login_screen, image=background_image)
    background_image_label.image = background_image
    background_image_label.place(x=0, y=0)
    login_frame = Frame(login_screen, bg="white")
    login_frame.place(x=window_width // 12, y=(window_height//3), height=4*window_height //7,
                        width=4 * window_width // 9)
    heading_label =Label(login_screen,text="LOGIN PAGE", width="30", height="2", font=("Calibri", 13))
    heading_label.place(y=window_height //5, x=3 * window_width // 20)
    userID_label_login = Label(login_frame, text="userID", font=("Goudy old style", 15, "bold"), fg="grey", bg="white")
    userID_entry_login = Entry(login_frame, font=("times new roman", 15), bg="lightgray")
    userID_entry_login.focus()
    aadhar_label_login = Label(login_frame, text="Aadharno", font=("Goudy old style", 15, "bold"), fg="grey", bg="white")
    aadhar_entry_login = Entry(login_frame, font=("times new roman", 15), bg="lightgray")
    password_label_login = Label(login_frame, text="password", font=("Goudy old style", 15, "bold"), fg="grey", bg="white")
    password_entry_login = Entry(login_frame, font=("times new roman", 15), bg="lightgray",show = "*")
    userID_label_login.place(y=1 * window_height // 20, x=window_width // 30)
    userID_entry_login.place(y=1 * window_height // 20, x=2.2 * window_width // 20, width=2 * window_width // 5 - 130)
    aadhar_label_login.place(y=2.5 * window_height // 20, x=window_width // 30)
    aadhar_entry_login.place(y=2.5 * window_height // 20, x=2.2 * window_width // 20, width=2 * window_width // 5 - 130)
    password_label_login.place(y=4 * window_height // 20, x=window_width // 30)
    password_entry_login.place(y=4 * window_height // 20, x=2.2 * window_width // 20, width=2 * window_width // 5 - 130)

    # Set register button
    login_button=Button(login_frame, text="Login", command=login_verification, font=("Ariel 15 bold"))
    login_button.place(x=2.2*window_width // 13, y=5.5 * window_height // 20, height=window_height // 15,
                        width=2 * window_width // 15 - 35)

def admin_login_successful():
    global admin_login_successful_screen
    admin_login_successful_screen = Toplevel(admin_login_screen)
    admin_login_successful_screen.title("Admin Login successful")
    admin_login_successful_screen.geometry("300x100")
    Label(admin_login_successful_screen,text = "Login Successful!").pack()
    Button(admin_login_successful_screen,text = "Proceed",command = destroy_admin_login_successful_screen).pack()

def destroy_admin_login_successful_screen():
    admin_login_successful_screen.destroy()
    admin_login_screen.destroy()


def admin_login_verify_failed():
    global admin_login_verify_failed_screen
    admin_login_verify_failed_screen = Toplevel(admin_login_screen)
    admin_login_verify_failed_screen.title(" Login Unscuccessful")
    admin_login_verify_failed_screen.geometry("300x100")
    Label(admin_login_verify_failed_screen,text = "Enter login details correctly!").pack()
    Button(admin_login_verify_failed_screen,text = "OK",command = delete_admin_login_verify_failed_screen).pack()

def delete_admin_login_verify_failed_screen():
    admin_login_verify_failed_screen.destroy()


def update_customer():
    def update_customer_get():
        print("enter")
        ID = userID_entry_update.get()
        username = Name_entry_update.get()
        password = password_entry_update.get()
        units = units_entry_update.get()
        months = months_entry_update.get()
        address = address_entry_update.get()
        update_customer_admin(ID,username,password,address,units,months)
        global success_screen
        success_screen = Toplevel(main_screen)
        success_screen.title("success")
        success_screen.geometry("300x100")
        Label(success_screen,text = "Updation Successful!")
        Button(success_screen,text = "OK",command = destroy_success_screen)
    global update_customer_screen
    update_customer_screen = Toplevel(admin_options_screen)
    update_customer_screen.title('Update customer details')
    screen_width = update_customer_screen.winfo_screenwidth()
    screen_height = update_customer_screen.winfo_screenheight()
    global Name
    Name = StringVar()
    global password 
    password = StringVar()
    global address 
    address = StringVar()
    global aadhar 
    aadhar = StringVar()
    global userID
    userID = StringVar()
    global var
    var = IntVar()
    window_width = (5*screen_width)//7
    window_height = (5*screen_height)//7

    center_x = int(screen_width/2-window_width/2)
    center_y = int(screen_height/2-window_height/2)

    update_customer_screen.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    update_customer_screen.resizable(False,False)

   # main_screen.iconbitmap('Images/logo.ico')
    background_image = ImageTk.PhotoImage(Image.open('C:\Chethan\My first git project\Star_Techies\Code\elctric.jpg').resize((window_width+100,window_height),Image.ANTIALIAS))
    background_image_label = tkinter.Label(update_customer_screen, image=background_image)
    background_image_label.image = background_image
    background_image_label.place(x=0, y=0)
    update_customer_frame = Frame(update_customer_screen, bg="white")
    update_customer_frame.place(x=window_width // 30, y=(window_height // 4), height=4*window_height //5,
                      width=4 * window_width // 9)
    heading_label =Label(update_customer_screen,text="UPDATE CUSTOMER PAGE", width="30", height="2", font=("Calibri", 13))
    heading_label.place(y=1* window_height // 20, x=7 * window_width // 20)
    userID_label_update = Label(update_customer_frame, text="userID", font=("Goudy old style", 15, "bold"), fg="grey", bg="white")
    userID_entry_update = Entry(update_customer_frame, font=("times new roman", 15), bg="lightgray")
    userID_entry_update.focus()
    Name_label_update = Label(update_customer_frame, text="Name", font=("Goudy old style", 15, "bold"), fg="grey", bg="white")
    Name_entry_update = Entry(update_customer_frame, font=("times new roman", 15), bg="lightgray")
    password_label_update = Label(update_customer_frame, text="password", font=("Goudy old style", 15, "bold"), fg="grey", bg="white")
    password_entry_update = Entry(update_customer_frame, font=("times new roman", 15), bg="lightgray",show = "*")
    address_label_update = Label(update_customer_frame, text="Address", font=("Goudy old style", 15, "bold"), fg="grey", bg="white")
    address_entry_update = Entry(update_customer_frame, font=("times new roman", 15), bg="lightgray")
    units_label_update = Label(update_customer_frame, text="Units", font=("Goudy old style", 15, "bold"), fg="grey", bg="white")
    units_entry_update = Entry(update_customer_frame, font=("times new roman", 15), bg="lightgray")
    months_label_update = Label(update_customer_frame, text="Months due" ,font=("Goudy old style", 15, "bold"), fg="grey", bg="white")
    months_entry_update = Entry(update_customer_frame, font=("times new roman", 15), bg="lightgray")
    userID_label_update.place(y=1 * window_height // 20, x=window_width // 30)
    userID_entry_update.place(y=1 * window_height // 20, x=2.2 * window_width // 20, width=2 * window_width // 5 - 130)
    Name_label_update.place(y=2.5 * window_height // 20, x=window_width // 30)
    Name_entry_update.place(y=2.5 * window_height // 20, x=2.2 * window_width // 20, width=2 * window_width // 5 - 130)
    password_label_update.place(y=4 * window_height // 20, x=window_width // 30)
    password_entry_update.place(y=4 * window_height // 20, x=2.2 * window_width // 20, width=2 * window_width // 5 - 130)
    address_label_update.place(y=5.5 * window_height // 20, x=window_width // 30)
    address_entry_update.place(y=5.5 * window_height // 20, x=2.2 * window_width // 20, width=2 * window_width // 5 - 130)
    units_label_update.place(y=7 * window_height // 20, x=window_width // 30)
    units_entry_update.place(y=7 * window_height // 20, x=2.2 * window_width // 20, width=2 * window_width // 5 - 130)
    months_label_update.place(y=8.5 * window_height // 20, x=window_width // 30)
    months_entry_update.place(y=8.5 * window_height // 20, x=2.2 * window_width // 20, width=2 * window_width // 5 - 130)
    # Set register button
    update_button=Button(update_customer_frame, text="Update", command=update_customer_get, font=("Ariel 15 bold"))
    update_button.place(x=2.2*window_width // 30, y=10 * window_height // 20, height=window_height // 15,
                       width=2 * window_width // 5 - 35)
    Button(update_customer_screen,text = "CLOSE",height = "2",width = "10",command = destroy_update_customer_screen).place(x=2.2*window_width // 30, y=18 * window_height // 20, 
    height=window_height // 15,width=2 * window_width // 5 - 35)

def destroy_update_customer_screen():
    update_customer_screen.destroy()



def destroy_success_screen():
    success_screen.destroy()


def admin_logout_previous():
    global admin_prev_log_out_screen
    admin_prev_log_out_screen = Toplevel(register_Screen)
    admin_prev_log_out_screen.title("INVALID")
    admin_prev_log_out_screen.geometry("300x100")
    Label(admin_prev_log_out_screen,text = "Log out of currently logged in account!").pack()
    Button(admin_prev_log_out_screen,text = "OK",command = destroy_admin_prev_log_out_screen).pack()

def destroy_admin_prev_log_out_screen():
    admin_prev_log_out_screen.destroy()



def admin_login_verification():
    username = admin_username_verify.get()
    password = admin_password_verify.get()
    global active_account_status
    
    if(active_account_status == 0):

        if(len(username)>0  and len(password)>0): 
            check = admin_login_verify(username,password)

            
            if(check == 1):
                active_account_status = 1
                admin_login_successful()
                admin_options()

            else:
                admin_login_verify_failed()



        else:
            admin_login_verify_failed()

    #else:
        #admin_log_out_previous()


def admin_login_screen():
    global admin_login_screen
    admin_login_screen = Toplevel(main_screen)
    admin_login_screen.title("Admin Login")
    admin_login_screen.geometry("300x300")
    Label(admin_login_screen, text="Please enter details below to login").pack()
    Label(admin_login_screen, text="").pack()
 
    global admin_username_verify
    global admin_password_verify
    
 
    admin_username_verify = StringVar()
    admin_password_verify = StringVar()
   
    Label(admin_login_screen, text="Username ").pack()
    username_login_entry = Entry(admin_login_screen, textvariable=admin_username_verify)
    username_login_entry.pack()

    
    Label(admin_login_screen, text="").pack()
    Label(admin_login_screen, text="Password * ").pack()
    password__login_entry = Entry(admin_login_screen, textvariable=admin_password_verify, show= '*')
    password__login_entry.pack()

    Label(admin_login_screen, text="").pack()
    Button(admin_login_screen, text="Login", width=10, height=1, command=admin_login_verification).pack()



    



def main_account_screen():
    global main_screen
 
# add command=register in button widget
 
    
    main_screen = tkinter.Tk()
    main_screen.title('Login page')
    screen_width = main_screen.winfo_screenwidth()
    screen_height = main_screen.winfo_screenheight()

    window_width = (5*screen_width)//7
    window_height = (5*screen_height)//7

    center_x = int(screen_width/2-window_width/2)
    center_y = int(screen_height/2-window_height/2)

    main_screen.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

   # main_screen.iconbitmap('Images/logo.ico')
    background_image = ImageTk.PhotoImage(Image.open('C:\Chethan\My first git project\Star_Techies\Code\elctric.jpg').resize((window_width+100,window_height),Image.ANTIALIAS))
    background_image_label = tkinter.Label(main_screen, image=background_image)
    background_image_label.image = background_image
    background_image_label.place(x=0, y=0)
    main_screen.resizable(False,False)

    Label(text="Electricity Billing system", bg="#87CEFA", width="300", height="2", font=("Calibri", 13)).pack() 
    Label(text="").pack() 
    # create Login Button 
    Button(text="Login", height="4", width="40", command = login_screen).pack()
    Label(text="").pack() 


    Button(text="Register", height="4", width="40", command=register).pack()
    Label(text = "").pack()
    Button(text = "Admin Login",height = "4",width = "40",command = admin_login_screen).pack()

    main_screen.mainloop()
 
main_account_screen()

