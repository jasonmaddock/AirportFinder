# Airport Finder
The Airport Finder application is used to determine the closest airport to the input coordinates. The application takes two user inputs and a .csv file input. The user inputs are latitude and Longitude coordinates. The .csv file contains a list of airports and their corresponding coordinates. The application will calculate the ground distance between the user coordinates and each airport in the .csv, before returning the closest airport and the ground distance to that airport to the GUI. The application is built in Python 3 using only built-in modules.

# Installation
After downloading the Airport Finder.zip file. Extract the files contents to where you would like the application to be installed. The application will require Python3 and to be installed and added to PATH in order to run.

#Function
The application is designed to find the ground distance between the user input coordinates and the airports stored in the uk_airport_coords.csv file. The application will open a GUI to receive the user coordinates. Once received the application will take the user coordinates along with the each airport coordinates and use the Haversine formula to determine the ground distance between the two points. Once calculated the application will return the closest airport name, its coordinates and its distance. This information will be displayed in the GUI as below.

Airport: SHOREHAM
Latitude: 50.835556
Longitude: -0.297222
Distance(Km): 130.69

# Use
Before running the application, the user can add their list of airports to the .csv file provided. The user is able to skip this step as there are airports loaded into the .csv file at the point of installation. The data in the csv file requires the following columns in order NAME, ICAO, Latitude, Longitude. If the data is not loaded correctly, a apValueError will be returned to the GUI. This is outlined further in the error messages section below. Below is example data from uk_airport_coords.csv.

NAME,	ICAO,	Latitude,	Longitude
HONINGTON,	EGXH,	52.342611,	0.772939
WELSHPOOL,	EGCW,	52.628611,	-3.153333

Once the uk_airport_coords.csv has been configured, the application is run by using the command python main.py in the windows terminal while in the directory containing the application.

# Error messages
There are five error types that the script can encounter. These errors will require the user to close the program and check the .csv input or change their input. These errors are outlined in the table below:

____________________________________________________________________________
Error Name             | Result of error        |Cause of error            |
_______________________|________________________|__________________________|
uiValueError           |Error message will ask  |illegal entry in          |
                       |the user to correct     |the latitude or longitude |
                       |their GUI input.        |GUI fields.               |
_______________________|________________________|__________________________|
FileBlankError         |Error message will ask  |The source file is empty. |
                       |the user to fill the    |                          |
                       |.csv file.              |                          |
_______________________|________________________|__________________________|
FileNotFoundError      |Ask the user to check   |The script cannot find    |
                       |the location of the     |"uk_airport_coords.csv"   |
                       |.csv file.              |in its directory.         |
_______________________|________________________|__________________________|
apValueError           |Error message will ask  |Unexpected data in the    |
                       |the user to check the   |latitude or longitude     |
                       |contents of the .csv.    |columns of the .csv.     |
_______________________|________________________|__________________________|
NoDataError            |Error message will ask  |.csv file contains headers|
                       |the user to check the   |but no airport data.      |
                       |contents of the .csv.   |                          |
_______________________|________________________|__________________________|

The error messages printed in the GUI are displayed below:

uiValueError: uiValueError: uiValueError: The latitude and longitude
fields can only accept numbers within accepted
range (latitude -90 - 90, longitude -180 - 180)

FileBlankError: FileBlankError: The uk_airport_coords.csv
file is blank. Please add data.

FileNotFoundError: FileNotFoundError: uk_airport_coords.csv
cannot be found in the scripts directory.

apValueError: apValueError: There is an error in the
values of the input .csv file.

NoDataError: NoDataError: The uk_airport_coords.csv
file only contains headers. Please add data.

#Tests
The unit test will feed the coordinates airports from the uk_airport_coords.csv into the app as the user input, bypassing the GUI. The console will print the name of the airport fed as a user query, followed by the name of the closest airport, it's coordinates and the distance. In a successful case Each airport will match with itself and the distance between the user input and the airport will be zero.

The test is run by using the command python tests.py in the windows terminal while in the directory containing the application.
