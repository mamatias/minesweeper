"""
Implementation of a REST API interface to command the game
"""

import minesweeper
from fastapi import FastAPI

app = FastAPI()

board = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/board")
def get_board():
    if board:
        return {"board": None, "res": 1}
    
    return {"board": None, "res": -1}
    
# def main()-> None:
#     minesweeper.play()

# if __name__ == '__main__':
#     main()