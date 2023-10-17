"""
Contains one function which takes a string as an arguement. It will attempt
to open a file with the name of the passed arguement if it exists within the
scripts directory. The function will extract the files contents and return it.
Three errors are watched for within the function
"""

import csv
from errorhandler import errorhandler

def csvreader(filename):
    """Takes the filename string as an arguement. The function attempts to open
    the file unless there is a FileNotFoundError. The function then uses the csv
    module to extract the contents of the file and list comprehension to create
    a list of lists. Each of the nested lists containing two strings in the
    first two positions and two floats in the second two. this data is returned
    with the table headers removed. If the file is blank, a FileBlankError is
    thrown. If the file contains only headers a NoDataError is thrown. Any
    thrown errors are fed into the errorhandler function in the errorhandler
    module and the output of that function is returned.
    """
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            contents = [row for row in reader]
            if contents == [[]]:
                return errorhandler("FileBlankError")
            elif contents[1:] == []:
                return errorhandler("NoDataError")
    except FileNotFoundError:
        return errorhandler("FileNotFoundError")
    return(contents[1:])
