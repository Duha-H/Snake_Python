'''
    Board Definition Module
'''
from tkinter import *

class Board:

    def __init__(self, master):
        '''A grid of blocks, filled based on game state'''
        
        self.cols = 14
        self.rows = 25
        
        self.width = 15 * self.cols
        self.height = 15 * self.rows

        self.canvas = Canvas(master, width=self.width, height=self.height) #, fill='red')
        self.canvas.pack(side=LEFT)
        
        self.draw_board()


    def draw_board(self):
        '''Draw the game board, fill in blocks based on position of snake and apple'''
        #print("DRAWING!!!")
        for i in range(self.cols):
            for j in range(self.rows):
                self.canvas.create_rectangle(i, j, 15*i, 15*j)

    def fill_rect(self, x, y):
        self.canvas.create_rectangle(x, y, 15*x, 15*y, fill='red')

    #def refresh(self, snake_pos, apple_pos):

