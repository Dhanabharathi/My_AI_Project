

import pathlib


parent_directory = ((pathlib.Path(__file__)).parent).parent
Reference_folder = parent_directory.joinpath("Reference")
filepath = Reference_folder.joinpath("Sample_book.txt")

matrix_2 = Reference_folder.joinpath("co_occ_mat_win_2.npy")
matrix_3 = Reference_folder.joinpath("co_occ_mat_win_3.npy")
matrix_4 = Reference_folder.joinpath("co_occ_mat_win_4.npy")
