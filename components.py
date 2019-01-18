'''
    Definition module of all game components (Snake, Apple)
'''
from tkinter import *
from board import *
import random


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

    def new_apple(self, snake_pos):
        new_x = random.randint(0, cols-1)
        new_y = random.randint(0, rows-1)
        new_pos = (new_x * cell_size, new_y * cell_size)
        if new_pos not in snake_pos:    # set new random position if chosen block is not occupied by snake
            self.pos = (new_x * cell_size, new_y * cell_size)
        else:
            self.new_apple(snake_pos)