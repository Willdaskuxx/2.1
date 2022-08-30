from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


# Designing window for registration

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("644x788")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command=register_user).pack()


# Designing window for login

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("644x788")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


# Implementing event on register button

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_all).pack()


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_login_screen():
    login_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


def delete_main_account_screen():
    main_screen.destroy()


def delete_all():
    login_success_screen.destroy()
    delete_login_screen()
    delete_main_account_screen()

    def newFile():
        global file
        root.title("Untitled - Notepad")
        file = None
        TextArea.delete(1.0, END)

    def openFile():
        global file
        file = askopenfilename(defaultextension=".txt",
                               filetypes=[("All Files", "*.*"),
                                          ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            root.title(os.path.basename(file) + " - Notepad")
            TextArea.delete(1.0, END)
            f = open(file, "r")
            TextArea.insert(1.0, f.read())
            f.close()

    def saveFile():
        global file
        if file == None:
            file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                     filetypes=[("All Files", "*.*"),
                                                ("Text Documents", "*.txt")])
            if file == "":
                file = None

            else:
                # Save as a new file
                f = open(file, "w")
                f.write(TextArea.get(1.0, END))
                f.close()

                root.title(os.path.basename(file) + " - Notepad")
                print("File Saved")
        else:
            # Save the file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

    def quitApp():
        root.destroy()

    def cut():
        TextArea.event_generate(("<>"))

    def copy():
        TextArea.event_generate(("<>"))

    def paste():
        TextArea.event_generate(("<>"))

    def about():
        showinfo("Notepad", "Made by William Tinnock-Jones")

    if __name__ == '__main__':
        # Basic tkinter setup
        root = Tk()
        root.title("Untitled - Notepad")
        root.geometry("644x788")

        # Add TextArea
        TextArea = Text(root, font="lucida 13")
        file = None
        TextArea.pack(expand=True, fill=BOTH)

        # tkinter menubar
        MenuBar = Menu(root)

        # File Menu
        FileMenu = Menu(MenuBar, tearoff=0)
        # open new file
        FileMenu.add_command(label="New", command=newFile)

        # Open existing file
        FileMenu.add_command(label="Open", command=openFile)

        # save current file

        FileMenu.add_command(label="Save", command=saveFile)
        FileMenu.add_separator()
        FileMenu.add_command(label="Exit", command=quitApp)
        MenuBar.add_cascade(label="File", menu=FileMenu)
        # File Menu done

        # Edit Menu
        EditMenu = Menu(MenuBar, tearoff=0)
        # cut, copy paste
        EditMenu.add_command(label="Cut", command=cut)
        EditMenu.add_command(label="Copy", command=copy)
        EditMenu.add_command(label="Paste", command=paste)

        MenuBar.add_cascade(label="Edit", menu=EditMenu)
        # Edit Menu done

        # Help Menu
        HelpMenu = Menu(MenuBar, tearoff=0)
        HelpMenu.add_command(label="About Notepad", command=about)
        MenuBar.add_cascade(label="Help", menu=HelpMenu)
        # Help Menu done

        root.config(menu=MenuBar)

        # Scrollbar
        Scroll = Scrollbar(TextArea)
        Scroll.pack(side=RIGHT, fill=Y)
        Scroll.config(command=TextArea.yview)
        TextArea.config(yscrollcommand=Scroll.set)

        root.mainloop()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("644x788")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()


main_account_screen()