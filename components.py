'''
    Definition module of all game components
'''
from tkinter import *
import random


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


class Snake:
    '''
        Definition of snake (player-controlled component)
    '''

    def __init__(self):
        '''Defines snake position using a list of (col, row) coordinates'''
        self.pos = [(6 * cell_size, 10 * cell_size), 
                    (5 * cell_size, 10 * cell_size), 
                    (4 * cell_size, 10 * cell_size)] #TODO: center initial snake position
        self.length = 3
        self.forward = 'right'  # keep track of a forward direction
        self.dead = False

    def move(self, new_head, consume):
        '''Adds a new (head) block in the direction of motion
           and removes a block from the end of the list (if no apple is consumed)'''
        self.pos.insert(0, new_head)
        if not consume:
            self.pos.pop()


class Apple:
    '''
        Definition of apple (appears at random positions)
    '''

    def __init__(self):
        '''Defines apple position using a (col, row) tuple,
           position changes when apple is "consumed"'''
        self.pos = (5*cell_size, 5*cell_size) #TODO: center initial apple position

    def new_apple(self):
        new_x = random.randint(0, cols-1)
        new_y = random.randint(0, rows-1)
        self.pos = (new_x * cell_size, new_y * cell_size)