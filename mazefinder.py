from curses import wrapper
import curses
import queue
import time

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def printmaze(maze, stdscr, path):
    blue = curses.color_pair(1)
    red = curses.color_pair(2) 
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j*2, "X", red)    
            else:
                stdscr.addstr(i, j*2, value, blue)


def findstart(maze, startsymbol):
    for i, row in enumerate(maze):
        for j, val in enumerate(row):
            if maze[i][j] == startsymbol:
                return i, j
    return None


def findpath(maze, stdscr):
    start = "O"
    end = "X"
    startpos = findstart(maze, start)

    q = queue.Queue()
    q.put((startpos, [startpos]))

    visited = set()

    while q.qsize():
        currentpos, path = q.get()
        row, col = currentpos

        stdscr.clear()
        printmaze(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()

        if maze[row][col] == end:
            return path

        nebors = findnebors(maze, row, col)

        for nbor in nebors:
            if nbor in visited:
                continue

            r, c = nbor
            if maze[r][c]=="#":
                continue

            newpath = path + [nbor]
            q.put((nbor, newpath))
            visited.add(nbor)



def findnebors(maze, row, col):
    nebors = list()

    if row>0:
        nebors.append((row-1, col))
    if row+1<len(maze):
        nebors.append((row+1, col))
    if col>0:
        nebors.append((row, col-1))
    if col+1<len(maze[0]):
        nebors.append((row, col+1))

    return nebors




 
def main(stdscr):
    stdscr.clear()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    findpath(maze, stdscr)
    stdscr.getch()

wrapper(main)