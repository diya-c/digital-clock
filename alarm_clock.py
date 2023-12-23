import time
import tkinter as tk
import webbrowser
from tkinter import messagebox
from win10toast import ToastNotifier
from PIL import Image, ImageTk


def set_alarm():
    try:
        hour = int(hour_entry.get())
        minute = int(minute_entry.get())
        url=str(url_entry.get())
        if 0 <= hour  and hour <= 23 and 0 <= minute and minute <= 59:
            alarm_time = time.strptime(f"{hour}:{minute}", "%H:%M")
                
            while True:
                current_time = time.localtime()
                if current_time[3]==alarm_time[3] and current_time[4]==alarm_time[4]:
                    # sample url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 
                    webbrowser.open(url)
                    toast = ToastNotifier()
                    toast.show_toast("Alarm", " Alarm Time! ", duration=10)
                    break
                time.sleep(1) # Check every second
        else:
            messagebox.showerror("Error", "Invalid Time")
    except ValueError:
        messagebox.showerror("Error", "Invalid Input")

root = tk.Tk()
root.title("Alarm Clock")
root.geometry('400x300')

alrm_img = Image.open("C:\\Users\\user\\Desktop\\mini project\\green1.jpg")
test1 = ImageTk.PhotoImage(alrm_img)
alrm_label = tk.Label(image=test1)
alrm_label.image = test1
alrm_label.pack()

hour_entry = tk.Entry(root, width=5,font=("Helvetica", 16))
hour_entry.place(x=133, y=70, anchor='center')


minute_entry = tk.Entry(root, width=5, font=("Helvetica", 16))
minute_entry.place(x=266, y=70, anchor='center')


url_entry = tk.Entry(root, width=15, font=("Helvetica", 14))
url_entry.place(x=200, y=150, anchor='center')

hour_label = tk.Label(root, text="Hour", font=('Verdana 30',16))
hour_label.place(x=133, y=100, anchor='center')

minute_label = tk.Label(root, text="Minute", font=('Verdana 30',16))
minute_label.place(x=266, y=100, anchor='center')

url_label = tk.Label(root, text="URL", font=('Verdana 30',16))
url_label.place(x=200, y=180, anchor='center')

alarm_button = tk.Button(root, text="Set Alarm", command=set_alarm, font=('Verdana 30',16))
alarm_button.place(x=200, y=230, anchor='center')

root.mainloop()