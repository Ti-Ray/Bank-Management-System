# # POINTS TO REMEMBER
# - Remember to change the about us link
# - Remember to comment properly and define clearly

import os
import webbrowser

import customtkinter
from tkinter import *
from PIL import Image

customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("Dark")

main = customtkinter.CTk()
main.geometry("850x600")


#
# # Frames
# def login_get():
#     page1.destroy()
def main_pg():
    def reg_get():
        page1.destroy()
        reg()

    def login_get():
        page1.destroy()
        login()

    # # main page when the app is started
    def callback(url):
        webbrowser.open_new_tab(url)
    page1 = customtkinter.CTkFrame(master=main, width=500, height=500)  # This is frame holds login or register buttons
    page1.pack(fill="both", expand=True, padx=10, pady=10)
    # page1.place(anchor="c", relx=.5, rely=.5)

    # Objects
    img1_h = 1400
    img1_w = 1400
    img1_path = "im1.png"
    pg1img = customtkinter.CTkImage(light_image=Image.open(img1_path), size=(img1_w, img1_h))
    lab = customtkinter.CTkLabel(master=page1, image=pg1img, text=" ")
    lab.pack(fill="both", expand=True, padx=10, pady=10)

    login_btn = customtkinter.CTkButton(master=page1, width=100, height=50, bg_color='black', fg_color='brown',
                                        text="LOGIN", command=login_get)
    login_btn.place(anchor=CENTER, relx=.5, rely=.4)

    login_btn = customtkinter.CTkButton(master=page1, width=100, height=50, bg_color='black', fg_color='brown',
                                        text="REGISTER", command=reg_get)
    login_btn.place(anchor=CENTER, relx=.5, rely=.5)

    about_link = customtkinter.CTkButton(master=page1, text="About us", bg_color="black", fg_color="brown", width=100,
                                         height=50)
    about_link.place(anchor=CENTER, relx=.5, rely=.6)
    about_link.bind("<Button-1>", lambda e: callback("https://www.youtube.com/"))

# start from here


def login():
    def bck_log():
        lg_frame.destroy()
        main_pg()
    # Login page Happens when the login button is pressed

    lg_frame = customtkinter.CTkFrame(master=main)
    lg_frame.pack(fill="both", expand=True, padx=10, pady=10)

    img2_h = 900
    img2_w = 1400
    img2_path = "login.png"
    img2 = customtkinter.CTkImage(light_image=Image.open(img2_path), size=(img2_w, img2_h))
    lab2 = customtkinter.CTkLabel(master=lg_frame, text=" ", image=img2)
    lab2.pack(fill="both", expand=True)

    email_ent = customtkinter.CTkEntry(master=lg_frame, placeholder_text="Enter your Email", width=200, height=2,
                                       bg_color="blue", fg_color="blue")
    email_ent.place(anchor=CENTER, relx=.5, rely=.5)

    pass_ent = customtkinter.CTkEntry(master=lg_frame, placeholder_text="Enter Your Password", width=200, height=2,
                                      bg_color="blue", fg_color="blue")
    pass_ent.place(anchor=CENTER, relx=.5, rely=.6)

    for_btn = customtkinter.CTkButton(master=lg_frame, text="Forgot login", width=200, height=2,
                                      bg_color="blue", fg_color="blue")
    for_btn.place(anchor=CENTER, relx=.5, rely=.7)

    bck_btn = customtkinter.CTkButton(master=lg_frame, width=100, height=50, bg_color='blue', fg_color='blue',
                                      text='BACK', command=bck_log)
    bck_btn.place(anchor=CENTER, relx=.1, rely=.1)

# start from here


def reg():
    def bck_reg():
        reg_frame.destroy()
        main_pg()
    # registration page

    reg_frame = customtkinter.CTkFrame(master=main)  # creates the registration page
    reg_frame.pack(fill="both", expand=True, padx=10, pady=10)

    regimg_h = 700  # sizes the images height in the page
    regimg_w = 1340  # sizes the images width in the page
    regimg_path = "reg.png"  # Directs to the image path or name in the file
    img3 = customtkinter.CTkImage(Image.open(regimg_path),
                                  size=(regimg_w, regimg_h))  # Imports the image from the path Dir
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
                                      fg_color="blue")
    reg_btn.place(anchor=CENTER, relx=.5, rely=.8)

    bck_btn = customtkinter.CTkButton(master=reg_frame, width=100, height=50, bg_color='black', fg_color='blue',
                                      text='BACK', command=bck_reg)
    bck_btn.place(anchor=CENTER, relx=.1, rely=.1)


# Functions
main_pg()
main.mainloop()
