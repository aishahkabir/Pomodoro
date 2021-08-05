import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self)
        self.label["text"] = "Test"
        self.label.pack()

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")


    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
root.geometry("500x200")
app = Application(master=root)
app.mainloop()