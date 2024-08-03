from tkinter import simpledialog, messagebox, Tk

# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story
window = Tk()
window.withdraw()

if __name__ == '__main__':

    story = simpledialog.askstring(title="", prompt = "wanna hear a story?")
    if story == "yes":
        story_1 = simpledialog.askstring(title="", prompt="okeydokey! here we go............................there was a cat...what do you think the cat's name should be? Bob, pesky, or, yada?")
        if story_1 == "Bob":
            messagebox.showinfo(title="", message="okeydokey, bob it is!")
        elif story_1 == "pesky":
            messagebox.showinfo(title="", message="okeydokey, pesky it is!")
        elif story_1 == "yada":
            messagebox.showinfo(title="", message="okeydokey, yada it is!")
        else:
            messagebox.showinfo(title="", message="there was an error in your text. please exit out and try again. please be aware that the error could have just been a typo or you not writing exactly what was in the message")
    elif story =="no":
        story_2 = simpledialog.askstring(title="", prompt="Well sucks for you! Here we go.............................There was a cat...What do you think the cat's name should be? Bob, pesky, or yada?")
        if story_2 == "Bob":
            messagebox.showinfo(title="", message="okeydokey, bob it is!")
        elif story_2 == "pesky":
            messagebox.showinfo(title="", message="okeydokey, pesky it is!")
        elif story_2 == "yada":
            messagebox.showinfo(title="", message="okeydokey, yada it is!")
        else:
            messagebox.showinfo(title="", message="there was an error in your text. please exit out and try again. please be aware that the error could have just been a typo or you not writing exactly what was in the message")