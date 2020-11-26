import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_components()

    def create_components(self):
        self.hi_btn = tk.Button(self)
        self.hi_btn['text'] = "Hello World\n(Click Me)"
        self.hi_btn['command'] = self.say_hello
        self.hi_btn.pack(side='top')

        self.quit = tk.Button(self)
        self.quit['text'] = 'Quit'    
        self.quit['command'] = self.master.destroy
        self.quit['fg'] = 'red'
        self.quit.pack(side='bottom')

    def say_hello(self):
        print('Hi')

root = tk.Tk()
app = Application(root)

tk.mainloop()