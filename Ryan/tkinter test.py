from tkinter import *

def welcome():
    name = text_box1.get(1.0, END)
    text_box2.delete(1.0, END)
    text_box2.insert(END, "Welcome " + name)

root = TK()
root.geometry("300x300")
frame = Frame(root)
frame.pack()

label = Label(frame, text="Enter your name:")
label.pack()

text_box1 = Text(frame, height=1, width=20)
text_box1.pack()

button = Button(frame, text="Welcome", command=welcome)
button.pack()

text_box2 = Text(frame, height=1, width=20)
text_box2.congig(font("Arial", 20))
text_box2.pack()

root.mainloop()