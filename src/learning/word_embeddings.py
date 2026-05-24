import numpy as npy
import pathlib
import scipy as spy

from Ngram_and_NextWord_Prediction import My_book_AI



parent_directory = ((pathlib.Path(__file__)).parent).parent
Reference_folder = parent_directory.joinpath("Reference")
filepath = Reference_folder.joinpath("Sample_book.txt")


class co_occ():
    @staticmethod
    def co_occurance_matix(data_path,Window_size):
        token = My_book_AI.clean_data(data_path)
        #word_count = My_book_AI.word_frequency_counter(token)
        Unique_words = sorted(set(token))
        length_of_unique_words = len(Unique_words)
        maxtrix = npy.zeros((length_of_unique_words,length_of_unique_words),dtype=int)
        word_index = {}
        for index,word in enumerate(Unique_words):
            word_index[word] = index

        for i in range(len(token)):
            word_start = max(0,(i-Window_size))
            word_end = min((len(token)),(i+1+Window_size))
            target_word = token[i]
            #print("target = ",target_word)
            for j in range(word_start,word_end):
                if i !=j:
                    context_word = token[j]
                    #print("context =",context_word)
                    #print(token[i],"<--->",token[j])
                    target_word_ixd = word_index[target_word]
                    context_word_ixd = word_index[context_word]
                    maxtrix[(target_word_ixd,context_word_ixd)] +=1
                    maxtrix[(context_word_ixd,target_word_ixd)] +=1
        return word_index,maxtrix

uniques_wrd,maxtrix = co_occ.co_occurance_matix(filepath,2)

"""class vector_creation():
    @staticmethod
    def unique_wrdVec():
        uniques_wrd,maxtrix = co_occ.co_occurance_matix(filepath,2)

        return 
    

print(vector_creation.unique_wrdVec())"""