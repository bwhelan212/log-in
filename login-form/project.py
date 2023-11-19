from tkinter import *
from tkinter import messagebox
from tkmacosx import Button

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg = "#fff")
root.resizable(False,False)
def sign_in():
    username = user_field.get()
    password = pass_field.get()
    
    if username == 'admin' and password == '1234':
        screen = Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg = "white")
        
        Label(screen , text = 'Hello', bg = "#fff", fg = 'black', font = ('Avenir', 50, 'bold')).pack(expand = True)
    
        screen.mainloop()
    elif username != 'admin' and password != '1234':
        messagebox.showerror("Invalid","invalid user and password")
    elif password != '1234':
        messagebox.showerror("Invalid","invalid user and password")
    elif username != 'admin':
        messagebox.showerror("invalid", "invalid username" )
    
        

frame = Frame(root, width = 350, height = 350, bg = "white")
frame.place(x=480, y=70)

heading = Label(frame,text = 'Sign in', fg = '#57a1f8', bg = "white", font =('Avenir', 23, 'bold'))
heading.place(x = 100, y=5)

def user_enter(e):
    user_field.delete(0, 'end')

def user_exit(e):
    name = user_field.get()
    if name == '':
        user_field.insert(0, 'Username')
        
user_field = Entry(frame, width = 25, fg = 'black', border = 0, bg = "white", font =('Avenir', 11, 'bold'))
user_field.place(x=30,y=80)
user_field.insert(0,'Username')
user_field.bind('<FocusIn>', user_enter)
user_field.bind('<FocusOut>', user_exit)
Frame(frame, width = 295, height = 2, bg = 'black').place(x=25,y=107)

def pass_enter(e):
    pass_field.delete(0, 'end')

def pass_exit(e):
    name = pass_field.get()
    if name == '':
        pass_field.insert(0, 'Username')
## FIX SIGN IN AND SIGN UP
pass_field = Entry(frame, width = 25, fg = 'black', border = 0, bg = "white", font =('Avenir', 11, 'bold'))
pass_field.place(x=30,y=150)
pass_field.insert(0,'Password')
pass_field.bind('<FocusIn>', pass_enter)
pass_field.bind('<FocusOut>', pass_exit)
Frame(frame, width = 295, height = 2, bg = 'black').place(x=25,y=177)

Button(frame, width = 275, pady = 7, text = 'Sign in', bg = '#57a1f8', fg = 'white', border = 0, command = sign_in).place(x=35, y=204)
no_account = Label(frame, text = "Don't have an account?", fg = 'black', bg = 'white', font =('Avenir',9))
no_account.place(x=75, y = 270)

sign_up = Button(frame,width = 100, text = 'Sign up', border = 0, bg = 'white', cursor = 'hand', fg = '#57a1f8')
sign_up.place(x = 215, y = 270)
root.mainloop()