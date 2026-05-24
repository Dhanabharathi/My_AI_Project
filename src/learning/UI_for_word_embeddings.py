import pathlib
import tkinter as Tk
from word_embeddings import co_occ
import numpy as npy


parent_directory = ((pathlib.Path(__file__)).parent).parent
Reference_folder = parent_directory.joinpath("Reference")
filepath = Reference_folder.joinpath("Sample_book.txt")

word_index,matrix = co_occ.co_occurance_matix(filepath,2)

#npy.save(r"D:\all_Python_code\My_AI_project\Reference\co_occ_mat_win_4",matrix)


def matrix_prediction(event):
    input_txt= entry.get()
    input_txt = input_txt.lower()
    input_txt = input_txt.split()
    lenght = len(input_txt)
    if not input_txt:
        entry_1.delete("1.0",Tk.END)
        entry_1.insert("1.0","Please enter word")
        return
    
    frequency = {} 
    word= input_txt[lenght-1]
    if word in word_index:
        index = word_index[word]
    else:
        entry_1.delete("1.0",Tk.END)
        entry_1.insert("1.0",f"'{word}' not found in vocabulary matrix.")
        return
    row_of_input_word = matrix[index]
    for idx_word, k in word_index.items():
            #print("word",idx_word,"--",k,"<-->",row_of_input_word[k])
            frequency[idx_word] = int(row_of_input_word[k])
    highest_possibility= sorted(frequency.items(),key=lambda items:items[1],reverse=True)[:50]
    entry_1.delete("1.0",Tk.END)
    entry_1.insert("1.0",f"{highest_possibility}")

main_win = Tk.Tk()
main_win.title("Matrix prediction")

entry = Tk.Entry(fg="black", bg="white", width=50,justify="left")
entry_1 = Tk.Text(fg="yellow", bg="blue", width=70,height=20)
entry_2 = Tk.Entry(fg="black", bg="white", width=50)

entry.pack()
entry_1.pack()
entry_2.pack()

entry.bind("<space>",matrix_prediction)

main_win.mainloop()