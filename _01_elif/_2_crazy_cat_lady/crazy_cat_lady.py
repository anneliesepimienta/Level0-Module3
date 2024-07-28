from tkinter import simpledialog, messagebox, Tk
import webbrowser


# Use this function to play a video from the internet
def play_video(url):
    webbrowser.open(url)

# =================== DO NOT MODIFY THE CODE ABOVE ===========================

if __name__ == '__main__':
    frog = "https://dai.ly/x1xuy7v"
    cat_video = "https://youtu.be/wzqygKSJqEY?si=Qzt4UZWHZ4iEakw9"
    dancing_cat = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExajl0dmRtMGgxcHk2NWJzMDJ0dXJkMzZwdmd4b2Q1eXhwZzd5dHlweSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/BK1EfIsdkKZMY/giphy.gif"
    window = Tk()
    window.withdraw()
    number = int(2.3)
    print(number)
    cats = simpledialog.askstring(title = "", prompt = "How many cats do you have? 3 or more, less than 3 but more than 0, or 0?")
    if cats == "3 or more":
        messagebox.showinfo(title = "", message = "your a crazy cat person!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    elif cats == "less than 3 but more than 0":
        play_video(cat_video)
    elif cats == "0":
        play_video(frog)
    else:
        play_video(dancing_cat)
    # TODO 1) Make a new window variable, window = Tk()
    #      2) Hide the window using the window's .withdraw() method
    #      3) Ask the user how many cats they have
    #      4) If they have 3 or more cats, tell them they are a crazy cat lady
    #      5) If they have less than 3 cats AND more than 0 cats, call the
    #         play_video function below to show them a cat video
    #      6) If they have 0 cats, show them a video of A Frog Sitting on a
    #         Bench Like a Human
        print("h")




