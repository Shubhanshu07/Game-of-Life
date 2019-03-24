#!/usr/bin/env python

import time
import curses
from random import randint

PG_W = 20
PG_H = 20

playground=None

def init_playground():
    global playground
    playground = []
    for y in range(0, PG_H):
        playground.append([])
        for x in range(0, PG_W):
            playground[y].append(randint(0,1))

stdscr_dbg = None
def debug_init(stdscr):
    global stdscr_dbg
    stdscr_dbg = stdscr
    
def debug(str):
    stdscr_dbg.addstr(PG_H, 0, " "*PG_W)
    stdscr_dbg.addstr(PG_H, 0, "DEBUG: " + str)
    stdscr_dbg.refresh()

count = 0
def update_ground(playground):
    global count
    new_pg = [[0 for x in range(0, PG_W)] for y in range(0, PG_H)]

    for y in range(0, PG_H):
        for x in range(0, PG_W):
            neighbours = [[0 for i in list(range(0, 3))] for j in list(range(0, 3))]
            if y == 0:
                pass
            elif y == PG_H-1:
                pass
            elif x == 0:
                pass
            elif x == PG_W-1:
                pass
            else:
                time.sleep(0)
                for i in range(y-1,y+2):
                    for j in range(x-1,x+2):
                        neighbours[i-y+1][j-x+1] = playground[i][j]
                
            neighbour_count = sum([i.count(1) for i in neighbours])

            count += 1
            debug(str(count) + " " + "neighbour_count: " + str(neighbour_count) + "size: " + str(neighbours))

            if playground[y][x] == 1: # alive
                if neighbour_count != 2 and neighbour_count != 3 :
                    new_pg[y][x] = 0
                else:
                    new_pg[y][x] = 1
            else: # dead
                if neighbour_count == 3:
                    new_pg[y][x] = 1
                else:
                    new_pg[y][x] = 0
    return new_pg

def main(stdscr):
    global playground
    debug_init(stdscr)
    init_playground()

    stdscr.clear()
    stdscr.addstr("Initialized the array")
    while (True):
        for x in range(0, PG_W):
            for y in range(0, PG_H):
                stdscr.addch(y, x, str(playground[y][x]))
        stdscr.refresh()

        time.sleep(1)
        playground = update_ground(playground)
                

    stdscr.getkey()
    

curses.wrapper(main)

print(playground)
