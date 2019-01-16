'''
    Board Definition Module
'''
from tkinter import *


global cell_size, cols, rows
cell_size = 15
cols = 14
rows = 25

class Board:
    '''
        Definition of game board
    '''

    def __init__(self, master):
        '''A grid of blocks, filled based on game state'''
        
        self.cols = cols
        self.rows = rows
        
        self.width = cell_size * self.cols
        self.height = cell_size * self.rows

        self.canvas = Canvas(master, width=self.width, height=self.height) #, fill='red')
        self.canvas.grid(row=0, column=2, rowspan=20)


    def draw_board(self, snake_pos, apple_pos):
        '''Draws the game board, fills in blocks based on position of snake and apple'''
        x = -cell_size
        y = -cell_size
        color = ''
        tag = ''
        for i in range(self.rows * self.cols):
            if i % self.cols == 0:
                x = 0
                y += cell_size
            else:
                x += cell_size
            
            if (x, y) == apple_pos:   #if coordinate is apple position: fill in red
                color = 'red'
                tag = 'apple'
            elif (x, y) in snake_pos: #if coordinate is in snake position: fill in black
                color = 'black'
                tag = 'snake'
            else:                     #else: no fill
                color = ''
                tag = ''
            
            self.canvas.create_rectangle(x, y, x+cell_size, y+cell_size, fill=color, outline='white', tag=tag)

    def refresh(self, snake_pos, apple_pos):
        '''Removes existing snake/apple block fills, and redraws them given their new positions'''
        self.canvas.itemconfigure('snake', fill='', outline='white', tag='')
        self.canvas.itemconfigure('apple', fill='', outline='white', tag='')
        x = -cell_size
        y = -cell_size
        for i in range(self.rows * self.cols):
            if i % self.cols == 0:
                x = 0
                y += cell_size
            else:
                x += cell_size

            if (x, y) in snake_pos:
                self.canvas.create_rectangle(x, y, x+cell_size, y+cell_size, fill='black', outline='white', tag='snake')
            elif (x, y) == apple_pos:
                self.canvas.create_rectangle(x, y, x+cell_size, y+cell_size, fill='red', outline='white', tag='apple')

