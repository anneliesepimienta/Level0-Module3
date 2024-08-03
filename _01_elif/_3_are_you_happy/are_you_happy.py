from tkinter import Tk, simpledialog, messagebox

if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements
    window = Tk()
    window.withdraw()
    happiness_meter = simpledialog.askstring(title="", prompt="Are you happy? yes or no?")
    if happiness_meter == "yes":
        messagebox.showinfo(title="", message="keep doing whatever your doing")
    elif happiness_meter == "no":
        happiness_meter_2 = simpledialog.askstring(title="", prompt="Do you want to be happy? yes or no?")

        if happiness_meter_2 == "yes":
            messagebox.showinfo(title="", message="Change something")
        elif happiness_meter_2 == "no":
            messagebox.showinfo(title="", message="Keep doing whatever your doing")
        else:
            messagebox.showinfo(title="", message="there was an error in your text. Please exit out and try again")
    else:
        messagebox.showinfo(title="", message="there was an error in your text. please exit out and try again")