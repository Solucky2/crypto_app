from MessageClass import EncodeMessages, SolverMessages
from solver import *
import numpy as np


class CodeTypes:

    def encode_fence_code(self, message: str, height: int):
        sheet = [["" for i in range(len(message))] for j in range(height)]
        direction = -1
        row = 0
        col = 0
        for letter in message:
            sheet[row][col] = letter
            if row == 0 or row == height-1:
                direction = -direction
            row += direction
            col += 1
        [print(layer) for layer in sheet]
        out = ''
        for layer in range(height):
            for letter in range(len(message)):
                out += sheet[layer][letter]
        print(out)

    def decode_cesar_code(self, message: str, b: int):
        out = []
        for letter in message:
            ind = set1.get(letter)
            val = (ind - b) % len(set1)
            out.append(val)
        mess = [set2[number] for number in out]
        encoded = ''.join(mess)
        print("Hasło: " + encoded)

    def encode_cezar_code(self, message: str, b: int):
        out = []
        for letter in message:
            ind = set1.get(letter)
            val = (ind + b) % len(set1)
            out.append(val)
        mess = [set2[number] for number in out]
        encoded = ''.join(mess)
        print("Hasło: " + encoded)

    def encode_modulo(self, message: str, b: int):
        outp = []
        for letter in message:
            a = set1.get(letter)
            val = (a+b) % len(set1)
            outp.append(val)
        mess = [set2[number] for number in outp]
        encoded = ''.join(mess)
        print("Hasło: " + encoded)

    def decode_modulo(self, message: str, b: int):
        outp = []
        for letter in message:
            a = set1.get(letter)
            val = (a-b) % 26
            outp.append(val)
        mess = [set2[number] for number in outp]
        encoded = ''.join(mess)
        print("Hasło: " + encoded)

    def encode_decode_module_keys(self, message: str, key1: int, key2: int):
        out = []
        for letter in message:
            a = set1.get(letter)
            val = (a*key1+key2) % len(set1)
            out.append(val)
        mess = [set2[number] for number in out]
        encoded = ''.join(mess)
        print("Hasło: " + encoded)

    def encode_decode_modulo_digram(self, message: str, a: int, b: int):
        if len(message) % 2 != 0:
            message += "Q"
        out3 = []
        sen2 = [message[i:i+2] for i in range(0, len(message), 2)]
        out = (26 * set1.get(i[0]) + set1.get(i[1]) for i in sen2)
        out2 = ((a*i + b) % 676 for i in out)
        for i in out2:
            val3 = i//len(set1)
            val4 = i % len(set1)
            out3.append(val3)
            out3.append(val4)
        mess = [set2[number] for number in out3]
        encoded = ''.join(mess)
        print("Hasło: " + encoded)

    def decode_matrix_code(self, message: str, a: int, b: int, c: int, d: int):
        if len(message) % 2 != 0:
            message += "Q"
        sen2 = [message[i:i+2] for i in range(0, len(message), 2)]
        array_keys = np.array([[a, b], [c, d]])
        out = []
        for par_of_letters in sen2:
            for letter in par_of_letters:
                letter_value_1 = set1.get(letter)
                out.append(letter_value_1)
        out_sorted_for_two = [out[i:i+2] for i in range(0, len(out), 2)]
        encoded_values = []
        for i in out_sorted_for_two:
            summed_i = np.sum(i*array_keys, axis=1)
            encoded_values.append(summed_i)
        encoded_message = []
        for i in encoded_values:
            for j in i:
                val = set2.get(j % len(set1))
                encoded_message.append(val)
        encoded = ''.join(encoded_message)
        print("Hasło: " + encoded)

    def encode_matrix_code(self, message: str, a: int, b: int, c: int, d: int):
        d_factor = a*d-c*b
        if d_factor < 0:
            d_factor += len(set1)
        d_factor = pow(d_factor, -1, len(set1))
        sen2 = [message[i:i+2] for i in range(0, len(message), 2)]
        array_keys = np.array([[d*d_factor, b*-d_factor], [c*-d_factor, a*d_factor]])
        factored_num = []
        for row in array_keys:
            for num in row:
                if num < 0:
                    while num < 0:
                        num += len(set1)
                    factored_num.append(num)
                elif num > len(set1):
                    while num > len(set1):
                        num -= len(set1)
                    factored_num.append(num)
                else:
                    factored_num.append(num)
        factored_num = np.array(factored_num)
        factored_num = factored_num.reshape(2, -1)
        print("Macierz odwrtona: ")
        print(factored_num)
        out = []
        for par_of_letters in sen2:
            for letter in par_of_letters:
                letter_value_1 = set1.get(letter)
                out.append(letter_value_1)
        out_sorted_for_two = [out[i:i + 2] for i in range(0, len(out), 2)]
        decoded_values = []
        for i in out_sorted_for_two:
            summed_i = np.sum(i*array_keys, axis=1)
            decoded_values.append(summed_i)
        encoded_message = []
        for i in decoded_values:
            for j in i:
                val = set2.get(j % len(set1))
                encoded_message.append(val)
        encoded = ''.join(encoded_message)
        print("Hasło: " + encoded)

    def create_playfair_matrix(self, message_key:str):
        # usuń powtarzające się litery i spacje
        key = message_key.replace(' ', '')
        key = ''.join(sorted(set(key), key=key.index))
        # utwórz pustą macierz 5x5
        matrix = [['' for _ in range(5)] for _ in range(5)]
        # wypełnij macierz literami klucza i litery alfabetu
        letters = key + 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        used_letters = []
        for row in range(5):
            for col in range(5):
                letter = letters[0]
                while letter in used_letters:
                    letters = letters[1:]
                    letter = letters[0]
                matrix[row][col] = letter
                used_letters.append(letter)
        # zamień litery 'j' na 'i'
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == 'J':
                    matrix[row][col] = 'I'
        [print(layer) for layer in matrix]
        return matrix

    def playfair_encrypt(self, plaintext:str, message_key: str):
        matrix = CodeTypes().create_playfair_matrix(message_key)
        plaintext = plaintext.replace(' ', '')
        plaintext = plaintext.replace('J', 'I')
        if len(plaintext) % 2 == 1:
            plaintext += 'X'
        pairs = [plaintext[i:i + 2] for i in range(0, len(plaintext), 2)]
        ciphertext = ''
        for pair in pairs:
            row1, col1 = 0, 0
            row2, col2 = 0, 0
            for i in range(5):
                for j in range(5):
                    if matrix[i][j] == pair[0]:
                        row1, col1 = i, j
                    elif matrix[i][j] == pair[1]:
                        row2, col2 = i, j
            if row1 == row2:
                ciphertext += matrix[row1][(col1 + 1) % 5]
                ciphertext += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                ciphertext += matrix[(row1 + 1) % 5][col1]
                ciphertext += matrix[(row2 + 1) % 5][col2]
            else:
                ciphertext += matrix[row1][col2]
                ciphertext += matrix[row2][col1]
        print(ciphertext)


