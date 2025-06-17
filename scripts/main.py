from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import threading
import usb,security,password

def home(window):
    window.title("Welcome")
    window.geometry("625x625")

    gif_path = "chill_cat.gif"
    gif = Image.open(gif_path)

    label = Label(window, bg="black")
    label.pack(expand=True)

    frames = [ImageTk.PhotoImage(frame.copy().resize((625, 625)))
              for frame in ImageSequence.Iterator(gif)]

    def animate(index):
        label.configure(image=frames[index])
        label.image = frames[index]
        window.after(100, animate, (index + 1) % len(frames))

    def open_soft():
        usb_info = usb.wait_for_usb()
        if security.verify(usb_info):
            password.main(window)
        else:
            print("Error")

    animate(0)
    threading.Thread(target=open_soft, daemon=True).start() #Task that is doing

    window.mainloop()

if __name__ == "__main__":
    window_obj = Tk()
    home(window_obj)
