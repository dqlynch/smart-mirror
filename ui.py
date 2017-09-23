from tkinter import Tk, Message
import weather
root = Tk()

# Create instance of weatherData to use
wd = weather.weatherData()

# Set the message to be the current temperature
msg = Message(root, text=wd.data[0])
msg.config(font=('times', 48))
msg.pack()

root.mainloop()
