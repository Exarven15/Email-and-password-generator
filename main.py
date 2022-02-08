from random import *
from tkinter import *
import string
from random import *


#generation of random mdp 
def generate_pass():
    password_min = 8
    password_max = 15
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars)
                       for x in range(randint(password_min, password_max)))
    pass_entry.delete(0, END)
    pass_entry.insert(0, password)
    with open("email&pass-list.txt", "a+") as file:
        for passwords in password : 
            file.write(passwords )
        file.write("\n")
        file.close()

#generation of random email
def generate_email():
    generate_min = 4
    generate_max = 16
    mail = "@gmail.com"
    all_chars = string.ascii_letters + string.digits
    email = "".join(choice(all_chars)
                    for x in range(randint(generate_min, generate_max)))
    for z in email :
        email += mail 
        break
    email_entry.delete(0, END)
    email_entry.insert(0, email)
    with open("email&pass-list.txt", "a+") as file:
        for mailz in email : 
            file.write(mailz )
        file.write("\n")
        file.close()
        
root = Tk()
root.title("Email and Password generator")
root.geometry("700x300")
root.config(bg="lightgreen")

label1 = Label(root, text="Email ", font="Poppins 20", bg="lightgreen", fg="#151515")
label1.grid(row=0, column=0, pady=25)

label2 = Label(root, text="Password", font="Poppins 20", bg="lightgreen", fg="#151515")
label2.grid(row=0, column=1, pady=25)

pass_entry = Entry(root, font="Poppins 18", fg="#151515", width=18)
pass_entry.grid(row=1, column=1,padx=10, pady=10)

email_entry = Entry(root, font="Poppins 18", fg="#151515", width=26)
email_entry.grid(row=1, column=0,padx=50, pady=10 )

email_bttn = Button(root, text="Generate Email", font="Poppins 18", fg="#151515", command=generate_email)
email_bttn.grid(row=2, column=0,padx=50, pady=10)

pass_bttn = Button(root, text="Generate Password", font="Poppins 18", fg="#151515", command=generate_pass)
pass_bttn.grid(row=2, column=1,padx=10, pady=10)

root.mainloop()