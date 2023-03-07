from tkinter import *
from tkinter import messagebox

# functions


def reset():
    E1.delete(0, 'end')
    E2.delete(0, 'end')
    c1.deselect()
    c2.deselect()
    c3.deselect()
    c4.deselect()


def submit():
    user = E1.get().capitalize()
    pwd = E2.get()
    g = val.get()
    lang = []
    lang.append(val1.get())
    lang.append(val2.get())
    lang.append(val3.get())
    lang.append(val4.get())
    data = {"Username": user, "Password": pwd, "Gender": g, "Language": lang}
    try:
        f = open("C:/Project on Github/Tkinter Project/Users.txt", "r")
        old_data = str(f.read())
        if user in old_data:
            messagebox.showerror("Message", "Already Registered")
            f.close()
            return 0
        f.close()
    except:
        pass
    f = open("C:/Project on Github/Tkinter Project/Users.txt", "a")
    f.write(str(data)+"\n")
    f.close()
    f = open("C:/Project on Github/Tkinter Project/Users.txt", 'r')
    messagebox.showinfo("Message", f.read())
    f.close()
    messagebox.showinfo("Message", "Submitted")


win = Tk(className="TkTkTk-Form")
win.geometry("400x400")
win.resizable(0, 0)
# Outer Frame
frame = Frame(win, bg="red", width="400", height="400")
frame.pack(pady=10, padx=10)
frame.pack_propagate(0)
# Registration Label
title = Label(frame, text="Registration Page")
title.pack(pady=20)
# Inner Frames
frame1 = Frame(frame, width="400", height="50")
frame1.pack(padx=10)
frame1.pack_propagate(0)

frame2 = Frame(frame, width="400", height="50")
frame2.pack(padx=10, pady=10)
frame2.pack_propagate(0)

frame3 = Frame(frame, width="400", height="50")
frame3.pack(padx=10)
frame3.pack_propagate(0)

frame4 = Frame(frame, width="400", height="50")
frame4.pack(padx=10, pady=10)
frame4.pack_propagate(0)
# Inner Labels
L1 = Label(frame1, text="Username")
L1.pack(side="left", padx=40)

L2 = Label(frame2, text="Password")
L2.pack(side="left", padx=40)

L3 = Label(frame3, text="Gender")
L3.pack(side="left", padx=40)

L4 = Label(frame4, text="Language")
L4.pack(side="left", padx=40)
# Inner Entries
E1 = Entry(frame1, bd=5)
E1.pack(side="right", padx=40)

E2 = Entry(frame2, bd=5)
E2.pack(side="right", padx=40)
# Radio Button
val = StringVar(frame3, "M")
r1 = Radiobutton(frame3, text="Female", variable=val, value="F")
r1.pack(side="right", padx=25)

r2 = Radiobutton(frame3, text="Male", variable=val, value="M")
r2.pack(side="right")
# Checkbox
val1 = StringVar()
val2 = StringVar()
val3 = StringVar()
val4 = StringVar()
c1 = Checkbutton(frame4, text="Python", variable=val1,
                 onvalue="Python", offvalue="")
c1.pack(side="left")
c2 = Checkbutton(frame4, text="C", variable=val2, onvalue="C", offvalue="")
c2.pack(side="left")
c3 = Checkbutton(frame4, text="Java", variable=val3,
                 onvalue="Java", offvalue="")
c3.pack(side="left")
c4 = Checkbutton(frame4, text="C++", variable=val4, onvalue="C++", offvalue="")
c4.pack(side="left")
# Reset and Submit
Reset = Button(frame, text="Reset", fg="red", command=reset)
Reset.pack(side="left", padx=60)
Submit = Button(frame, text="Submit", fg="red", command=submit)
Submit.pack(side="right", padx=60)

win.mainloop()
