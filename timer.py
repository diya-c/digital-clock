import threading
import time
import tkinter as tk
from win10toast import ToastNotifier
from tkinter import messagebox
from PIL import Image, ImageTk

class Countdowntimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x300")
        self.root.title("Timer")
        
        image1 = Image.open("C:\\Users\\user\\Desktop\\mini project\\green2.jpg")
        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(image=test)
        label1.image = test
        # Position image
        label1.pack()


        self.time_entry = tk.Entry(self.root, font=("Helvetica", 18),)
        self.time_entry.place(x=200, y=170, anchor='center')

        self.start_button = tk.Button(self.root, font=("Helvetica", 15), text="Start", command=self.start_thread, width=5)
        self.start_button.place(x=160, y=230, anchor='center')

        self.stop_button = tk.Button(self.root, font=("Helvetica", 15), text="Reset", command=self.stop, width=5)
        self.stop_button.place(x=240, y=230, anchor='center')

        self.time_label = tk.Label(self.root, font=("Helvetica", 30), text="Time: 00:00:00")
        self.time_label.place(x=200, y=80, anchor='center')

        self.stop_loop = False

        self.root.mainloop()

    def start_thread(self):

        t = threading.Thread(target=self.start)
        t.start()

    def start(self):
        self.stop_loop = False
        hours,minutes,seconds=0,0,0
        string_split = self.time_entry.get().split(":")
        if len(string_split) == 3:
            hours = int(string_split[0])
            minutes = int(string_split[1])
            seconds = int(string_split[2])

        elif len(string_split) == 2:
            minutes = int(string_split[0])
            seconds = int(string_split[1])

        elif len(string_split) == 1:
            seconds = int(string_split[0])

        else:
            print("Invalid time format")
            return
        full_seconds = (hours*3600) + (minutes * 60) + seconds

        while full_seconds > 0 and not self.stop_loop:
            full_seconds -= 1

            minutes, seconds = divmod(full_seconds, 60)
            hours, minutes = divmod(minutes, 60)

            self.time_label.config(text=f"Time: {hours:02d}:{minutes:02d}:{seconds:02d}")
            self.root.update()
            time.sleep(1)
        if full_seconds==0 :
            toast = ToastNotifier()
            tk.messagebox.showinfo(title="Countdown Timer", message="Times UP!" )
            toast.show_toast("Countdown Timer", " Times UP !") 

    def stop(self):
        self.stop_loop = True
        self.time_label.config(text="Time: 00:00:00")


Countdowntimer()