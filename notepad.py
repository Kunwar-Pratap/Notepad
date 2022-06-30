from tkinter import *
import os
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo
import tkinter.messagebox as tmsg

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    textArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " -Notepad")
        textArea.delete(1.0, END)
        fl = open(file, "r")
        textArea.insert(1.0, fl.read())
        fl.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Document", "*.txt")])
        if file == "":
            file = None
        else:
            fl = open(file, "w")
            fl.write(textArea.get(1.0, END))
            fl.close()
            root.title(os.path.basename(file) + " -Notepad")
    else:
        fl = open(file, "w")
        fl.write(textArea.get(1.0, END))
        fl.close()

def exitApp():
    root.destroy()

def cut():
    textArea.event_generate("<<Cut>>")

def copy():
    textArea.event_generate("<<Copy>>")

def paste():
    textArea.event_generate("<<Paste>>")

def aboutApp():
    showinfo("Notepad - 1.0.0.1", "This is Notepad version 1.0.0.1\nThanks for using this app")

def aboutDev():
    showinfo("About Developer", "This Notepad has Developed by Kunwar Pratap")

def rateUs():
    rate = tmsg.askquestion("Rate Us", "You used this app...Was your experience good?")
    if rate == "yes":
        message = "Great...Please Rate us on Appstore"
    else:
        message = "Tell us what happened with using this app?\nWe will contact you shortly."
    tmsg.showinfo("Experience", message)

def helpApp():
    showinfo("Help", "We will contact you shortly.")

if __name__ == '__main__':
    root = Tk()
    root.geometry("590x850")
    root.title("Untitled - Notepad")
    # root.wm_iconbitmap("notepad-3.ico")

    textArea = Text(root, font="georgia 14")
    file = None
    textArea.pack(expand=True, fill=BOTH)

    mainMenu = Menu(root)
    fileMenu = Menu(mainMenu, tearoff=0, bg="sky blue", font="ubuntu 11", fg="dark blue")
    fileMenu.add_command(label="New", command=newFile)
    fileMenu.add_command(label="Open", command=openFile)
    fileMenu.add_command(label="Save", command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=exitApp)
    mainMenu.add_cascade(label="File", menu=fileMenu)

    editMenu = Menu(mainMenu, tearoff=0, bg="sky blue", font="ubuntu 11", fg="dark blue")
    editMenu.add_command(label="Cut", command=cut)
    editMenu.add_command(label="Copy", command=copy)
    editMenu.add_command(label="Paste", command=paste)
    mainMenu.add_cascade(label="Edit", menu=editMenu)

    helpMenu = Menu(mainMenu, tearoff=0, bg="sky blue", font="ubuntu 11", fg="dark blue")
    helpMenu.add_command(label="About App", command=aboutApp)
    helpMenu.add_command(label="About Developer", command=aboutDev)
    helpMenu.add_command(label="Rate Us", command=rateUs)
    helpMenu.add_separator()
    helpMenu.add_command(label="Help", command=helpApp)
    mainMenu.add_cascade(menu=helpMenu, label="Help")
    root.config(menu=mainMenu)

    scrollBar = Scrollbar(textArea)
    scrollBar.pack(side=RIGHT, fill=Y)
    textArea.config(yscrollcommand=scrollBar.set)
    scrollBar.config(command=textArea.yview)

    statusBar = StringVar()
    statusBar.set("Notepad V 1.0.0.1")
    sBar = Label(root, textvariable=statusBar, anchor=N, relief=SUNKEN, bg="sky blue",  font="ubuntu 11", fg="dark blue")
    sBar.pack(fill=X, side=BOTTOM)

    root.mainloop()