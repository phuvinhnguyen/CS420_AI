OUR CODE STRUCTURE:
- input:
    + mapx_y.txt #where x is map size and y is the index
- output:
    + move.gif: #this is file display the way how the game happen
    + o.txt: 
- main.py #this file is used to run our project

HOW TO RUN OUR CODE:

- move to TreasureIsland folder
- open main.py
- in line 14 and 15, we have INPUT_FILE(path to input file) and OUTPUT_FILE(path to output file), default we will run a file in our input folder and output to the output folder. You can change the path to run your own map
- to see the result, you can open and see in move.gif(visualization) or log.txt in output folder
- notice about gif file: The color will be darker if agent know that tile cannot have treasure