from tkinter import *
from customtkinter import *
from client import Client
import threading


class Program:
    def __init__(self):
        self.window = Tk()
        self.center(500,500)
        self.client = Client()
        self.enter_user()

    def center(self, w, h):
        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()
        x = (width - w) // 2
        y = (height - h) // 2
        return self.window.geometry(f'{w}x{h}+{x}+{y}')
    
    def enter_user(self):   
        self.enter_user_frame = Frame(self.window, bg='gray')
        self.enter_user_frame.pack(fill='both', expand=True)
        self.user_entry = Entry(self.enter_user_frame)
        self.user_entry.place(x=180, y=180)

        self.user_button = Button(self.enter_user_frame, 
                                  text='Enter chat',
                                  command=lambda user=str(self.user_entry.get()): threading.Thread(target=self.user_button_function, args=(user,)).start())
        self.user_button.place(x=210, y=230)

    def user_button_function(self, user):
        print(user)
        self.client.set_user(str(user))

if __name__ == "__main__":
    program = Program()
    program.window.mainloop()