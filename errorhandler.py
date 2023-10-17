"""
Used to handle errors that may be thrown during the process of the script.
errortext is a dictionary containing five distinct error names as keys and they
error message as values. Contains one function errorhandler. Takes a string and
uses it as a key to retrieve a value from the errortext dictionary before
returning a list with two strings.
"""

errortext = {
"uiValueError": """uiValueError: The latitude and longitude
fields can only accept numbers within accepted
range (latitude -90 - 90, longitude -180 - 180).""",
"apValueError": """apValueError: There is an error in the
values of the input .csv file.""",
"FileNotFoundError": """FileNotFoundError: uk_airport_coords.csv
cannot be found in the scripts directory.""",
"NoDataError": """NoDataError: The uk_airport_coords.csv
file only contains headers. Please add data.""",
"FileBlankError": """FileBlankError: The uk_airport_coords.csv
file is blank. Please add data."""
}

def errorhandler(errortype):
    """Takes a string and uses it as a key to retrieve a value from the
    errortext dictionary before returning a list with two strings.
    """
    errormsg = errortext[errortype]
    return "error", errormsg
