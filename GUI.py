import os
import customtkinter
from tkinter import *
from PIL import Image

customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("Dark")

main = customtkinter.CTk()
main.geometry("850x600")

# Frames
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

login_btn = customtkinter.CTkButton(master=page1, width=100, height=50, bg_color='black', fg_color='brown', text="LOGIN")
login_btn.place(anchor=CENTER, relx=.5, rely=.4)

login_btn = customtkinter.CTkButton(master=page1, width=100, height=50, bg_color='black', fg_color='brown', text="REGISTER")
login_btn.place(anchor=CENTER, relx=.5, rely=.5)

# Functions

main.mainloop()
