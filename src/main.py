import ui
import maze.maze as maze

def main():
    randomMaze = maze.generateMaze()

    ui.start(randomMaze)

if __name__ == "__main__":
    main()