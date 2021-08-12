import tkinter as tk
from datetime import datetime

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.t = 1500

    def create_widgets(self):
        self.time_now = datetime.now().strftime("%H:%M:%S")
        self.label = tk.Label(self)
        self.label["text"] = self.time_now
        self.label.pack()
        self.start = tk.Button(self, text="Start timer", fg="blue")
        self.start.pack(side="left")
        self.start = tk.Button(self, text="Stop timer", fg="green")
        self.start.pack(side="right")
        self.quit = tk.Button(self, text="Quit", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def update(self):
        if self.t > 0:
            seconds = self.t % (24 * 3600)
            seconds %= 3600
            minutes = seconds // 60
            seconds %= 60
            self.label["text"] = "%02d:%02d" % (minutes, seconds)
            self.t -= 1
            root.after(1000, self.update)

root = tk.Tk()
root.title("Pomodoro Timer")
root.geometry("500x200")
app = Application(master=root)
app.update()
app.mainloop()
