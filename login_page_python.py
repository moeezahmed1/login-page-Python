from tkinter import *
from tkinter import messagebox

# Function to validate login credentials
def login():
    username=entry1.get()
    password=entry2.get()

    if (username=="" and password==""):
        messagebox.showinfo("", 'Blank Not Allowed')

    elif(username=='Moeez' and password=="admin"):
        messagebox.showinfo("", "Login Success")
    else:
        messagebox.showinfo("", "Incorrect Username Or Password")        

# Main window setup
root=Tk()
root.title("Login")
root.geometry('600x300')

# Try to load custom icon
try:
    image_icon = PhotoImage(file="login.png")
    root.iconphoto(False, image_icon)
except Exception as e:
    print(f"Icon loading error: {e}")


global entry1
global entry2

# GUI elements
Label(root,text='Username').place(x=20,y=20)
Label(root,text='Password').place(x=20,y=70)

entry1=Entry(root,bd=5)
entry1.place(x=140,y=20)

entry2=Entry(root,bd=5)
entry2.place(x=140, y=70)

Button(root,text='Login', command=login,height=3,width=13,bd=6).place(x=100,y=120)

root.mainloop()