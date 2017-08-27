from tkinter import *
import BrCa_backend


def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[0])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[1])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[2])


def view_command():
    list1.delete(0, END)
    for row in BrCa_backend.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in BrCa_backend.search(patientid_text.get(), patient_name_text.get(), birth_year_text.get()):
        list1.insert(END, row)


def update_command():
    BrCa_backend.update(patient_name_text.get(), birth_year_text.get(), patientid_text.get())
    list1.delete(0, END)


def delete_command():
    BrCa_backend.delete(patientid_text.get())
    list1.delete(0, END)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)


window = Tk()
window.wm_title("Nottingham BrCa Patient Management")

l1 = Label(window, text="Patient ID")
l1.grid(row=0, column=0)

l2 = Label(window, text="Patient name")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year of birth")
l3.grid(row=1, column=0)

patientid_text = StringVar()
e1 = Entry(window, text=patientid_text)
e1.grid(row=0, column=1)

patient_name_text = StringVar()
e2 = Entry(window, text=patient_name_text)
e2.grid(row=0, column=3)

birth_year_text = StringVar()
e3 = Entry(window, text=birth_year_text)
e3.grid(row=1, column=1)

list1 = Listbox(window, height=8, width=35)
list1.grid(row=2, column=0, rowspan=7, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Update selected", width=12, command=update_command)
b3.grid(row=5, column=3)

b4 = Button(window, text="Delete selected", width=12, command=delete_command)
b4.grid(row=6, column=3)

b5 = Button(window, text="Close", width=12, command=window.destroy)
b5.grid(row=7, column=3)

window.mainloop()
