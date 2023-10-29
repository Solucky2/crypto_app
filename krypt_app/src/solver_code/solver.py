from krypt_app.src.messages.dics import *
import numpy as np


def solve_afinic_code(par1: str, par2: str, out1: str, out2: str):
    x = set1.get(par1)
    y = set1.get(par2)
    out1 = set1.get(out1)
    out2 = set1.get(out2)
    for a in range(26):
        for b in range(26):
            res1 = (a*x+b) % 26
            res2 = (a*y+b) % 26
            if res1 == out1 and res2 == out2:
                print({'a': a, 'b': b})


def solve_digram(par1: str, par2: str, out1: str, out2: str):
    par_1_num = [set1.get(i) for i in par1]
    par_2_num = [set1.get(i) for i in par2]
    x = par_1_num[0]*26+par_1_num[1]
    y = par_2_num[0]*26+par_2_num[1]
    out1_num = [set1.get(i) for i in out1]
    out2_num = [set1.get(i) for i in out2]
    out1 = out1_num[0]*26+out1_num[1]
    out2 = out2_num[0]*26+out2_num[1]
    for a in range(676):
        for b in range(676):
            res1 = (a*x+b) % 676
            res2 = (a*y+b) % 676
            if res1 == out1 and res2 == out2:
                print({'a': a, 'b': b})


def solve_matrix(par1: str, par2: str, out1: str, out2: str):
    par_1_num = [set1.get(i) for i in par1]
    par_2_num = [set1.get(i) for i in par2]
    out1_num = [set1.get(i) for i in out1]
    out2_num = [set1.get(i) for i in out2]
    array_keys_text_public = np.transpose(np.array([par_1_num, par_2_num]))
    array_keys_text_decoded = np.transpose(np.array([out1_num, out2_num]))
    det_keys_decoded = round(np.linalg.det(array_keys_text_decoded))
    det_keys_decoded_modulo = det_keys_decoded % len(set1)
    modulo_reverse = pow(det_keys_decoded_modulo, -1, len(set1))
    array_keys_text_decoded_list = []
    for row in array_keys_text_decoded:
        for number in row:
            array_keys_text_decoded_list.append(number)
    array_keys_text_decoded_reverse = np.array([
        [array_keys_text_decoded_list[3], array_keys_text_decoded_list[1]*-1],
        [array_keys_text_decoded_list[2]*-1, array_keys_text_decoded_list[0]]])
    array_keys_text_decoded_reverse = array_keys_text_decoded_reverse*modulo_reverse
    c_final = []
    for row in array_keys_text_decoded_reverse:
        for num in row:
            if num < 0:
                while num < 0:
                    num += len(set1)
                c_final.append(num)
            elif num > len(set1):
                while num > len(set1):
                    num -= len(set1)
                c_final.append(num)
            else:
                c_final.append(num)

    c_final = np.array(c_final)
    c_final = c_final.reshape(2, -1)
    arr_splited1, arr_splited2 = np.split(c_final, [1], axis=1)
    arr_splited1 = np.array([[arr_splited1[0, 0]*array_keys_text_public[0, 0] +
                              arr_splited1[1, 0]*array_keys_text_public[0, 1]],
                             [arr_splited1[0, 0]*array_keys_text_public[1, 0] +
                              arr_splited1[1, 0]*array_keys_text_public[1, 1]]])
    arr_splited2 = np.array([[arr_splited2[0, 0]*array_keys_text_public[0, 0] +
                              arr_splited2[1, 0]*array_keys_text_public[0, 1]],
                             [arr_splited2[0, 0]*array_keys_text_public[1, 0] +
                              arr_splited2[1, 0]*array_keys_text_public[1, 1]]])
    final_array = np.concatenate([arr_splited1, arr_splited2], axis=1)
    final_array_out = []
    for row in final_array:
        for number in row:
            final_array_out.append(number % len(set1))
    final_array_out = np.array(final_array_out)
    final_array_out = final_array_out.reshape(2, -1)
    print("Macierz rozszyfrowująca: ")
    print(final_array_out)
