from tkinter import *
from tkinter import messagebox
from random import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generatePassword():
    numbers= list(map(chr,range(48,58)))
    alphabets=list(map(chr,range(65,91))) +list(map(chr,range(97,123)))
    symbols=["!",'#','$','%','&','(',')','*','+']

    passwordLetters=[choice(alphabets) for _ in range(randint(6,9))]
    passwordNumbers=[choice(numbers) for _ in range(randint(3,5))]
    passwordSymbols=[choice(symbols) for _ in range(randint(2,5))]

    passwordList=passwordLetters+passwordNumbers+passwordSymbols
    shuffle(passwordList)
    passwordList= "".join(passwordList)
    passwordEntry.insert(0,passwordList)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if len(websiteEntry.get())==0 or len(passwordEntry.get())==0:
        messagebox.showwarning(title="Insufficient Data", message="Make sure you have Entried all the fields")
        return
    if messagebox.askokcancel(title="Details confirmation", message=f"Here are the details you have entered \nWebsite:   {websiteEntry.get()} \nUsername: {usernameEntry.get()} \nPassword: {passwordEntry.get()} \n\nDo you want to proceed?\n"):
        with open("pass.txt","a") as file:
            file.write(f"{websiteEntry.get()} | {usernameEntry.get()} | {passwordEntry.get()}\n")
            websiteEntry.delete(0,END)
            passwordEntry.delete(0,END)

# ---------------------------- UI SETUP -------------------------------
root=Tk()
root.title("Password Manager")
root.config(padx=50,pady=50)


canvas=Canvas(height=200,width=200)
photo=PhotoImage(file="logo.png")
canvas.create_image(100,80,image=photo)
canvas.grid(row=0,column=1,sticky="w")

website=Label(text="Website:")
website.grid(row=1,column=0)
websiteEntry=Entry(width=40)
websiteEntry.grid(row=1,column=1, columnspan=2, sticky="w")
websiteEntry.focus()

username=Label(text="Email/Username:")
username.grid(row=2,column=0)
usernameEntry=Entry(width=40)
usernameEntry.grid(row=2,column=1,sticky="w")
usernameEntry.insert(0,"yodhangowda328@gmail.com")

password=Label(text="Password:")
password.grid(row=3,column=0)
passwordEntry=Entry(width=21)
passwordEntry.grid(row=3,column=1, sticky="w")

btn1=Button(text="Generate Password", command=generatePassword)
btn1.grid(row=3,column=1,sticky="e")

addBtn=Button(text="Add", width=33, command=save)
addBtn.grid(row=4,column=1,columnspan=2,sticky="w")

root.mainloop()