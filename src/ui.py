from tkinter import *
import threading

from maze.Spot import Spot

import algorithms.aStar as aStar
import algorithms.djikstra as djikstra
import algorithms.bfs as bfs

class Ui:
    def __init__(self):
        self.window = None

        self.canvas = None

        self.buttonFrame = None

        self.aStarButton = None

        self.width = 0
        self.height = 0

    def start(self, maze):
        self.window = Tk()
        self.window.title("Pathfinder Viewer")
        self.window.geometry("600x700")
        self.window.resizable(False, False)
        self.window.update_idletasks()

        self.width = self.window.winfo_width()
        self.height = self.window.winfo_height()
        # Grid frame

        self.canvas = Canvas(self.window, width=self.width, height=self.height - 100, bg="white")
        self.canvas.pack(fill="both", expand=True)

        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[i][j].getWallStatus():
                    self.drawCell(maze[i][j], "black", maze)
                else:
                    self.drawCell(maze[i][j], "white", maze)

        # Button frame
        self.buttonFrame = Frame(self.window)
        self.buttonFrame.pack(pady=10)

        self.aStarButton = Button(self.buttonFrame, text="A*", width=10, command=lambda:aStar.aStarSimulation(self, maze))
        #self.aStarButton = Button(self.buttonFrame, text="A*", width=10, command=lambda:threading.Thread(target=aStar.aStarSimulation, args=(self, maze)).start())
        self.aStarButton.pack(side=LEFT, padx=5)

        self.djikstraButton = Button(self.buttonFrame, text="Djikstra", width=10, command=lambda:djikstra.djikstraSimulation(self, maze))
        #self.djikstraButton = Button(self.buttonFrame, text="Djikstra", width=10, command=lambda:threading.Thread(target=djikstra.djikstraSimulation, args=(self, maze)).start())
        self.djikstraButton.pack(side=LEFT, padx=5)

        self.BFSButton = Button(self.buttonFrame, text="BFS", width=10, command=lambda:bfs.bfsSimulation(self, maze))
        #self.BFSButton = Button(self.buttonFrame, text="BFS", width=10, command=lambda:threading.Thread(target=bfs.bfsSimulation, args=(self, maze)).start())
        self.BFSButton.pack(side=LEFT, padx=5)

        self.window.mainloop()

    def drawCell(self, cell, color, maze):
        # DISCLAIMER: Em células o i representa a linha e o j a coluna mas em x, y é ao contrário (pixeis)
        if cell.getCell() is not None:
            self.canvas.itemconfig(cell.getCell(), fill=color)
        else:
            x1 = cell.getj() * self.width // len(maze) 
            y1 = cell.geti() * (self.height - 100) // len(maze[0])
            x2 = (cell.getj() + 1) * self.width // len(maze)
            y2 = (cell.geti() + 1) * (self.height - 100) // len(maze[0])
            cell.setCell(self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black"))

    def update(self):
        self.window.update()