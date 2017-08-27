from tkinter import *
import DS_Model_MySQL.DS_Model_backend as backend


def Pain_present_insert_yes_command():
    e1.delete(0, END)
    e1.insert(END, backend.Pain_present_insert_yes())


def Pain_present_insert_no_command():
    e1.delete(0, END)
    e1.insert(END, backend.Pain_present_insert_no())

def add_data_command():
    backend.add_data()
    list1.insert(END, "Model added")

def insertDSModel_command():
    list1.delete(0, END)
    backend.insertDSModel()
    list1.insert(END, "Weights calculated")


def view_command():
    list1.delete(0,END)
    backend.view()
    results = backend.view()
    for result in results["results"]["bindings"]:
        diagnosis=result["Label"]["value"]
        weight = result['DiagnosisWeight']['value']
        diagnosisWeight=diagnosis+ " "+ "[" + weight + "]"
        list1.insert(END,diagnosisWeight)

def clear_command():
    list1.delete(0, END)
    backend.clear()
    list1.insert(END, "Model cleared")


window = Tk()
window.wm_title("Disease Symptom Model")

l1 = Label(window, text="Chief complaint")
l1.grid(row=0, column=0)

l2 = Label(window, text="Data selected")
l2.grid(row=0, column=3)

l3 = Label(window, text="Pain present")
l3.grid(row=1, column=0)

# pain_present_text = StringVar()
e1 = Entry(window, text="")
e1.grid(row=1, column=3)

b1a = Button(window, text="Yes", width=12, command=Pain_present_insert_yes_command)
b1a.grid(row=1, column=1)

b1b = Button(window, text="No", width=12, command=Pain_present_insert_no_command)
b1b.grid(row=1, column=2)

b1c = Button(window, text="Add DS Model", width=14, command=add_data_command)
b1c.grid(row=6, column=3)

b2 = Button(window,width=14,text="Calculate Weights", command=insertDSModel_command)
b2.grid(row=7,column=3)

b3 = Button(window,width=14,text="Get Diagnosis", command=view_command)
b3.grid(row=8,column=3)

b5 = Button(window, text="Clear data", width=14, command=clear_command)
b5.grid(row=9, column=3)

b7 = Button(window, text="Close", width=14, command=window.destroy)
b7.grid(row=10, column=3)

list1 = Listbox(window, height=8, width=40)
list1.grid(row=5, column=0, rowspan=7, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=5, column=2, rowspan=7)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

window.mainloop()
