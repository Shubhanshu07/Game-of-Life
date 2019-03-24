Conway's Game of Life
---------------------

Implementation of Conway's Game of Life for 2019 GSoC application for
JDE Robots.
Installation Instruction
------------------------
```shell
# make virutal Environment
pip3 install .
```

To run test
-----------------------
```shell
python3 setup.py test
```

To use as package in file
-------------------
```shell
python3
>>from jdegol import gol
>> gol(init_type="random",h=20,w=20)
```
The parameters of the gol function are <i>init_type,json_path,h,w.</i>
1. init_type="random" to take initially random values
2. init_type="json" json_path="" to parse the json file as an input
3. h corresponds to the height of the grid
4. w corresponds to the width of the grid
