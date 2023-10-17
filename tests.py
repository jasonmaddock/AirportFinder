"""
Used to test the airport finder app. Bypasses the GUI and feeds the coordinates
of each airport into logic as the user input. The console will print the name of
the airport fed as a user query, followed by the name of the closest airport,
it's coordinates and the distance. In a successful case Each airport will match
with itself and the distance between the user input and the airport will be
zero.
"""


from guiinterface import guiresult
from csvhandler import csvreader
from distancecalculator import distcalc

airports = csvreader('uk_airport_coords.csv')
testcoords = airports
for i in testcoords:
    print(f"{i[0]}: {distcalc(airports, (float(i[2]),float(i[3]))) }")
