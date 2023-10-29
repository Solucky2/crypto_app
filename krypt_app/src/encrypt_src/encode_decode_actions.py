from krypt_app.src.messages.MessageClass import *
from encrypt_actions import *

def cesar_code_actions_encode():
    try:
        message = input(EncodeMessages().input_password).upper().replace(" ", "")
        b = input(EncodeMessages().input_transition_b).replace(" ", "")
        encode_cezar_code(message, int(b))
    except ValueError:
        print(EncodeMessages().messege_invalid_type)

def cesar_code_actions_decode():
    try:
        message = input(EncodeMessages().input_password).upper().replace(" ", "")
        b = input(EncodeMessages().input_transition_b).replace(" ", "")
        decode_cesar_code(message, int(b))
    except ValueError:
        print(EncodeMessages().messege_invalid_type)

def fence_code_actions_encode():
    try:
        message = input(EncodeMessages().input_password).upper().replace(" ", "")
        height = input(EncodeMessages().input_fence_height).replace(" ", "")
        encode_fence_code(message, int(height))
    except ValueError:
        print(EncodeMessages().messege_invalid_type)

def modulo_code_actions_encode():
    try:
        message = input(EncodeMessages().input_password).upper().replace(" ", "")
        b = input(EncodeMessages().input_transition_b).replace(" ", "")
        encode_modulo(message, int(b))
    except ValueError:
        print(EncodeMessages().messege_invalid_type)

def modulo_code_actions_decode():
    try:
        message = input(EncodeMessages().input_password).upper().replace(" ", "")
        b = input(EncodeMessages().input_transition_b).replace(" ", "")
        decode_modulo(message, int(b))
    except ValueError:
        print(EncodeMessages().messege_invalid_type)

def afinic_code_encode_decode():
    message = input(EncodeMessages().input_password).upper().replace(" ", "")
    try:
        a = input(EncodeMessages().input_transition_a).replace(" ", "")
        b = input(EncodeMessages.input_transition_b).replace(" ", "")
        encode_decode_module_keys(message, int(a), int(b))
    except ValueError:
        print(EncodeMessages().messege_invalid_type)

def digram_code_encode_decode():
    message = input(EncodeMessages().input_password).upper().replace(" ", "")
    try:
        a = input(EncodeMessages().input_transition_a).replace(" ", "")
        b = input(EncodeMessages.input_transition_b).replace(" ", "")
        encode_decode_modulo_digram(message, int(a), int(b))
    except ValueError:
        print(EncodeMessages().messege_invalid_type)

def matrix_code_encode():
    message = input(EncodeMessages().input_password).upper().replace(" ", "")
    try:
        matrix1 = input(EncodeMessages().input_matrix_num1).replace(" ", "")
        matrix2 = input(EncodeMessages().input_matrix_num1).replace(" ", "")
        matrix3 = input(EncodeMessages().input_matrix_num1).replace(" ", "")
        matrix4 = input(EncodeMessages().input_matrix_num1).replace(" ", "")
        encode_matrix_code(message, int(matrix1), int(matrix2), int(matrix3), int(matrix4))
    except ValueError:
        print(EncodeMessages().messege_invalid_type)

def matrix_code_decode():
    message = input(EncodeMessages().input_password).upper().replace(" ", "")
    try:
        matrix1 = input(EncodeMessages().input_matrix_num1).replace(" ", "")
        matrix2 = input(EncodeMessages().input_matrix_num1).replace(" ", "")
        matrix3 = input(EncodeMessages().input_matrix_num1).replace(" ", "")
        matrix4 = input(EncodeMessages().input_matrix_num1).replace(" ", "")
        decode_matrix_code(message, int(matrix1), int(matrix2), int(matrix3), int(matrix4))
    except ValueError:
        print(EncodeMessages().messege_invalid_type)

def playfair_code_encode():
    plaintext = input(EncodeMessages().input_password).upper().replace(" ", "")
    messege_key = input(EncodeMessages().input_plaintext).upper().replace(" ", "")
    try:
        playfair_encrypt(plaintext=plaintext, message_key=messege_key)
    except ValueError:
        print(EncodeMessages().message_invalid_playfair)