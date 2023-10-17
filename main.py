"""
The main file of the Airport Finder application. If this file is run directly it
will use the functions and classes outlined in its accompanying modules to read
data from a .csv file including airports and their coordinates, create a Gui
to capture a set of user input coordinates and then calculate the ground
distance between the two coordinates. The closest airport to the user input
and the distance to that airport will be returned and displayed in the GUI.
The script will also handle any errors that may occur throughout it's function.

The script requires the following modules to function:
guiinterface
csvhandler
distancecalculator
"""


import tkinter as tk
from guiinterface import guiresult
from csvhandler import csvreader
from distancecalculator import distcalc

if __name__ == "__main__":
    x = 1
    airports = csvreader('uk_airport_coords.csv')
    if airports[0] != "error":
        message = (["","","",""],"")
    else:
        message = airports
    while x == 1:
        input = guiresult(message)
        if input[0] != "error":
            result = distcalc(airports, input)
        else:
            result = input
        message = result
        #guiresult()
