from tkinter import *
from PIL import Image, ImageTk, ImageSequence

def main():
    window = Tk()
    window.title("Welcome")
    window.geometry("625x400")
    window.configure(bg="black")

    # Load the GIF using PIL
    gif_path = "chill_cat.gif"
    gif = Image.open(gif_path)

    # Create a Label to display the GIF
    label = Label(window, bg="black")
    label.pack(expand=True)

    # Extract frames from GIF using ImageSequence
    frames = [ImageTk.PhotoImage(frame.copy().resize((625, 400)))
              for frame in ImageSequence.Iterator(gif)]

    # Function to animate frames
    def update(index):
        label.configure(image=frames[index])
        label.image = frames[index]
        window.after(100, update, (index + 1) % len(frames))

    update(0)  # Start animation

    window.mainloop()

if __name__ == "__main__":
    main()
