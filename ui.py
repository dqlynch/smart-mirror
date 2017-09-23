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
            urllib.request.urlretrieve(str(url), 'meme.jpg')

        # Create instance of weatherData to use
        wd = weather.weatherData()

        s_width = self.winfo_screenwidth()
        s_height = self.winfo_screenheight()

        image = Image.open('meme.jpg')
        image.save('meme.png', 'PNG')
        photo = PhotoImage(file="meme.png")
        my_image = Label(self, image=photo)
        my_image.image = photo
        my_image.grid(row=4, column=0)

        disp_time = Message(self, text=time.strftime("%H:%M:%S"))
        disp_time.config(width=250, font=('times', 16))
        disp_time.grid(row=0, column=0)

        # Set the message to be the current temperature
        msg = Message(self, text=wd.data[0])
        msg.config(width=250, font=('times', 16), anchor=N)
        msg.grid(row=0, column=1)


if __name__ == "__main__":
    root = ui()
    root.mainloop()
