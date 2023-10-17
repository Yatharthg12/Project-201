from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.geometry("400x400")
window.configure(bg="lightcyan")

def calculate_interest():
    p = float(principal.get())
    r = float(rate_entry.get())
    t = float(time_entry.get())
    i = (p*r*t)/100
    interest = round(i,2)
    result_label.destroy()

    output_msg = Label(result_frame, text= " Your simple interest is "+str(interest), bg="lightcyan", font=("Calibri",12), width = 42)
    output_msg.place(x=20, y=40)
    output_msg.pack()

heading_label = Label(window, text="Simple Interest Calculator", fg="black", bg="lightcyan", font=("Calibri", 20), bd="5")
heading_label.place(x=50,y=20)
principal = Entry(window, text="", bd=2, width=22)
principal.place(x=150, y=92)

name_label = Label(window, text="Principal Value:", fg="black",bg="lightcyan",bd=1,font=("Calibri",12))
name_label.place(x=20,y=90)

rate = Label(window, text= "Enter Interest Rate:", fg="black",bg="lightcyan",font=("Calibri",12))
rate.place(x=20,y=140)
rate_entry = Entry(window, text="", bd=2, width=15)
rate_entry.place(x=190,y=142)

time = Label(window, text= "Enter Time:", fg="black",bg="lightcyan",font=("Calibri",12))
time.place(x=20,y=185)
time_entry = Entry(window, text="", bd=2, width=15)
time_entry.place(x=170,y=187)

calc_button = Button(window, text="Calculate", fg="black", bg="cyan", bd=4, command=calculate_interest)
calc_button.place(x=20, y=250)

result_frame = LabelFrame(window, text="Result", bg="lightcyan", font=("Calibri",12), width=33)
result_frame.pack(padx=20,pady=20)
result_frame.place(x=20, y=300)

result_label = Label(result_frame, text="", bg="lightcyan",font=("Calibri",12),width=33)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()