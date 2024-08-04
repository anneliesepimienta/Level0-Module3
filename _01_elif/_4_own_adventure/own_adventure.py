from tkinter import simpledialog, messagebox, Tk

# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story
window = Tk()
window.withdraw()

if __name__ == '__main__':

    story = simpledialog.askstring(title="", prompt="wanna hear a story?")
    if story == "yes":
        story_1 = simpledialog.askstring(title="", prompt="okeydokey! here we go............................there was a cat...what do you think the cat's name should be? Bob, pesky, or, yada?")
        if story_1 == "Bob":
            messagebox.showinfo(title="", message="okeydokey, bob it is!")
            story_1_2 = simpledialog.askstring(title="", prompt="bob was lying in the sun! then what happens? does bob get really hot then burn to death(unrealistically), or the sun is actually a beam of light from an alien spaceship, and he gets taken away by the alien creatures?")
            if story_1_2 == "bob gets really hot then burn to death":
                messagebox.showinfo(title="", message="you have officially finished the interactive story, ending with Bob's death. CONGRATULATIONS!")
            elif story_1_2 == "the sun is actually a beam of light from an alien spaceship, and he gets taken away by the alien creatures":
                messagebox.showinfo(title="", message="you have officially finished the interactive story, ending with Bob's disappearance, and soon enough living in space with the aliens as a space cat pet. CONGRATULATIONS!")
            else:
                messagebox.showinfo(title="", message="there was an error in your text. please exit out and try again. please be aware that the error could have just been a typo or you not writing exactly what was in the message. for example; the message said Bob, not bob. it could also be that you are writing exactly what the message says when your supposed to be using correct grammar. for example; the message might say,  bob get really hot then burn to death(unrealistically), but it should say; bob gets really hot then burns to death")
        elif story_1 == "pesky":
            messagebox.showinfo(title="", message="sorry but you actually really only have one choice! hehehhehehehhehehehehhehehehehehehehehehhehehehehehhehehehehehehehehehehehehhehehehehhehehehehehehehehehehehehehehehhehehhehehehhehehehehhehehehehhehehehehehheehhehehhehehhe!")
        elif story_1 == "yada":
            messagebox.showinfo(title="", message="sorry but you actually really only have one choice! hehehhehehehhehehehehhehehehehehehehehehhehehehehehhehehehehehehehehehehehehhehehehehhehehehehehehehehehehehehehehehhehehhehehehhehehehehhehehehehhehehehehehheehhehehhehehhe!")
        else:
            messagebox.showinfo(title="", message="there was an error in your text. please exit out and try again. please be aware that the error could have just been a typo or you not writing exactly what was in the message. for example the message said Bob not bob")
    elif story == "no":
        story_2 = simpledialog.askstring(title="", prompt="Well sucks for you! Here we go.............................There was a cat...What do you think the cat's name should be? Bob, pesky, or yada?")
        if story_2 == "Bob":
            messagebox.showinfo(title="", message="sorry but you actually really only have one choice! hehehhehehehhehehehehhehehehehehehehehehhehehehehehhehehehehehehehehehehehehhehehehehhehehehehehehehehehehehehehehehhehehhehehehhehehehehhehehehehhehehehehehheehhehehhehehhe!")
        elif story_2 == "pesky":
            messagebox.showinfo(title="", message="okeydokey, pesky it is!")
            story_2_2 = simpledialog.askstring(title="", prompt="pesky was lying in the sun! then what happens? does pesky get really hot then burn to death(unrealistically), or the sun is actually a beam of light from an alien spaceship, and he gets taken away by the alien creatures?")
            if story_2_2 == "pesky gets really hot then burns to death":
                messagebox.showinfo(title="", message="you have officially finished the interactive story, ending with pesky's death. CONGRATULATIONS!")
            elif story_2_2 == "the sun is actually a beam of light from an alien spaceship, and he gets taken away by the alien creatures":
                messagebox.showinfo(title="", message="you have officially finished the interactive story, ending with pesky's disappearance, and soon enough living in space with the aliens as a space cat pet. CONGRATULATIONS!")
            else:
                messagebox.showinfo(title="", message="there was an error in your text. please exit out and try again. please be aware that the error could have just been a typo or you not writing exactly what was in the message. for example; the message said Bob, not bob. it could also be that you are writing exactly what the message says when your supposed to be using correct grammar. for example; the message might say,  pesky get really hot then burn to death(unrealistically), but it should say; pesky gets really hot then burns to death")
        elif story_2 == "yada":
            messagebox.showinfo(title="", message="sorry but you actually really only have one choice! hehehhehehehhehehehehhehehehehehehehehehhehehehehehhehehehehehehehehehehehehhehehehehhehehehehehehehehehehehehehehehhehehhehehehhehehehehhehehehehhehehehehehheehhehehhehehhe!")
        else:
            messagebox.showinfo(title="", message="there was an error in your text. please exit out and try again. please be aware that the error could have just been a typo or you not writing exactly what was in the message. for example; the message said Bob, not bob")
    else:
        messagebox.showinfo(title="", message="there was an error in your text. please exit out and try again. please be aware that the error could have just been a typo or you not writing exactly what was in the message. for example the message said Bob not bob")
