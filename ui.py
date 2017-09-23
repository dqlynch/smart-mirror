from tkinter import *
import weather

def ui():
    root = Tk()
    # Setup the window size
    geo_string = str(root.winfo_screenwidth()) + "x" + str(root.winfo_screenheight())
    root.geometry(geo_string)

    # Create instance of weatherData to use
    wd = weather.weatherData()

    # Add a seperator for the UI
    seperator = Frame(root, height=200)
    seperator.pack(fill=X, side=TOP)

    # Set the message to be the current temperature
    title = Message(seperator, text='Current Temperature: ')
    title.config(width=250, font=('times', 16))
    title.pack(side=LEFT)

    msg = Message(seperator, text=wd.data[0])
    msg.config(width=250, font=('times', 16))
    msg.pack(side=LEFT)

    root.mainloop()

if __name__ == "__main__":
    ui()
