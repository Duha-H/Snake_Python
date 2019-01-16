"""
    Main Snake Game Module
"""
# import tkinter for Python 3.x, Tkinter for Python 2.x
from tkinter import *
from tkinter import messagebox
from components import *
import time

class Game:
    """
        Game Definition and logic implementations
    """

    def __init__(self, master):
        self.width = 200
        self.height = 450
        
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()

        self.score = 0
        self.score_text = StringVar()
        self.score_text.set(0)
        
        self.score_label1 = Label(self.frame, text="SCORE", font="Fixedsys")
        self.score_label1.grid(row=0, column=0, columnspan=2, rowspan=3)
        
        self.score_label2 = Label(self.frame, textvariable=self.score_text, font=("Fixedsys", 14))
        self.score_label2.grid(row=2, column=0, columnspan=2, rowspan=5)
        
        self.start_button = Button(self.frame, text="START", command=self.start_game)
        self.start_button.grid(row=10, column=0)

        self.quit_button = Button(self.frame, text="QUIT", command=self.frame.quit)
        self.quit_button.grid(row=10, column=1)

        self.board = Board(self.frame)

        self.snake = Snake()

        self.apple = Apple()

        self.started = False

        self.board.draw_board(self.snake.pos, self.apple.pos)       
        
        # bind controls
        master.bind('<Up>', self.move_up)
        master.bind('<Down>', self.move_down)
        master.bind('<Left>', self.move_left)
        master.bind('<Right>', self.move_right)
        master.bind('q', quit)


    def start_game(self):
        self.started = True
        if not self.snake.dead: 
            self.move(self.snake.forward)
            root.after(1000, self.start_game)

    def move(self, direction):
        '''Implements game logic, performs a move if it is valid,
           resets game if move is invalid and player dies'''
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
            self.update_score()
        elif new_block in self.snake.pos and new_block != self.snake.pos[1]:    # invalid move; snake wrapping around itself
            self.death_message()
        elif new_block[0] >= self.board.width or new_block[0] < 0:   # invalid move, out of board bounds
            self.death_message()
        elif new_block[1] >= self.board.height or new_block[1] < 0:   # invalid move, out of board bounds
            self.death_message()
        else:   # no apple, and move is valid
            self.snake.move(new_block, False)
        self.board.refresh(self.snake.pos, self.apple.pos)
    
    def move_up(self, event):
        if self.started:
            self.move('up')

    def move_down(self, event):
        if self.started:
            self.move('down')

    def move_left(self, event):
        if self.started:
            self.move('left')

    def move_right(self, event):
        if self.started:
            self.move('right')

    def death_message(self):
        self.snake.dead = True
        messagebox.showerror("Whoops", "You ded")
        self.reset()

    def reset(self):
        '''Resets game components after player has died'''
        self.started = False
        self.score = 0
        self.score_text.set(self.score)        
        self.snake = Snake()
        self.apple = Apple()
        self.board.draw_board(self.snake.pos, self.apple.pos)

    def update_score(self):
        self.score += 5
        self.score_text.set(self.score)

# Tk root widget and mainloop

root = Tk()

game = Game(root)

root.mainloop()