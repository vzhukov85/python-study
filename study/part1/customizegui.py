from tkinter import mainloop
from tkinter.messagebox import showinfo
from tkinter102 import MyGui


class CustomGui(MyGui):
    def reply(self):
        showinfo(title='popup', message='Outch!')


if __name__ == '__main__':
    CustomGui().pack()
    mainloop()
