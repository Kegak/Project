from tkinter import *
from KeeganSims3_2 import *
from game import *
class GUI:
    def __init__(self, window):
        self.window = window

        self.frame_top = Frame(self.window)
        self.radio_1 = StringVar()
        self.radio_1.set('0')
        self.radio_rock = Radiobutton(self.frame_top, text='Rock', variable=self.radio_1, value='rock')
        self.radio_paper = Radiobutton(self.frame_top, text='Paper', variable=self.radio_1, value='paper')
        self.radio_scissor = Radiobutton(self.frame_top, text='Scissors', variable=self.radio_1, value='scissor')
        self.radio_rock.pack(side='left')
        self.radio_paper.pack(side='left')
        self.radio_scissor.pack(side='left')
        self.frame_top.pack()

        self.frame_bottom = Frame(self.window)
        self.button_submit = Button(self.frame_bottom, text='SUBMIT', command=self.clicked)
        self.button_submit.pack(side='bottom', pady=10)
        self.frame_bottom.pack()

    def clicked(self):
        thing = self.radio_1.get()
        p = Game(thing)
        print(p)
        self.radio_1.set('0')