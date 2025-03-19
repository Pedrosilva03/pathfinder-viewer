from tkinter import *

from maze.Spot import Spot

class Ui:
    def __init__(self):
        self.window = None

        self.canvas = None

        self.buttonFrame = None

        self.aStarButton = None

    def start(self, maze):
        self.window = Tk()
        self.window.title("Pathfinder Viewer")
        self.window.geometry("600x700")
        self.window.update_idletasks()

        # Grid frame

        self.canvas = Canvas(self.window, width=self.window.winfo_width(), height=self.window.winfo_height() - 100, bg="white")
        self.canvas.pack(fill="both", expand=True)

        for i in range(len(maze)):
            for j in range(len(maze[0])):
                self.drawCell(maze[i][j], "white", maze)

        # Button frame
        self.buttonFrame = Frame(self.window)
        self.buttonFrame.pack(pady=10)

        self.aStarButton = Button(self.buttonFrame, text="A*", width=10)
        self.aStarButton.pack(side=LEFT, padx=5)

        self.window.mainloop()

    def drawCell(self, cell, color, maze):
        x1, y1 = cell.getj() * self.window.winfo_width() // len(maze), cell.geti() * (self.window.winfo_height() - 100) // len(maze[0])
        x2, y2 = (cell.getj() + 1) * self.window.winfo_width() // len(maze), (cell.geti() + 1) * (self.window.winfo_height() - 100) // len(maze[0])
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")