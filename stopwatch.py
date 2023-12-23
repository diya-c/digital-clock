import tkinter as Tkinter
from datetime import datetime
from PIL import Image, ImageTk

counter = 0
running = False


def counter_label(label):
    def count():
        if running:
            global counter 
            if counter == 0:
                display = 'Ready!'
            else:
                tt = datetime.utcfromtimestamp(counter)
                string = tt.strftime('%H:%M:%S')
                display = string

            label['text'] = display
            label.after(1000, count)
            counter += 1 
    count()

def Start(label):
    global running
    running = True
    counter_label(label)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'

def Stop():
    global running
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    running = False


def Reset(label):
	global counter
	counter = 0
	if not running:
		reset['state'] = 'disabled'
		label['text'] = '00:00:00'
	else:
		label['text'] = '00:00:00'


root = Tkinter.Tk()
root.title("Stopwatch")

root.geometry('350x250')

sw_img = Image.open(r"C:\Users\user\Desktop\mini project\green3.jpeg")
test2 = ImageTk.PhotoImage(sw_img)
sw_label = Tkinter.Label(image=test2)
sw_label.image = test2
# Position image
sw_label.pack()



start = Tkinter.Button(root, text='Start', width=6, command=lambda: Start(label),font=('Verdana 30',13))
stop = Tkinter.Button(root, text='Stop', width=6, state='disabled', command=Stop,font=('Verdana 30',13))
reset = Tkinter.Button(root, text='Reset', width=6, state='disabled', command=lambda: Reset(label),font=('Verdana 30',13))
start.place(x=105, y=180, anchor='center')
stop.place(x=175, y=180, anchor='center')
reset.place(x=245, y=180, anchor='center')
label = Tkinter.Label(root, text='00:00:00', fg='black', font='Verdana 31 bold')
label.place(x=175, y=85, anchor='center')
root.mainloop()