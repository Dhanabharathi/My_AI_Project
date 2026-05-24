import tkinter as Tk
import pathlib
from learning.Ngram_and_NextWord_Prediction import My_book_AI

parent_directory = ((pathlib.Path(__file__)).parent).parent
Reference_folder = parent_directory.joinpath("Reference")
filepath_1 = Reference_folder.joinpath("Sample_book.txt")


def print_input(event):
    a = entry.get()
    a = a.lower()
    prediction = My_book_AI.Prediction_process(a, filepath_1)
    entry_1.delete("1.0", Tk.END)
    for k in prediction[2]:
        entry_1.insert(Tk.END, f"{k}\n")


main_win = Tk.Tk()
main_win.title("My first app in Tkinter")

entry = Tk.Entry(fg="black", bg="white", width=50, justify="left")
entry_1 = Tk.Text(fg="yellow", bg="blue", width=50, height=10)
entry_2 = Tk.Entry(fg="black", bg="white", width=50)

entry.pack()
entry_1.pack()
entry_2.pack()

entry.bind("<space>", print_input)
entry.bind("<Return>", print_input)

main_win.mainloop()
