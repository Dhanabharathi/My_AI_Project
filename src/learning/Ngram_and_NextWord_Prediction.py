import re
from collections import defaultdict
import collections
import tkinter as Tk
import string
import pathlib

parent_directory = ((pathlib.Path(__file__)).parent).parent
Reference_folder = parent_directory.joinpath("Reference")
filepath_1 = Reference_folder.joinpath("Sample_book.txt")


class My_book_AI():
    @staticmethod                 #From here im creating all the lanaguge model necessary iteams
    def clean_data(filepath):
        with open (filepath,'r') as target_dataset:
            try:
                read_data = target_dataset.read()
                read_data = re.sub(r'https?://\S+|www\.\S+', '', read_data)
                read_data = re.sub(r"[^a-zA-Z ]","", read_data)
                read_data = read_data.lower()
                read_data = re.sub(r'\s+', ' ', read_data).strip()
                read_data = read_data.split()
                return read_data 
            except Exception as e:
                print("not possible",e)
                return e

    @staticmethod
    def N_gram(tokens, N):
        ngram_dict = defaultdict(list)
        for i in range(len(tokens) - N):
            ngram = tuple(tokens[i:i+N])
            next_word = tokens[i+N]
            ngram_dict[ngram].append(next_word)
        return ngram_dict

    @staticmethod
    def word_frequency_counter(tokens):
        counter = collections.Counter(tokens)
        return dict(counter)
                   
    @staticmethod
    def Prediction_process(input_text,data_path):
        if not input_text.strip():
            return input_text,0,["space"]
        input_text = input_text.lower()
        input_text = re.sub(r"[^a-zA-Z ]","",input_text)
        input_text= tuple(input_text.split())
        #print(input_text)

        input_grams_size = len(input_text)

        book_N_gram = My_book_AI.N_gram(My_book_AI.clean_data(data_path),input_grams_size)

        if input_text in book_N_gram:
            predicted_word = set(book_N_gram[input_text])
            #print(predicted_word)

        else:
            predicted_word=["Not predictable"]
            return input_text,input_grams_size,predicted_word

        return input_text,input_grams_size,predicted_word