class CodeActions:

    def cesar_code_actions_encode(self):
        try:
            message = input(EncodeMessages().input_password).upper().replace(" ", "")
            b = input(EncodeMessages().input_transition_b).replace(" ", "")
            CodeTypes().encode_cezar_code(message, int(b))
        except ValueError:
            print(EncodeMessages().messege_invalid_type)

    def cesar_code_actions_decode(self):
        try:
            message = input(EncodeMessages().input_password).upper().replace(" ", "")
            b = input(EncodeMessages().input_transition_b).replace(" ", "")
            CodeTypes().decode_cesar_code(message, int(b))
        except ValueError:
            print(EncodeMessages().messege_invalid_type)

    def fence_code_actions_encode(self):
        try:
            message = input(EncodeMessages().input_password).upper().replace(" ", "")
            height = input(EncodeMessages().input_fence_height).replace(" ", "")
            CodeTypes().encode_fence_code(message, int(height))
        except ValueError:
            print(EncodeMessages().messege_invalid_type)

    def modulo_code_actions_encode(self):
        try:
            message = input(EncodeMessages().input_password).upper().replace(" ", "")
            b = input(EncodeMessages().input_transition_b).replace(" ", "")
            CodeTypes().encode_modulo(message, int(b))
        except ValueError:
            print(EncodeMessages().messege_invalid_type)

    def modulo_code_actions_decode(self):
        try:
            message = input(EncodeMessages().input_password).upper().replace(" ", "")
            b = input(EncodeMessages().input_transition_b).replace(" ", "")
            CodeTypes().decode_modulo(message, int(b))
        except ValueError:
            print(EncodeMessages().messege_invalid_type)

    def afinic_code_encode_decode(self):
        message = input(EncodeMessages().input_password).upper().replace(" ", "")
        try:
            a = input(EncodeMessages().input_transition_a).replace(" ", "")
            b = input(EncodeMessages.input_transition_b).replace(" ", "")
            CodeTypes().encode_decode_module_keys(message, int(a), int(b))
        except ValueError:
            print(EncodeMessages().messege_invalid_type)

    def digram_code_encode_decode(self):
        message = input(EncodeMessages().input_password).upper().replace(" ", "")
        try:
            a = input(EncodeMessages().input_transition_a).replace(" ", "")
            b = input(EncodeMessages.input_transition_b).replace(" ", "")
            CodeTypes().encode_decode_modulo_digram(message, int(a), int(b))
        except ValueError:
            print(EncodeMessages().messege_invalid_type)

    def matrix_code_encode(self):
        message = input(EncodeMessages().input_password).upper().replace(" ", "")
        try:
            matrix1 = input(EncodeMessages().input_matrix_num1).replace(" ", "")
            matrix2 = input(EncodeMessages().input_matrix_num1).replace(" ", "")
            matrix3 = input(EncodeMessages().input_matrix_num1).replace(" ", "")
            matrix4 = input(EncodeMessages().input_matrix_num1).replace(" ", "")
            CodeTypes().encode_matrix_code(message, int(matrix1), int(matrix2), int(matrix3), int(matrix4))
        except ValueError:
            print(EncodeMessages().messege_invalid_type)

    def matrix_code_decode(self):
        message = input(EncodeMessages().input_password).upper().replace(" ", "")
        try:
            matrix1 = input(EncodeMessages().input_matrix_num1).replace(" ", "")
            matrix2 = input(EncodeMessages().input_matrix_num1).replace(" ", "")
            matrix3 = input(EncodeMessages().input_matrix_num1).replace(" ", "")
            matrix4 = input(EncodeMessages().input_matrix_num1).replace(" ", "")
            CodeTypes().decode_matrix_code(message, int(matrix1), int(matrix2), int(matrix3), int(matrix4))
        except ValueError:
            print(EncodeMessages().messege_invalid_type)

    def playfair_code_encode(self):
        plaintext = input(EncodeMessages().input_password).upper().replace(" ", "")
        messege_key = input(EncodeMessages().input_plaintext).upper().replace(" ", "")
        try:
            CodeTypes().playfair_encrypt(plaintext=plaintext,message_key=messege_key)
        except ValueError:
            print(EncodeMessages().message_invalid_playfair)


