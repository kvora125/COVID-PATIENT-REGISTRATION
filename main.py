from tkinter import *
import tkinter.messagebox
import os

if os.path.exists("patients_records.txt"):
    print("file loaded")
else:
    print("file created")
    file = open("patients_records.txt", 'a')
    header = file.write("First_Name;Last_Name;Address;Date_of_Birth;Admitted_On;Quarantine_Duration;DischargeStatus\n")
    file.close()


def data_save():
    print("saving data")
    file1 = open("patients_records.txt", 'a')
    status.set("saving data")
    record = e1.get() + ";" + e2.get() + ";" + e3.get() + ";" + e4.get() + ";" + e5.get() + ";" + e6.get() + ";"
    record = record + discharge_status.get() + "\n"
    write = file1.write(record)
    print(write)
    tkinter.messagebox.showinfo("Status", "Record saved")
    status.set("data saved and ready for new entry")
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    discharge.deselect()


window = Tk()
window.title("Covid Patients Registration")
window.geometry("800x250")
window.config(bg="black")
menu = Menu(window)
options = Menu(menu, tearoff=0)
options.add_command(label="see records", command=lambda: os.system('patients_records.txt'))
options.add_command(label="credits", command=lambda: tkinter.messagebox.showinfo("Credits", "Developed by Keval Vora "
                                                                                            "(kvora125)"))
options.add_separator()
options.add_command(label="exit", command=window.quit)
menu.add_cascade(label="options", menu=options)
window.config(menu=menu)
frame1 = Frame(window, bg="grey", width=800, height=200)
frame1.pack(side=TOP)
inp1 = Label(frame1, text="Covid Patient : Form")
inp1.grid(row=0, column=1)
inp2 = Label(frame1, text="First Name")
inp2.grid(row=1, column=1)
global e1
e1 = Entry(frame1, width=40, borderwidth=5)
e1.grid(row=1, column=2)
inp4 = Label(frame1, bg="grey", text="         ")
inp4.grid(row=1, column=3)
inp5 = Label(frame1, text="Last Name")
inp5.grid(row=1, column=4)
inp6 = Label(frame1, bg="grey", text="   ")
inp6.grid(row=1, column=5)
global e2
e2 = Entry(frame1, width=40, borderwidth=5)
e2.grid(row=1, column=6)
inp7 = Label(frame1, bg="grey", text="         ")
inp7.grid(row=2, column=1)
inp8 = Label(frame1, text="Address")
inp8.grid(row=3, column=1)
global e3
e3 = Entry(frame1, width=40, borderwidth=5)
e3.grid(row=3, column=2)
inp9 = Label(frame1, bg="grey", text="         ")
inp9.grid(row=3, column=3)
inp10 = Label(frame1, text="Date of Birth")
inp10.grid(row=3, column=4)
inp11 = Label(frame1, bg="grey", text="   ")
inp11.grid(row=3, column=5)
global e4
e4 = Entry(frame1, width=40, borderwidth=5)
e4.grid(row=3, column=6)
inp12 = Label(frame1, bg="grey", text="         ")
inp12.grid(row=4, column=1)
inp13 = Label(frame1, text="Admitted On")
inp13.grid(row=5, column=1)
global e5
e5 = Entry(frame1, width=40, borderwidth=5)
e5.grid(row=5, column=2)
inp14 = Label(frame1, bg="grey", text="         ")
inp14.grid(row=5, column=3)
inp15 = Label(frame1, text="Quarantine Duration")
inp15.grid(row=5, column=4)
inp16 = Label(frame1, bg="grey", text="   ")
inp16.grid(row=5, column=5)
global e6
e6 = Entry(frame1, width=40, borderwidth=5)
e6.grid(row=5, column=6)
global discharge_status
discharge_status = StringVar()
global discharge
discharge = Checkbutton(frame1, text="Patient Discharged", onvalue="discharged", offvalue="pending",
                        variable=discharge_status)
discharge.deselect()
discharge.grid(row=7, column=2)
button1 = Button(frame1, text="Submit", bg="white", activebackground="green", command=data_save, font=("bold", 12))
button1.grid(row=10, column=3)
inp17 = Label(frame1, bg="grey", text="         ")
inp17.grid(row=6, column=1)
inp18 = Label(frame1, bg="grey", text="         ")
inp18.grid(row=7, column=1)
status = StringVar()
status.set("ready")
label1 = Label(window, textvariable=status, bg="green", fg="white", font=("bold", 12), width=12)
label1.pack(side=BOTTOM, fill=X, expand=True)
window.mainloop()
