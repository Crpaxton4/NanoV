# NanoV
Nano material visualization tool in python.

Requires Panda3D 1.10
Written in Python 3.6.0, other versions of 3 should work, but have not been tested

## Running NanoV
To run the project, type the command ```python main.py``` in the command line.

## main.py
This file contains the settings and properties of the main window. Panda3D is used to create the visualizations.

## Menu.py
This file creates the menu bar at the top of the screen as well as the drop down items. 

## StructureLibrary.py
Any structures that will be added to the system should be added to this file. The methods take three parameters which specify the size of the structure. These parameters are x, y, and z directions. They return two values as a tuple. The first value is the list of atom locations and types for the structure. The second value is the total types in that structure. The total types is used to display the correct number of options when selecting atom color.

Examples for how to test the structures can be found in the comments of that file.

## CuttingLibrary.py
The logic behind the cutting tool will be placed in this file. Currently we have an untested method to cut a sphere from a molecule, but this functionality has not be added to the GUI yet.

## setup.py
This file is used to build the executable. More info to come.
