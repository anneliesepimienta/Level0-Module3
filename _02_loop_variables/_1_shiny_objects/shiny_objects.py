from tkinter import simpledialog, Tk
from playsound import playsound

can_play_sounds = True


def play_mister_zee():
    if can_play_sounds:
        playsound('shiny-objects.wav')
    else:
        print("Mister Zee requires shiny objects")


def many_shiny_objects():
    # TODO 1) Call the method above to play Mister Zee
    play_mister_zee()
    # TODO 2) Ask the user how many shiny objects they want
    user_input = simpledialog.askstring(title="", prompt="how many shiny objects would you like!?")
    number_of_objects = int(user_input)
    # TODO 3) Play the sound that many times
    for i in range(number_of_objects):
        play_mister_zee()



if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    many_shiny_objects()
