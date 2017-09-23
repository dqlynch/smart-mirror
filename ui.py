from tkinter import *
import weather
import meme_browser
import urllib.request
from PIL import Image

def ui():
    root = Tk()
    test = 0
    url = ''
    for x in meme_browser.gen_urls_from_sub('me_irl'):
        ++test
        url = x
        if test == 3:
            break
    urllib.request.urlretrieve(str(url), 'meme.jpg')


    # Setup the window size
    geo_string = str(root.winfo_screenwidth()) + "x" + str(root.winfo_screenheight())
    root.geometry(geo_string)

    # Create instance of weatherData to use
    wd = weather.weatherData()

    # Add a seperator for the UI
    seperator = Frame(root, height=200, width=200)
    seperator.pack(side=LEFT)

    # Add a seperator for the meme
    meme_seperator = Frame(root, width=300)
    meme_seperator.pack(fill=Y, side=RIGHT)

    # Insert the meme of the day
    image = Image.open('meme.jpg')
    image.save('meme.png', 'PNG')
    photo = PhotoImage(file="meme.png")
    my_image = Label(meme_seperator, image=photo)
    my_image.pack()

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
