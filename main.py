import tkinter as tk
from datetime import datetime

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.time_now = datetime.now().strftime("%H:%M:%S")
        self.label = tk.Label(self)
        self.label["text"] = self.time_now
        self.label.pack()

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def update(self):
        self.label["text"] = datetime.now().strftime("%H:%M:%S")
        root.after(1000, self.update)

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
root.geometry("500x200")
app = Application(master=root)
app.update()
app.mainloop()