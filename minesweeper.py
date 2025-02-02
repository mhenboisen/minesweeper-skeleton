import tkinter as tk
from tkinter import font as tkFont
import random


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.titlefont = tkFont.Font(family="Arial", size=20, slant="italic")
        self.buttonFont = tkFont.Font(family="Arial", size=18)
        self.label = tk.Label(self, text="Minesweeper", font=self.titlefont)
        self.label.grid(row=0, column=1)
        self.goButton = tk.Button(self, text="    Go!    ", command=self.go, bg="green", fg="white")
        self.goButton.grid(row=0, column=0)
        self.buttongrid = tk.Frame(self)
        self.buttongrid.grid(row=2, column=0, sticky="NSEW", columnspan=2)
        self.buttons = []
        self.flagImage = tk.PhotoImage(file="flag.gif")
        self.mineImage = tk.PhotoImage(file="mine.gif")
        self.nomineImage = tk.PhotoImage(file="nomine.gif")
        buttonNum = 0
        for rownum in range(10):
            for columnnum in range(10):
                self.buttons.append(tk.Button(self.buttongrid, text=" ", font=self.titlefont))
                self.buttons[buttonNum].bind("<Button-1>", lambda event, x=buttonNum: self.buttonLeftClicked(event, x))
                self.buttons[buttonNum].bind("<Button-3>", lambda event, x=buttonNum: self.buttonRightClicked(event, x))
                self.buttons[buttonNum].config(height=50, width=50)
                self.buttons[-1].grid(row=rownum, column=columnnum, sticky="NSEW")
                self.buttongrid.rowconfigure(rownum, weight=1)
                self.buttongrid.columnconfigure(columnnum, weight=1)
                buttonNum += 1
        self.rowconfigure(2, weight=1)
        self.columnconfigure(1, weight=1)
        self.go()

    def buttonLeftClicked(self, event, pos):
        print("Button", pos, " was left clicked")
        # When this happens, you have to check self.minepositions to see if it contains a mine
        # if so, the mine explodes (  see dead()   )

        # if it's not a mine, it changes to show the number of mines in neighbouring cells (see getNoMines)
        # if there are no neighbouring mines (so it's blank) it flood-fills to reveal all contiguous blank cells
        pass

    def buttonRightClicked(self, event, num):
        # when right clicked, a mine will either show a flag or hide the flag
        pass

    def placeMines(self):
        self.minepositions = [0 for x in range(100)]
        # self.minepositions is a 100-slot array containing 0 for blank cells and 1 for mines
        # 20 mines should be placed randomly

    def getNoMines(self, pos):
        numberMines = 0
        # this checks the neighbouring cells of postion pos and counts the number of mines
        # it returns the number
        return numberMines

    def dead(self):
        self.gameOn = False
        # This changes all the cells to red, reveals the mines and ends the game

        # To change the image on a button to a mine, use this:
        # self.buttons[pos].config(image=self.mineImage)

        # To change the colour and style of button:
        # self.buttons[pos].config(state="normal", bg="red", relief="raised")

    def floodfill(self, pos):
        # This reveals all the contiguous blank spaces in a floood-fill manner.
        # so all the blank cells are revealed, and a 'border' of mine numbers around the area are also revealed

        # To make a button appear flat:
        # self.buttons[pos].config(image="", state="disabled", relief="flat", bg="lightblue")

        pass

    def go(self):
        self.placeMines()
        #after calling placeMines, this puts all the buttons back to their blank starting style
        for button in self.buttons:
            button.config(state="normal", text=" ", relief="raised", bg="lightgrey", image="")
        self.gameOn = True


mine = App()
mine.geometry("800x800+200+200")
mine.title("Minesweeper")
mine.mainloop()