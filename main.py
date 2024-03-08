from tkinter import *


class GUI(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.title("Gui")
        self.configure(bg="#eee",
                       height=500,
                       width=500)

    def add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.pack()
        self.heading_label.configure(font="Arial 24",
                                     text="Sup bro?")


gui = GUI()
gui.mainloop()
