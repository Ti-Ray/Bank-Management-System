# # POINTS TO REMEMBER
# - Remember to change the about us link
# - Remember to comment properly and define clearly
import random
import webbrowser
from CTkMessagebox import CTkMessagebox
import customtkinter
from tkinter import *
from PIL import Image


customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("Dark")

main = customtkinter.CTk()
main.geometry("850x600")

# File set up

# def create_account():
# def login_account():


# # Frames
global nm_ent
global em_ent
global pass_ent
global cpass_ent
global acc_type
global account
global an_ent
global email_ent
global lg_pass_ent
global bal


def logged():
    md_page = customtkinter.CTkFrame(master=main)
    md_page.pack(fill="both", expand=True, padx=10, pady=10)
    img_w = 700
    img_h = 1400
    img3_path = "in.png"
    img3 = customtkinter.CTkImage(light_image=Image.open(img3_path), size=(img_h, img_w))
    lab4 = customtkinter.CTkLabel(master=md_page, image=img3, text=" ")
    lab4.pack(fill="both", expand=True, padx=10, pady=10)

    # This button is for the user to carry out a cash withdrawal from their account
    with_btn = customtkinter.CTkButton(master=md_page, width=100, height=2, text="Withdraw")
    with_btn.place(anchor=CENTER, relx=.5, rely=.4)

    # This button is for the user to deposit cash to their account
    dep_btn = customtkinter.CTkButton(master=md_page, width=100, height=2, text="Deposit")
    dep_btn.place(anchor=CENTER, relx=.5, rely=.5)

    # This button is for the user to check the balance in their bank account
    check_btn = customtkinter.CTkButton(master=md_page, width=100, height=2, text="Check Balance")
    check_btn.place(anchor=CENTER, relx=.5, rely=.6)

    # This button is for the user to request a bank statement for their accounts transactions
    state_btn = customtkinter.CTkButton(master=md_page, width=100, height=2, text="Statement")
    state_btn.place(anchor=CENTER, relx=.5, rely=.7)

    # This button is for the user to end their account
    del_btn = customtkinter.CTkButton(master=md_page, width=100, height=2, text="Delete Account", text_color="red",
                                      fg_color="green")
    del_btn.place(anchor=CENTER, relx=.5, rely=.8)

    # This button is for the user to logout of their account
    logout_btn = customtkinter.CTkButton(master=md_page, width=90, height=2, text="Log Out", fg_color="brown",
                                         command=lambda: back(main_pg, md_page))
    logout_btn.place(anchor=CENTER, relx=.1, rely=.1)


def main_pg():
    def close():
        main.destroy()

    # # main page when the app is started
    def callback(url):
        webbrowser.open_new_tab(url)

    page1 = customtkinter.CTkFrame(master=main, width=500, height=500)  # This is frame holds login or register buttons
    page1.pack(fill="both", expand=True, padx=10, pady=10)

    # Objects
    img1_h = 1400
    img1_w = 1400
    img1_path = "im1.png"
    pg1img = customtkinter.CTkImage(light_image=Image.open(img1_path), size=(img1_w, img1_h))
    lab = customtkinter.CTkLabel(master=page1, image=pg1img, text=" ")
    lab.pack(fill="both", expand=True, padx=10, pady=10)

    # This button is to take the user to the login page
    login_btn = customtkinter.CTkButton(master=page1, width=100, height=50, bg_color='black', fg_color='brown',
                                        text="LOGIN", command=lambda: enter(login, page1))
    login_btn.place(anchor=CENTER, relx=.5, rely=.4)

    # This button is to take the user to the registration page
    reg_btn = customtkinter.CTkButton(master=page1, width=100, height=50, bg_color='black', fg_color='brown',
                                      text="REGISTER", command=lambda: enter(reg, page1))
    reg_btn.place(anchor=CENTER, relx=.5, rely=.5)

    # This button is to completely close the program
    cls_btn = customtkinter.CTkButton(master=page1, width=100, height=50, bg_color='black', fg_color='brown',
                                      text="close", command=close)
    cls_btn.place(anchor=CENTER, relx=.5, rely=.6)

    # This button is to take the user to the company website to learn more about the company
    about_link = customtkinter.CTkButton(master=page1, text="About us", bg_color="black", fg_color="brown", width=100,
                                         height=50)
    about_link.place(anchor=CENTER, relx=.5, rely=.7)
    about_link.bind("<Button-1>", lambda e: callback("https://www.youtube.com/"))


