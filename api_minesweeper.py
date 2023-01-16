"""
Implementation of a REST API interface to command the game
"""

from minesweeper import Board
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


# Mounting the static site for the UI. Can be launched with any web server
app.mount("/web", StaticFiles(directory="web"), name="static")

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:5500",
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Main game
board = Board(10,10)


# The API Part
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/status")
def get_status():
    return {
        "response":"ok",
        "board": board.get_visible_board(),
        "msg":"",
        "status": board.status,
        "startTime": board.startTime,
        "endTime": board.endTime,
    }


@app.get("/visible_board")
def get_visible_board():
    if board.status != 'loser':
        return {
            "response":"ok",
            "board": board.get_visible_board(),
            "msg":"",
            "status": board.status,
            "startTime": board.startTime,
            "endTime": board.endTime,
        }
    
    return {
        "response":"ok",
        "board": board.board,
        "msg":"",
        "status": board.status,
        "startTime": board.startTime,
        "endTime": board.endTime,
    }


@app.get("/board")
def get_board():
    return {
        "response":"ok",
        "board": board.board,
        "msg":"",
        "status": board.status,
        "startTime": board.startTime,
        "endTime": board.endTime,
    }


@app.post("/dig/{row}/{col}")
def dig(row, col):   
    if int(row) < 0 or int(row) >= board.dim_size or int(col) < 0 or int(col) >= board.dim_size:
        return {
            "response":"ok",
            "board": board.get_visible_board(),
            "msg":"Invalid location. Try again.",
            "status": board.status,
            "startTime": board.startTime,
            "endTime": board.endTime,
        }

    # if it's valid, we dig
    board.dig(int(row), int(col))

    return {
        "response":"ok",
        "board": board.get_visible_board(),
        "msg":"",
        "status": board.status,
        "startTime": board.startTime,
        "endTime": board.endTime,
    }


@app.post("/superdig/{row}/{col}")
def superdig(row, col):
    row = int(row)
    col =int(col)
    
    if row < 0 or row >= board.dim_size or col < 0 or col >= board.dim_size:
        print("invalid location")
        return {
            "response":"ok",
            "board": board.get_visible_board(),
            "msg":"Invalid location. Try again.",
            "status": board.status,
            "startTime": board.startTime,
            "endTime": board.endTime,
        }

    # if it's valid, we dig
    for r in range(max(0, row-1), min(board.dim_size-1, row+1)+1):
        for c in range(max(0, col-1), min(board.dim_size-1, col+1)+1):
            if (r == row and c == col) or (r, c) in board.dug or (r, c) in board.bet:
                # our original location, don't dig
                continue
            
            # Dig
            board.dig(r, c)

            if board.status != "playing":
                return {
                    "response":"ok",
                    "board": board.get_visible_board(),
                    "msg":"",
                    "status": board.status,
                    "startTime": board.startTime,
                    "endTime": board.endTime,
                }

    return {
        "response":"ok",
        "board": board.get_visible_board(),
        "msg":"",
        "status": board.status,
        "startTime": board.startTime,
        "endTime": board.endTime,
    }


@app.post("/mark/{row}/{col}")
def mark(row, col):
    if int(row) < 0 or int(row) >= board.dim_size or int(col) < 0 or int(col) >= board.dim_size:
        return {
            "response":"ok",
            "board": board.get_visible_board(),
            "msg":"Invalid location. Try again.",
            "status": board.status,
            "startTime": board.startTime,
            "endTime": board.endTime,
        }

    board.mark(int(row), int(col))

    return {
        "response":"ok",
        "board": board.get_visible_board(),
        "msg":"",
        "status": board.status,
        "startTime": board.startTime,
        "endTime": board.endTime,
    }


@app.post("/newgame")
def new_game():
    global board
    board = Board(10,10)
    return {
        "response":"ok",
        "board": board.get_visible_board(),
        "msg":"",
        "status": board.status,
        "startTime": board.startTime,
        "endTime": board.endTime,
    }