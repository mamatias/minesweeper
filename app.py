# import minesweeper
from fastapi import FastAPI

class Contador:
    def __init__(self, cuenta = 0):
        self.cuenta = cuenta

    def sumar(self):
        self.cuenta = self.cuenta + 1

    def restar(self):
        self.cuenta = self.cuenta - 1

    def show(self):
        return self.cuenta

app = FastAPI()

contador = Contador(0)

@app.get("/actual")
def read_root():
    return {"Valor": contador.show()}


@app.get("/sumar")
def def_value():
    contador.sumar()
    return {"Valor": contador.show()}

@app.get("/restar")
def def_value():
    contador.restar()
    return {"Valor": contador.show()}