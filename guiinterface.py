"""
Creates the GuiInterface() object which manages the GUI. The object is built
using the tkinter module built into python and dates two inputs: The TKinter
instance and a tuple or a list. When successfully executed, the object will take
a tuple containing a list of strings and a string to be displayed in the GUI.
When unsucessful the object will take a list, displaying the string from the
second position of that list.

contains a function that a tuple or a list and uses it to create the
GuiInterface object.
"""


import tkinter as tk
from errorhandler import errorhandler

class GuiInterface(tk.Frame):
    """Used to create the GUI. Takes two arguements, an instance of TKinter and
    a tuple or a list. The tuple contains a list with three items followed by a
    string. These are used populate the results f string below. If the list is
    fed (with the first list item being "error"), the object will populate the
    results section with the second string in the list.

    The tkinter instance takes labels, entries and buttons to populate the GUI,
    the absolute place method of tkinter was used to place these elements on
    the page. On a button press, the object returns the values in the latfield
    and lonfield entries to its coordinates function before quiting.

    """
    def __init__(self, parent, message):
        tk.Frame.__init__(self, parent)
        self.message = message

        #---- Labels -----
        mainlabel= tk.Label(root, text="""Please enter your current
coordinates below:""", font=("Helvetica", 16))
        mainlabel.place(x=25, y=10)
        latlabel = tk.Label(root, text="Latitude", font=("Helvetica", 9))
        latlabel.place(x=50, y=70)
        lonlabel = tk.Label(root, text="Longitude", font=("Helvetica", 9))
        lonlabel.place(x= 170, y=70)

        #---- Entries -----
        latfield= tk.Entry(root, bd=5)
        latfield.place(x=50, y=90, width=80)
        lonfield= tk.Entry(root, bd=5)
        lonfield.place(x= 170, y=90, width=80)

        #---- Button -----
        btn= tk.Button(root, text="Return Closest Airport", command= lambda:
        [self.coordinates(latfield.get(), lonfield.get()), root.quit()])
        btn.place(x=85, y=130, width= 130)

        #---- Results -----
        reslabel = tk.Label(root, text="Results:", font=("Helvetica", 14))
        reslabel.place(x=25, y=170)
        if message[0] != "error":
            outlabel = tk.Label(root, text=f"""Airport: {message[0][0]}
Latitude: {message[0][2]}
Longitude: {message[0][3]}
Distance(Km): {message[1]}""", font=("Helvetica", 9), justify="left")
        else:
            outlabel = tk.Label(root, text=f"{message[1]}",
            font=("Helvetica", 9), justify="left")
        outlabel.place(x=25, y=200)

        root.title('Airport Finder')
        root.geometry("300x280+10+10")

    def coordinates(self, latfield, lonfield):
        """Takes two strings from the GuiInterface object and converts them to
        floats if possible and makes them gloabl variables as they cannot be
        returned from within the tkinter object. if the strings cannot be
        converted to a float then the gloabl errors variable has a ValueError
        assigned to it.
        """
        global lat
        global lon
        global errors
        try:
            lat = float(latfield)
            lon = float(lonfield)
            errors = ""
        except ValueError:
            errors = "uiValueError"
        if lat > 90 or lat < -90 or lon > 180 or lon < -180:
            errors = "uiValueError"

def guiresult(message):
    """Instantiates the TKinter object, feeding it the tkinter root and a tuple
    or a list. If the user closes the application, this function will print a
    message to the console and quit the script. If any errors are assigned to
    the gloabl errors variable they will be fed to the errorhandler function in
    the errorhandler module. Otherwise, this function will return the floated
    latitude and longitude.
    """
    try:
        GuiInterface(root, message).pack(side="top", fill="both", expand=True)
        root.mainloop()
    except tk.TclError:
        print("Application closed by user")
        quit()
    global errors
    if errors != "":
        return errorhandler(errors)
    else:
        try:
            return(lat,lon)
        except NameError:
            print("Application closed by user")
            quit()

errors = ""
root = tk.Tk()
