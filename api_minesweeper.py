"""
Implementation of a REST API interface to command the game
"""

from minesweeper import Board
from fastapi import FastAPI

class Minesweeper(Board):
    def __init__(self, dim_size, num_bombs):
        super().__init__(dim_size, num_bombs)
        self.status = "playing"

    
    def get_visible_board(self):
        # this is a magic function where if you call print on this object,
        # it'll print out what this function returns!
        # return a string that shows the board to the player

        # first let's create a new array that represents what the user would see
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        
        return visible_board

    
    def set_status(self, status):
        self.status = status


app = FastAPI()

board = Minesweeper(10,10)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/visible_board")
def get_visible_board():
    if board.status != 'loser':
        return {
            "response":"ok",
            "board": board.get_visible_board(),
            "msg":"",
            "status": board.status
        }
    
    return {
        "response":"ok",
        "board": board.board,
        "msg":"",
        "status": board.status
    }


@app.get("/board")
def get_board():
    return {
        "response":"ok",
        "board": board.board,
        "msg":"",
        "status": board.status
    }


@app.post("/dig/{row}/{col}")
def dig(row, col):
    
    if int(row) < 0 or int(row) >= board.dim_size or int(col) < 0 or int(col) >= board.dim_size:
        return {
            "response":"ok",
            "board": board.get_visible_board(),
            "msg":"Invalid location. Try again."
        }

    # if it's valid, we dig
    safe = board.dig(int(row), int(col))

    if not safe:
        board.set_status("loser")
        return {
            "response":"ok",
            "board": board.board,
            "msg":"loser"
        }

    if len(board.dug) == board.dim_size ** 2 - board.num_bombs:
        board.set_status("winner")
        return {
            "response":"ok",
            "board": board.board,
            "msg":"winner"
        }

    return {
        "response":"ok",
        "board": board.get_visible_board(),
        "msg":"",
        "status": board.status
    }


@app.post("newgame/")
def new_game():
    board = Minesweeper(10,10)
    return {
        "response":"ok",
        "board": board.get_visible_board(),
        "msg":"",
        "status": board.status
    }