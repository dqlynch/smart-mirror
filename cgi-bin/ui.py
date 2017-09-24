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
        # Set the monitor to fullscreen
        self.s_width = self.winfo_screenwidth()
        self.s_height = self.winfo_screenheight()
        geo_string = str(self.s_width) + "x" + str(self.s_height)
        self.geometry(geo_string)

        # Create instance of weatherData to use
        self.wd = weather.weatherData()

        # Stores the first line of text
        self.text_frame1 = Frame(self, bg="#000000")
        self.text_frame1.pack(fill=X)

        # Stores the second line of text
        text_frame2 = Frame(self, bg="#000000")
        text_frame2.pack(fill=X)

        # This is for the meme, if the user wants to show it
        self.seperator = Frame(self, bg="#000000")
        self.seperator.pack(fill=BOTH, expand=1)

        # Display the time
        self.disp_time = Message(self.text_frame1, text=time.strftime("%H:%M"),
                                 bg="#000000", fg="#FFF")
        self.disp_time.config(width=250, font=('arial', 36))
        self.disp_time.pack(side=LEFT, fill=X)

        # Set the message to be the current temperature
        self.temp = Message(self.text_frame1, text=str(self.wd.data[0]) + "°", bg="#000000", fg="#FFF")
        self.temp.config(width=250, font=('arial', 36))
        self.temp.pack(side=RIGHT, fill=X)

        # Set up the date Message
        t = time.localtime()
        date_data = time.asctime(t)
        self.date = Message(text_frame2, text=date_data[0:11], bg="#000000", fg="#FFF")
        self.date.config(width=250, font=('arial', 12), padx=12)
        self.date.pack(side=LEFT, fill=X)

        # Setup the weather max and main
        self.weather_highlow = Message(text_frame2, text=str(self.wd.data[1]) + "°/" + str(self.wd.data[0]) + "°",
                                       bg="#000000", fg="#FFF")
        self.weather_highlow.config(width=250, font=('arial', 12), padx=20)
        self.weather_highlow.pack(side=RIGHT, fill=X)

    def display_weather_icon(self):
        icon_name = ''
        if(self.wd.data[3] <= 299):
            icon_name = 'static/storm.png'
        elif(self.wd.data[3] <= 399):
            icon_name = 'static/sun_shower.png'
        elif(self.wd.data[3] <= 599):
            icon_name = 'static/water_drop.png'
        elif(self.wd.data[3] <= 699):
            icon_name = 'static/snowflake.png'
        elif(self.wd.data[3] == 800):
            icon_name = 'static/sun.png'
        elif(self.wd.data[3] <= 899):
            icon_name = 'static/white_cloud.png'
        image = Image.open(icon_name)
        image = image.resize((75, 75), Image.ANTIALIAS)
        image.save(icon_name, 'PNG')
        photo = PhotoImage(file=icon_name)
        self.icon = Label(self.text_frame1, image=photo, width=75, height=75, bg="#000000")
        self.icon.image = photo
        self.icon.pack(fill=X, side=RIGHT)

    def update_clock(self):
        am_or_pm = "am"
        h = int(time.strftime("%H"))
        if(int(time.strftime("%H")) > 12):
            h = int(time.strftime("%H")) - 12
            am_or_pm = "pm"
        now = str(h) + time.strftime(":%M") + " " + am_or_pm
        self.disp_time.configure(text=now)
        self.after(1000, self.update_clock)

    def display_meme(self):
        url = ''
        for x in meme_browser.gen_urls_from_sub('me_irl'):
            url = x
            break;
        urllib.request.urlretrieve(str(url), 'meme.jpg')

        # Get the image and resize it
        image = Image.open('meme.jpg')
        im_width, im_height = image.size
        resize_factor = 0
        if(im_height > 600):
            resize_factor = im_height/600
            new_width = int(im_width/resize_factor)
            new_height = int(im_height/resize_factor)
            image = image.resize((new_width, new_height), Image.ANTIALIAS)
        elif(im_width > 600):
            resize_factor = im_width/600
            new_width = int(im_width/resize_factor)
            new_height = int(im_height/resize_factor)
            image = image.resize((new_width, new_height), Image.ANTIALIAS)

        image.save('meme.png', 'PNG')
        photo = PhotoImage(file="meme.png")
        self.my_image = Label(self.seperator, image=photo, anchor=W, bg="#000000")
        self.my_image.image = photo
        self.my_image.pack(fill=BOTH, side=BOTTOM)


if __name__ == "__main__":
    root = ui()
    root.update_clock()
    root.display_meme()
    root.display_weather_icon()
    root.mainloop()