class SolverActions:

    def afinic_solve_actions(self):
        try:
            par1 = input(SolverMessages().x_input).replace(" ", "")
            out1 = input(SolverMessages().out1_input).replace(" ", "")
            par2 = input(SolverMessages().y_input).replace(" ", "")
            out2 = input(SolverMessages().out2_input).replace(" ", "")
            solve_afinic_code(par1=par1, par2=par2, out1=out1, out2=out2)
        except ValueError:
            print(SolverMessages().message_invalid_type)

    def digram_solve_actions(self):
        try:
            par1 = input(SolverMessages().x_input).replace(" ", "")
            out1 = input(SolverMessages().out1_input).replace(" ", "")
            par2 = input(SolverMessages().y_input).replace(" ", "")
            out2 = input(SolverMessages().out2_input).replace(" ", "")
            solve_digram(par1=par1, par2=par2, out1=out1, out2=out2)
        except ValueError:
            print(SolverMessages().message_invalid_type)

    def matrix_solce_actions(self):
        try:
            par1 = input(SolverMessages().x_input).replace(" ", "")
            out1 = input(SolverMessages().out1_input).replace(" ", "")
            par2 = input(SolverMessages().y_input).replace(" ", "")
            out2 = input(SolverMessages().out2_input).replace(" ", "")
            solve_matrix(par1=par1, par2=par2, out1=out1, out2=out2)
        except ValueError:
            print(SolverMessages().message_invalid_type)
