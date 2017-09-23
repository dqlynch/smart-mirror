#!/usr/bin/env python3

from tkinter import *
import weather
import meme_browser
import urllib.request
from PIL import Image
import time

class ui(Tk):
    def __init__(self):
        Tk.__init__(self)
        url = ''
        for x in meme_browser.gen_urls_from_sub('me_irl'):
            url = x
            break;
        urllib.request.urlretrieve(str(url), 'meme.jpg')

        # Set the monitor to fullscreen
        s_width = self.winfo_screenwidth()
        s_height = self.winfo_screenheight()
        geo_string = str(s_width) + "x" + str(s_height)
        self.geometry(geo_string)

        # Create instance of weatherData to use
        wd = weather.weatherData()

        text_frame = Frame(self, bg="#000000")
        text_frame.pack(fill=X)

        seperator = Frame(self, bg="#000000")
        seperator.pack(fill=BOTH, expand=1)

        # Get the image and resize it
        image = Image.open('meme.jpg')
        image = image.resize((int(s_width/2 - 50), int(s_height/2 - 50)), Image.ANTIALIAS)
        image.save('meme.png', 'PNG')
        photo = PhotoImage(file="meme.png")
        self.my_image = Label(seperator, image=photo, anchor=W, bg="#000000")
        self.my_image.image = photo
        self.my_image.pack(fill=BOTH, side=BOTTOM)

        # Display the time
        self.disp_time = Message(text_frame, text=time.strftime("%H:%M:%S"))
        self.disp_time.config(width=250, font=('times', 16))
        self.disp_time.pack(side=LEFT, fill=X)

        # Set the message to be the current temperature
        msg = Message(text_frame, text=wd.data[0])
        msg.config(width=250, font=('times', 16))
        msg.pack(side=RIGHT, fill=X)

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.disp_time.configure(text=now)
        self.after(1000, self.update_clock)

if __name__ == "__main__":
    root = ui()
    root.update_clock()
    root.mainloop()
