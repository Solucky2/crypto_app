from dics import set, set2
from MessageClass import Messages

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



    def decode_cesar_code(self, message:str, b): #dziala
        out = []
        for i in message:
            ind = set.get(i)
            val = (ind - b) % 26
            out.append(val)
        mess = [set2[i] for i in out]
        print(mess)


    def encode_cezar_code(self, message:str,b): #dziala
        out = []
        for i in message:
            ind = set.get(i)
            val = (ind + b) % 26
            out.append(val)
        mess = [set2[i] for i in out]
        print(mess)


    def encode_modulo(self, message:str, b): #działa
        outp = []
        for i in message:
            a = set.get(i)
            val = (a + b)%26
            outp.append(val)

        mess = [set2[i] for i in outp]
        print(mess)

    def decode_modulo(self, message:str, b:int): #działa
        outp = []
        for i in message:
            a = set.get(i)
            val = (a - b)%26
            outp.append(val)

        mess = [set2[i] for i in outp]
        print(mess)


    def encode_decode_module_keys(self, message:str, key1:int, key2:int): #dziala
        out = []
        for i in message:
            a = set.get(i)
            val = (a*key1+key2)%26
            out.append(val)
        mess = [set2[i] for i in out]
        print(mess)


    def decoed_modulo_n2(self, message:str): #todo dokończyć
        out = []
        length = len(message)
        print(length)
        if length // 2 != 0:
            pass
            # sentence.('Q')
            print(message)
            for i in message:
                pass

    def encode_module_n2(self, message:str,a:int, b:int): #działa
        out3 = []
        sen2 = [message[i:i+2] for i in range(0, len(message), 2)]
        out = (26*set.get(i[0])+set.get(i[1]) for i in sen2)
        out2 = ((a*i+b)%676 for i in out)
        for i in out2:
            val3 = i//26
            val4 = i%26
            out3.append(val3)
            out3.append(val4)

        mess = [set2[i] for i in out3]
        print(mess)


class CodeActions:

    def cesar_code_actions_encode(self):
        message = input(Messages().input_password).upper().replace(" ", "")
        b = input(Messages().input_transition_b)
        CodeTypes().encode_cezar_code(message, int(b))

    def cesar_code_actions_decode(self):
        message = input(Messages().input_password).upper().replace(" ", "")
        b = input(Messages().input_transition_b).replace(" ", "")
        CodeTypes.decode_cesar_code(message, int(b))

    def fence_code_actions_encode(self):
        message = input(Messages().input_password).upper().replace(" ", "")
        height = input(Messages().input_fence_height)
        CodeTypes().encode_fence_code(message, int(height))

    def modulo_code_actions_encode(self):
        message = input(Messages().input_password).upper().replace(" ", "")
        b = input(Messages().input_transition_b).replace(" ", "")
        CodeTypes().encode_modulo(message, int(b))

    def modulo_code_actions_decode(self):
        message = input(Messages().input_password).upper().replace(" ", "")
        b = input(Messages().input_transition_b).replace(" ", "")
        CodeTypes().decode_modulo(message, int(b))

    def afinic_code_encode_decode(self):
        message = input(Messages().input_password).upper().replace(" ", "")
        a = input(Messages().input_transition_a).replace(" ", "")
        b = input(Messages.input_transition_b).replace(" ", "")
        CodeTypes().encode_decode_module_keys(message, int(a), int(b))