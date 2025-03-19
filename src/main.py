from Ui import Ui
import maze.maze as maze

def main():
    randomMaze = maze.generateMaze()

    ui = Ui()
    ui.start(randomMaze)

if __name__ == "__main__":
    main()