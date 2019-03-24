Conway’s Game of Life
=====================

Implementation of Conway’s Game of Life for 2019 GSoC application for
JDE Robots.

Installation Instruction
------------------------

1. Create and activate a new virtual environment
2. Install the package

::

   pip3 install .

To run tests
------------

To run the tests execute

::

   python3 setup.py test

Using jdegol as a package
-------------------------

::

   >> from jdegol import gol
   >> gol(init_type="random",h=20,w=20) # for a random grid
   >> gol(init_type="json", json_path="path/to/a/json/file.json") # for grid from a json file

API
---

**gol(init_type=“random”, json_path=None, h=None, w=None, debug=None)**

Parameters:

1. **``init_type``** :: *``String``*

   1. **``"random"``**: Generates a random to grid to start with and
      starts the simulation, requires ``h`` and ``w``.
   2. **``"json"``**: Reads a specified json file and starts the
      simulation, requires ``json_path``

2. **``w``** :: *``Integer``*: Positive ``Integer`` specifying the width
   of the grid.
3. **``h``** :: *``Integer``*: Positive ``Integer`` specifying the
   height of the grid.
4. **``json_path``** :: *``String``*: String specifying the path of the
   JSON file to be used.
5. **``debug``** :: *``Boolean``*: A boolean value specifying the mode
   of operation, ``True``: Print the debug information after the grid on
   each operation, ``False``: Do not print any debug information.