def login():
    # Login
    def login_check():
        try:
            path = str(an_ent.get()+"-reg.txt")  # Fetches user input on their account number
            # global ac_num
            num = (lg_pass_ent.get()+"\n")  # Fetches user input on the password
            em = (email_ent.get()+"\n")  # Fetches user input on the email
            file_ch = open(path, "r")
            name = file_ch.readline()  # Reads the first line containing the name
            e_mail = file_ch.readline()  # Reads the second line containing the email
            entry = file_ch.readline()  # Reads the third line containing the password
            a_type = file_ch.readline()  # Reads the account type
            if em != e_mail:
                CTkMessagebox(title="Error", message="Incorrect Email / Password")
            elif entry != num:
                CTkMessagebox(title="Error", message="Incorrect Email / Password")
            else:
                enter(logged, lg_frame)
        except:
            CTkMessagebox(title="Error", message="Account not available")

    # Login page Happens when the login button is pressed
    lg_frame = customtkinter.CTkFrame(master=main)
    lg_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # This section places the image for the login page
    img2_h = 900
    img2_w = 1400
    img2_path = "login.png"
    img2 = customtkinter.CTkImage(light_image=Image.open(img2_path), size=(img2_w, img2_h))
    lab2 = customtkinter.CTkLabel(master=lg_frame, text=" ", image=img2)
    lab2.pack(fill="both", expand=True)
    # This section is for the entry of the account number
    an_ent = customtkinter.CTkEntry(master=lg_frame, placeholder_text="Enter your Account number", width=200, height=20,
                                    bg_color="blue", fg_color="blue")
    an_ent.place(anchor=CENTER, relx=.5, rely=.4)
    # This entry section is for the user to enter their email address
    email_ent = customtkinter.CTkEntry(master=lg_frame, placeholder_text="Enter your Email", width=200, height=20,
                                       bg_color="blue", fg_color="blue")
    email_ent.place(anchor=CENTER, relx=.5, rely=.5)

    # This Entry section is for the user to enter their password
    lg_pass_ent = customtkinter.CTkEntry(master=lg_frame, placeholder_text="Enter Your Password", width=200, height=20,
                                      bg_color="blue", fg_color="blue")
    lg_pass_ent.place(anchor=CENTER, relx=.5, rely=.6)

    # This button is for when the user has input their data and wants to log in
    login_btn = customtkinter.CTkButton(master=lg_frame, width=100, height=50, text="Login", fg_color="blue",
                                        bg_color="blue", command=login_check)
    login_btn.place(anchor=CENTER, relx=.5, rely=.7)

    # This is a forgot log in details for the user to recover their data
    for_btn = customtkinter.CTkButton(master=lg_frame, width=100, height=50, bg_color='blue', fg_color='blue',
                                      text="Forgot Login")
    for_btn.place(anchor=CENTER, relx=.5, rely=.8)

    # This is a back button that returns the user to the main page
    bck_btn = customtkinter.CTkButton(master=lg_frame, width=100, height=50, bg_color='blue', fg_color='blue',
                                      text='BACK', command=lambda: back(main_pg, lg_frame))
    bck_btn.place(anchor=CENTER, relx=.1, rely=.1)


