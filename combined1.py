import tkinter as tk
import time
from datetime import datetime
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import subprocess


class DigitalClock(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Digital Clock")
        self.geometry("350x537")
        combined_image = Image.open("C:\\Users\\user\\Desktop\\mini project\\greenbg.jpg")
        img = ImageTk.PhotoImage(combined_image)
        combined_label = tk.Label(image=img)
        combined_label.image = img
        combined_label.pack()

        self.time_label=tk.Label(self, font=('Verdana 30 bold',34))
        self.time_label.place(x=175, y=110, anchor='center')
        self.update_time()
        
        
        #alarm button
        self.start_alarm_button = tk.Button(self, text="Alarm", width=10, height=1 ,command=self.start_alarm, font=('Verdana 30',16))
        self.start_alarm_button.place(x=175, y=250, anchor='center')
        
        
        #timer button
        self.start_timer_button = tk.Button(self, text="Timer", width=10, height= 1 ,command=self.start_timer, font=('Verdana 30',16))
        self.start_timer_button.place(x=175, y=325, anchor='center')

        
        #stopwatch button
        self.start_stopwatch_button = tk.Button(self, text="Stopwatch", width=10, height=1 , command=self.start_stopwatch, font=('Verdana 30',16))
        self.start_stopwatch_button.place(x=175 ,y=400, anchor='center')
        
    
        
    
    #digital clock
    def update_time(self):
        time_text = time.strftime(" %H:%M:%S %p ")
        self.time_label.config(text=time_text)
        self.after(1000, self.update_time)
    
    
    
    
    
    #stopwatch
    def start_stopwatch(self):
        stopwatch_path="C:\\Users\\user\\Desktop\\mini project\\stopwatch.py"
        subprocess.run(["python", stopwatch_path])
            
    
    #timer
    def start_timer(self):
        timer_path="C:\\Users\\user\\Desktop\\mini project\\timer.py"
        subprocess.run(["python", timer_path])


    #alarm
    def start_alarm(self):
        alarm_path="C:\\Users\\user\\Desktop\\mini project\\alarm_clock.py"
        subprocess.run(["python", alarm_path])
        


if __name__ == "__main__":
    clock = DigitalClock()
    clock.mainloop()