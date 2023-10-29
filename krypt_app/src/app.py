from encrypt_src.encode_decode_actions import *
from solver_code.solver_actions import *

def encode_app():
    print(EncodeMessages().code_types_info)
    ask = input(EncodeMessages().enter_code_type).replace(" ","")
    match ask:
        case "1":
            rodzaj = input(EncodeMessages().choose_action).lower().replace(" ","")
            if rodzaj == EncodeMessages().encode:
                cesar_code_actions_encode()
            elif rodzaj == EncodeMessages().decode:
                cesar_code_actions_decode()
            else:
                print(EncodeMessages().error_wrong_action)

        case "2":
            fence_code_actions_encode()
        case "3":
            rodzaj = input(EncodeMessages().choose_action).lower().replace(" ","")
            if rodzaj == EncodeMessages().encode:
                modulo_code_actions_encode()
            elif rodzaj == EncodeMessages().decode:
                modulo_code_actions_decode()
            else:

                print(EncodeMessages().error_wrong_action)
        case "4":
            afinic_code_encode_decode()
        case "5":
            digram_code_encode_decode()
        case "6":
            rodzaj = input(EncodeMessages().choose_action).lower().replace(" ","")
            if rodzaj == EncodeMessages().encode:
                matrix_code_encode()
            elif rodzaj == EncodeMessages().decode:
                matrix_code_decode()
        case "7":
            playfair_code_encode()
        case _ :
            reapet = input(EncodeMessages().error_type_code).lower().replace(" ","")
            if reapet == EncodeMessages().yes:
                encode_app()
            else:
                print(EncodeMessages().message_for_haters)
                return 0
    try_again = input(EncodeMessages().restart_question).lower().replace(" ","")
    if try_again == EncodeMessages.yes:
        encode_app()
    else:
        print(EncodeMessages().message_for_kumpels)

def solver_app():
    print(SolverMessages().solver_types)
    choose_solver = input(SolverMessages().choose_solver)
    match choose_solver:
        case "1":
            afinic_solve_actions()
        case "2":
            digram_solve_actions()
        case '3':
            matrix_solve_actions()
        case _:
            print(EncodeMessages().error_wrong_action)
