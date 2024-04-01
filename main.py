import time
import tkinter as tk
import threading


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('700x500')
        self.var = tk.StringVar()
        self.var.trace("w", self.reset_timer)
        self.entry = tk.Entry(self, textvariable=self.var, width=100)
        self.timer = 10
        self.label = tk.Label(text=f'Time left: {self.timer} seconds.')
        self.label.pack()
        self.entry.pack()
        self.main_ctd()
        self.mainloop()

    def reset_timer(self, *args):
        self.timer = 10
    def countdown(self):
        while True:
            self.timer-=1
            self.label['text'] = f'Time left: {self.timer} seconds.'
            if self.timer <= 0:
                self.timer = 10
                with open('texts.txt','a') as file:
                    file.write(self.var.get())
                self.var.set('')
            time.sleep(1)

    def main_ctd(self):
        thread = threading.Thread(target=self.countdown)
        thread.start()

app = App()
