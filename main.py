import tkinter as tk
import datetime
import time

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        #self.time_now = datetime.now().strftime("%H:%M:%S")
        self.label = tk.Label(self)
        #self.label["text"] = self.time_now
        self.label.pack()
        self.start = tk.Button(self, text="Start timer", fg="blue")
        self.start.pack(side="left")
        self.start = tk.Button(self, text="Stop timer", fg="green")
        self.start.pack(side="right")
        self.quit = tk.Button(self, text="Quit", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def update(self):
        #self.label["text"] = datetime.now().strftime("%H:%M:%S")
        root.after(1000, self.update)


    def say_hi(self):
        print("hi there, everyone!")

def _format_time(t):
    seconds = t % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%02d:%02d" % (minutes, seconds)

def countdown(t):
    while t:
        timer = str(datetime.timedelta(seconds=t))
        print(_format_time(t))
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Fire in the hole!!')


root = tk.Tk()
root.title("Pomodoro Timer")
root.geometry("500x200")
app = Application(master=root)
countdown(int(1500))
app.update()
app.mainloop()