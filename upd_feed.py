import asyncio
import customtkinter
from customtkinter import filedialog
import os, shutil

from feeds import Eprice, KaufLand, Allegro

if os.path.isfile("updated.xlsx"):
    pass
else:
    raise Exception("YOU NEED TO RUN >> upd_origin script >> TO ALLOW THIS SCRIPT BE EXECUTABLE")

async def price(rate, revenue, url):
    if "eprice" in url:
        Eprice.eprice(rate, revenue, url)       
    elif "kaufland" in url:
        KaufLand.kaufland(rate, revenue)
    elif "alegro" in url:
        Allegro.allegro(rate, revenue, url)


customtkinter.set_appearance_mode("light")

customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.title("Update Feed")
root.geometry('440x500+666+180')


def openFile():
    fileroot = filedialog.askopenfilename()

    with open("filepath.txt", "w") as file:
        if isinstance(fileroot, str):
            file.write(fileroot)
    shutil.copyfile(fileroot, f"{os.getcwd()}/{fileroot.split('/')[-1]}")
    

def crawl():
    operation = "crawl"
    with open("operation.txt", "w") as file:
        file.write(operation)

def convert_price():
    operation = "price"
    with open("operation.txt", "w") as file:
        file.write(operation)

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=15, padx=15, fill="both", expand=True)

title = customtkinter.CTkLabel(master=frame, text="MARKET PRODUCT CONVERTOR")
title.pack(pady=15, padx=15)

label = customtkinter.CTkLabel(master=frame, text="Choose File")
label.place(x=80, y=55)

button2 = customtkinter.CTkButton(master=frame, text="Open", command=openFile)
button2.place(x=215, y=55)


label2 = customtkinter.CTkLabel(master=frame, text="Select a task")
label2.place(x=80, y=125)

checkbox1 = customtkinter.CTkCheckBox(master=frame, text="Crawling", command=crawl)
checkbox1.place(x=215, y=105)

checkbox2 = customtkinter.CTkCheckBox(master=frame, text="Price convert", command=convert_price)
checkbox2.place(x=215, y=145)

label3 = customtkinter.CTkLabel(master=frame, text="Enter conversion rate")
label3.place(x=135, y=185)

label4 = customtkinter.CTkLabel(master=frame, text="1 Kč:")
label4.place(x=80, y=225)

def convert(name):
    vara = entry.get()
    with open("currency.txt", "w") as file:
        file.write(str(vara))

entry = customtkinter.CTkEntry(master=frame, placeholder_text=" ", width=55)
entry.place(x=135, y=225)


clicked = customtkinter.StringVar()

drop = customtkinter.CTkOptionMenu(master=frame, values=["Select currency","EUR", "PLN", "USD", "RON"], command=convert)
drop.place(x=215, y=225)

label5 = customtkinter.CTkLabel(master=frame, text="Cost Adjustment")
label5.place(x=135, y=275)

label6 = customtkinter.CTkLabel(master=frame, text="X     = ")
label6.place(x=80, y=305)

entry3 = customtkinter.CTkEntry(master=frame, placeholder_text=" ", width=55)
entry3.place(x=135, y=305)

label7 = customtkinter.CTkLabel(master=frame, text="%")
label7.place(x=215, y=305)

variance = entry3.get()

def sub():
    with open("filepath.txt", "r") as file:
        fi = file.read()
    with open("operation.txt", "r") as file:
        op = file.read()
    with open("currency.txt", "r") as file:
        curr = file.read()
    revenue = (1 + int(entry3.get()) / 100)
    new_file = fi.split('/')[-1]
    currency = drop.get()
    if op == "price":
        print("[INFO] PLEASE WAIT, FILE IS BEING CONVERTED")
        asyncio.run(price(curr, revenue, f"{os.getcwd()}/{new_file}"))
    os.remove("currency.txt")
    os.remove("filepath.txt")
    os.remove("operation.txt")
    os.remove(f"{new_file}")
    print("[INFO] COMPLETED")
    root.destroy()
    


submit = customtkinter.CTkButton(master=frame, text="SUBMIT", command=sub)
submit.place(x=135, y=375)


root.mainloop()

