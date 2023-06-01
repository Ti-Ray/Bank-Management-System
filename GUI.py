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
# def callback(url):
#     webbrowser.open_new_tab(url)
#
# # Frames
# # main page when the app is started
# page1 = customtkinter.CTkFrame(master=main, width=500, height=500)  # This is frame holds login or register buttons
# page1.pack(fill="both", expand=True, padx=10, pady=10)
# # page1.place(anchor="c", relx=.5, rely=.5)
#
# # Objects
# img1_h = 1400
# img1_w = 1400
# img1_path = "im1.png"
# pg1img = customtkinter.CTkImage(light_image=Image.open(img1_path), size=(img1_w, img1_h))
# lab = customtkinter.CTkLabel(master=page1, image=pg1img, text=" ")
# lab.pack(fill="both", expand=True, padx=10, pady=10)
#
# login_btn = customtkinter.CTkButton(master=page1, width=100, height=50, bg_color='black', fg_color='brown', text="LOGIN")
# login_btn.place(anchor=CENTER, relx=.5, rely=.4)
#
# login_btn = customtkinter.CTkButton(master=page1, width=100, height=50, bg_color='black', fg_color='brown', text="REGISTER")
# login_btn.place(anchor=CENTER, relx=.5, rely=.5)
#
#
# about_link = customtkinter.CTkButton(master=page1, text="About us", bg_color="black", fg_color="brown", width=100, height=50)
# about_link.place(anchor=CENTER, relx=.5, rely=.6)
# about_link.bind("<Button-1>", lambda e: callback("https://www.youtube.com/"))

# start from here

# Login page Happens when the login button is pressed
# lg_frame = customtkinter.CTkFrame(master=main)
# lg_frame.pack(fill="both", expand=True, padx=10, pady=10)
#
# img2_h = 900
# img2_w = 1400
# img2_path = "login.png"
# img2 = customtkinter.CTkImage(light_image=Image.open(img2_path), size=(img2_w, img2_h))
# lab2 = customtkinter.CTkLabel(master=lg_frame, text=" ", image=img2)
# lab2.pack(fill="both", expand=True)
#
# email_ent = customtkinter.CTkEntry(master=lg_frame, placeholder_text="Enter your Email", width=200, height=2,
#                                    bg_color="blue", fg_color="blue")
# email_ent.place(anchor=CENTER, relx=.5, rely=.5)
#
# pass_ent = customtkinter.CTkEntry(master=lg_frame, placeholder_text="Enter Your Password", width=200, height=2,
#                                   bg_color="blue", fg_color="blue")
# pass_ent.place(anchor=CENTER, relx=.5, rely=.6)
#
# for_btn = customtkinter.CTkButton(master=lg_frame, text="Forgot login", width=200, height=2,
#                                   bg_color="blue", fg_color="blue")
# for_btn.place(anchor=CENTER, relx=.5, rely=.7)

# start from here

# registration page


# Functions

main.mainloop()
