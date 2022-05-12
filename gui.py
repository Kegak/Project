from tkinter import *
from KeeganSims3_2 import *
from game import *
class GUI:
    def __init__(self, window):
        """
        Method that generates a gui window, has options for rock,
        paper, scissors, and a submit button. Generates a string
        telling the player if they win or not after they click
        submit
        """
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

        self.frame_middle = Frame(self.window)
        self.label = Label(self.window, text='')
        self.label.pack(side='bottom', pady=10)

        self.frame_bottom = Frame(self.window)
        self.button_submit = Button(self.frame_bottom, text='SUBMIT', command=self.clicked)
        self.button_submit.pack(side='bottom')
        self.frame_bottom.pack()

    def clicked(self):
        """
        Method that fills in the label when clicked and runs game.py
        """
        thing = self.radio_1.get()
        p = Game(thing, c_input=None)
        self.label.config(text=f'{p}')
        self.radio_1.set('0')