from tkinter import *
import time

root = Tk()
root.title("Clock")
root.geometry("600x400")

def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    seconds = time.strftime("%S")
    day = time.strftime("%A")
    noon = time.strftime("%p")
    date = time.strftime("%x")
    time_zone = time.strftime("%Z")
    my_label.config(text = "Time: "+hour+ ":" +minute+ ":" +seconds+" "+noon)
    my_label.after(1000,clock)
    my_label2.config(text = "Day: "+day+" "+date)
    my_label3.config(text = "Timezone: "+time_zone)

my_label = Label(root,text = " ",font = ("Times 20 italic bold",48),fg = "red",bg = "green")
my_label.pack(pady = 20)

my_label2 = Label(root,text = " ",font = ("Times 20 italic bold",24))
my_label2.pack(pady = 10)

my_label3 = Label(root,text = " ",font = ("Times 20 italic bold",24))
my_label3.pack(pady = 10)

clock()

root.mainloop()