"""
    Main Snake Game Module
"""
# import tkinter for Python 3.x, Tkinter for Python 2.x
from tkinter import *
from components import *
import time

class Game:
    """
        Game Definition and logic implementations
    """
    global w, h
    w = 200
    h = 450

    def __init__(self, master):
        self.width = 200
        self.height = 450
        
        frame = Frame(master)
        frame.pack()

        #bind controls
        master.bind('<Up>', self.move_up)
        master.bind('<Down>', self.move_down)
        master.bind('<Left>', self.move_left)
        master.bind('<Right>', self.move_right)

        self.start_button = Button(frame, text="START", command=self.start_game)
        self.start_button.pack(side=LEFT)

        self.quit_button = Button(frame, text="QUIT", command=frame.quit)
        self.quit_button.pack(side=LEFT)

        self.board = Board(frame)
        
        self.snake = Snake()

        self.apple = Apple()

        self.board.draw_board(self.snake.pos, self.apple.pos)


    def start_game(self):
        #print("STARTED!")
        self.move(self.snake.forward)
        root.after(1200, self.start_game)

    def move(self, direction):
        dx = 0
        dy = 0
        if direction == 'up':
            dy = -cell_size
        elif direction == 'down':
            dy = cell_size
        elif direction == 'left':
            dx = -cell_size
        else:
            dx = cell_size
        new_block = (self.snake.pos[0][0] + dx, self.snake.pos[0][1] + dy)
        self.snake.forward = direction
        if new_block == self.apple.pos:  # consume apple
            self.snake.move(new_block, True)
            self.apple.new_apple()
        elif new_block not in self.snake.pos:   # no apple, move in direction if possible
            self.snake.move(new_block, False)
        self.board.refresh(self.snake.pos, self.apple.pos)
    
    def move_up(self, event):
        self.move('up')

    def move_down(self, event):
        self.move('down')

    def move_left(self, event):
        self.move('left')

    def move_right(self, event):
        self.move('right')

    def death_message(self):
        messagebox.showerror("Whoops", "You ded")


# Tk root widget and mainloop

root = Tk()

game = Game(root)

root.mainloop()