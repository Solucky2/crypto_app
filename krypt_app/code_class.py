from dics import set, set2
from MessageClass import EncodeMessages, SolverMessages
from solver import solve_digram, solve_afinic_code


class CodeTypes:


    def encode_fence_code(self, message:str, height:int): #działa
        sheet = [["" for i in range(len(message))] for j in range(height)]
        direction = -1
        row = 0
        col = 0
        for i in message:
            sheet[row][col] = i
            if row == 0 or row == height - 1:
                direction = -direction
            row += direction
            col += 1
        [print(i) for i in sheet]
        out = ''
        for i in range(height):
            for j in range(len(message)):
                out += sheet[i][j]
        print(out)



    def decode_cesar_code(self, message:str, b:int): #dziala
        out = []
        for i in message:
            ind = set.get(i)
            val = (ind - b) % 26
            out.append(val)
        mess = [set2[i] for i in out]
        encoded = ''
        for _ in mess:
            encoded += _
        print(encoded)


    def encode_cezar_code(self, message:str,b:int): #dziala
        out = []
        for i in message:
            ind = set.get(i)
            val = (ind + b) % 26
            out.append(val)
        mess = [set2[i] for i in out]
        encoded = ''
        for _ in mess:
            encoded += _
        print(encoded)


    def encode_modulo(self, message:str, b:int): #działa
        outp = []
        for i in message:
            a = set.get(i)
            val = (a + b)%26
            outp.append(val)

        mess = [set2[i] for i in outp]
        encoded = ''
        for _ in mess:
            encoded += _
        print(encoded)

    def decode_modulo(self, message:str, b:int): #działa
        outp = []
        for i in message:
            a = set.get(i)
            val = (a - b)%26
            outp.append(val)

        mess = [set2[i] for i in outp]
        encoded = ''
        for _ in mess:
            encoded += _
        print(encoded)


    def encode_decode_module_keys(self, message:str, key1:int, key2:int): #dziala
        out = []
        for i in message:
            a = set.get(i)
            val = (a*key1+key2)%26
            out.append(val)
        mess = [set2[i] for i in out]
        encoded = ''
        for _ in mess:
            encoded += _
        print(encoded)


    def encode_decode_modulo_digram(self, message:str,a:int, b:int): #działa
        if len(message) % 2 != 0:
            message += "Q"
        out3 = []
        sen2 = [message[i:i + 2] for i in range(0, len(message), 2)]
        out = (26 * set.get(i[0]) + set.get(i[1]) for i in sen2)
        out2 = ((a * i + b) % 676 for i in out)
        for i in out2:
            val3 = i // 26
            val4 = i % 26
            out3.append(val3)
            out3.append(val4)
        mess = [set2[i] for i in out3]
        encoded = ''
        for _ in mess:
            encoded += _
        print(encoded)


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


class SolverActions:

    def afinic_solve_actions(self):
        try:
            x = input(SolverMessages().x_input).replace(" ", "")
            y = input(SolverMessages().y_input).replace(" ", "")
            out1 = input(SolverMessages().out1_input).replace(" ", "")
            out2 = input(SolverMessages().out2_input).replace(" ", "")
            solve_afinic_code(int(x), int(y), int(out1), int(out2))
        except ValueError:
            print(SolverMessages().message_invalid_type)

    def digram_solve_actions(self):
        try:
            x = input(SolverMessages().x_input).replace(" ", "")
            y = input(SolverMessages().y_input).replace(" ", "")
            out1 = input(SolverMessages().out1_input).replace(" ", "")
            out2 = input(SolverMessages().out2_input).replace(" ", "")
            solve_digram(int(out1),int(x),int(out2),int(y))
        except ValueError:
            print(SolverMessages().message_invalid_type)