def reg():
    def check():
        try:
            if nm_ent.get() == "":
                CTkMessagebox(title="ERROR", message="Enter your full name")
            elif em_ent.get() == "":
                CTkMessagebox(title="ERROR", message="Enter your email")
            elif pass_ent.get() == "":
                CTkMessagebox(title="ERROR", message="Enter a password")
            elif cpass_ent.get() != pass_ent.get() or cpass_ent.get() == " ":
                CTkMessagebox(title="ERROR", message="Passwords do not match")
            elif acc_type.get() == "Account Type":
                CTkMessagebox(title="ERROR", message="Select account Type")
            else:
                # CTkMessagebox(title="SUCCESS", message="Registration Success")
                name = nm_ent.get()
                mail = em_ent.get()
                pas = pass_ent.get()
                ac_type = acc_type.get()
                file_create(name, mail, pas, ac_type)
                back(main_pg, reg_frame)
        except:
            CTkMessagebox(title="ERR", message="Check the code in try above code line 151 - 163")
            main_pg()
    # registration page

    reg_frame = customtkinter.CTkFrame(master=main)  # creates the registration page
    reg_frame.pack(fill="both", expand=True, padx=10, pady=10)

    reg_img_h = 700  # sizes the images height in the page
    reg_img_w = 1340  # sizes the images width in the page
    reg_img_path = "reg.png"  # Directs to the image path or name in the file
    img3 = customtkinter.CTkImage(Image.open(reg_img_path),
                                  size=(reg_img_w, reg_img_h))  # Imports the image from the path Dir
    lab3 = customtkinter.CTkLabel(master=reg_frame, text=" ", image=img3)  # Places the image onto the page
    lab3.pack(fill="both", expand=True)

    nm_ent = customtkinter.CTkEntry(master=reg_frame, placeholder_text="Enter Your Full Name", width=300, height=2,
                                    fg_color="black")
    nm_ent.place(anchor=CENTER, relx=.5, rely=.3)

    em_ent = customtkinter.CTkEntry(master=reg_frame, placeholder_text="Enter Your Email", width=300, height=2,
                                    fg_color="black")
    em_ent.place(anchor=CENTER, relx=.5, rely=.4)

    pass_ent = customtkinter.CTkEntry(master=reg_frame, placeholder_text="Enter Your Password", width=300, height=2,
                                      fg_color="black")
    pass_ent.place(anchor=CENTER, relx=.5, rely=.5)

    cpass_ent = customtkinter.CTkEntry(master=reg_frame, placeholder_text="Confirm The Password", width=300, height=2,
                                       fg_color="black")
    cpass_ent.place(anchor=CENTER, relx=.5, rely=.6)

    initial = customtkinter.StringVar(value="Account Type")
    acc_type = customtkinter.CTkComboBox(master=reg_frame, values=["Savings", "Money Market", "Fixed Deposit"],
                                         variable=initial)
    acc_type.place(anchor=CENTER, relx=.5, rely=.7)

    reg_btn = customtkinter.CTkButton(master=reg_frame, text="REGISTER", width=100, height=2, bg_color="green",
                                      fg_color="blue", command=check)
    reg_btn.place(anchor=CENTER, relx=.5, rely=.8)

    bck_btn = customtkinter.CTkButton(master=reg_frame, width=100, height=50, bg_color='black', fg_color='blue',
                                      text='BACK', command=lambda: back(main_pg, reg_frame))
    bck_btn.place(anchor=CENTER, relx=.1, rely=.1)


def enter(next_page, frm):
    frm.destroy()
    next_page()


def back(prev_page, val):
    val.destroy()
    prev_page()


# File creation
# This is used in the account creation method to implement the file creation when a file check is done to recognise
# that the name starting the account does not have another account and if so they can create another of a different
# version.

# Create an account
def file_create(name, mail, pas, ac_type):
    try:
        global account
        bal = 0
        account = random.randint(0, 20)
        file_cr = open(str(account)+"-reg.txt", "a+")  # This is the section to hold user data
        file_inf = open(str(account)+"-inf.txt", "a+")  # This file is to hold account information
        file_inf.write(name + "\n")
        file_inf.write(ac_type)
        file_inf.write(" Account Balance : "+str(bal))  # Writes initial user account balance
        # Error begins here where the files are being created but data is not being fetched
        # Start zone
        file_cr.write(name + "\n")  # Writes the users name
        file_cr.write(mail + "\n")  # Writes the users email address
        file_cr.write(pas + "\n")  # Writes the users password
        file_cr.write(ac_type + "\n")  # Writes the users account type
        # Here we close the files that were open
        file_cr.close()
        file_inf.close()
        CTkMessagebox(title="SUCCESS", message=("Success Your Account numbers is " + str(account)), icon="check")
    except:
        CTkMessagebox(title="ERROR", message="Try Again", icon="cancel")


# Check the account information --> (check balance , statement)
# Delete an account  --> (delete account)
# Edit account information --> (deposit , credit)
# Functions
main_pg()
main.mainloop()