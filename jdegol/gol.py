#!/usr/bin/env python3

import curses
import json
import os
import time

from random import randint

pg_w = None
pg_h = None

playground=None

# Init Types
RANDOM = 0
JSON = 1

enable_dbg=False

PG_SKIN = ['.','@']

stdscr_dbg = None
def debug_init(stdscr):
    global stdscr_dbg
    stdscr_dbg = stdscr
    
def debug(str):
    if enable_dbg:
        stdscr_dbg.addstr(pg_h, 0, " "*pg_w)
        stdscr_dbg.addstr(pg_h+1, 0, " *** DEBUG: " + str + " ***")
        stdscr_dbg.refresh()

""" Returns a list of list of int of same size as the playground but
each location denoting the number of neighbousr of the original
cell """
def get_neighbours(playground):
    padded_pg = [[0 for i in range(len(playground[0])+2)] for j in range(len(playground)+2)]
    for i in range(len(playground)):
        for j in range(len(playground[0])):
            padded_pg[i+1][j+1] = playground[i][j]

    result = [[0 for i in list(range(len(playground[0])))] for j in list(range(len(playground)))]
    
    for y in range(len(playground)):
        for x in range(len(playground[0])):
            neighbours = [[0 for i in list(range(3))] for j in list(range(3))]

            time.sleep(0)
            for i in range(3):
                for j in range(3):
                    neighbours[i][j] = padded_pg[i+y][j+x]

            # Find the neighbours of the current cell, by counting the
            # number of alive cells in a 3x3 grid centered at the
            # current cell
            neighbour_count = sum([i.count(1) for i in neighbours]) - playground[y][x] 
    
            result[y][x] = neighbour_count
    return result
    
count = 0
def update_pg(playground):
    global count
    w = len(playground[0])
    h = len(playground)

    new_pg = [[0 for x in range(0, w)] for y in range(0, h)]
    neighbour_count = get_neighbours(playground)
    
    for y in range(0, h):
        for x in range(0, w):
            
            count += 1
            debug(str(count) + " " + "neighbour_count: " + str(neighbour_count[y][x]))

            if playground[y][x] == 1: # alive
                if neighbour_count[y][x] != 2 and neighbour_count[y][x] != 3 :
                    new_pg[y][x] = 0
                else:
                    new_pg[y][x] = 1
            else: # dead
                if neighbour_count[y][x] == 3:
                    new_pg[y][x] = 1
                else:
                    new_pg[y][x] = 0
    return new_pg

def entrypoint(stdscr):
    global playground
    debug_init(stdscr)

    stdscr.clear()

    while (True):
        for x in range(0, pg_w):
            for y in range(0, pg_h):
                stdscr.addch(y, 2*x, PG_SKIN[playground[y][x]])
                
        stdscr.refresh()

        time.sleep(1)
        playground = update_pg(playground)   
    stdscr.getkey()

""" Returns a representation of playground as a list of list of
integers (0 or 1) after verifying the content. """
def pg_from_json(json_path):
    json_f = open(json_path)
    json_val = json.loads(json_f.read())
    json_f.close()
    
    pg_h = json_val["gol_init_state"]["size"]["height"]
    pg_w = json_val["gol_init_state"]["size"]["width"]

    content = json_val["gol_init_state"]["content"]

    # Verify the size of the playground
    if not len(content) == pg_h:
        print("ERROR: Content size verification failed expected height: {}, got: {}" % (len(content), pg_h))
        
    for h in range(pg_h):
        if not len(content[h]) == pg_w:
            print("ERROR: Content size verification, line {}'s expected width: {}, got: {}" %(h, pg_w, len(content[h])))

    # All verifications passed, return the values
    return content

""" Generates and returns a random playground of specified shape
(PG_W_DEF, PG_H_DEF) """
def gen_rand_pg(h, w):
    playground = []
    for y in range(0, h):
        playground.append([])
        for x in range(0, w):
            playground[y].append(randint(0,1))
    return playground

def gol(init_type="random", json_path=None, h=None, w=None, debug=False):
    global playground
    global pg_h
    global pg_w
    global enable_dbg
    
    # Create the playground
    if init_type == "random":
        assert (h != None and w != None), "No shape for the playground supplied, (pg_h=32, pg_w=32)"
        playground = gen_rand_pg(h, w)
        pg_h = h
        pg_w = w
    elif init_type == "json":
        assert json_path != None, "No JSON file path specified (json_path="")"
        playground = pg_from_json(json_path)

        # Infer the size from the playground
        pg_h = len(playground)
        pg_w = len(playground[0])

    enable_dbg = debug
    
    # Initialize the program
    curses.wrapper(entrypoint)

if __name__ == '__main__':
    json_path = input("Please enter the complete path to the JSON file> ")
    gol(init_type="json", json_path=json_path, debug=True)
