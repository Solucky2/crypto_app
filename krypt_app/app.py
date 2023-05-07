from code_class import CodeActions, SolverActions
from MessageClass import EncodeMessages, SolverMessages, AppMessages


def encode_app():
    print(EncodeMessages().code_types_info)
    ask = input(EncodeMessages().enter_code_type).replace(" ","")
    match ask:
        case "1":
            rodzaj = input(EncodeMessages().choose_action).lower().replace(" ","")
            if rodzaj == EncodeMessages().encode:
                CodeActions().cesar_code_actions_encode()
            elif rodzaj == EncodeMessages().decode:
                CodeActions().cesar_code_actions_decode()
            else:
                print(EncodeMessages().error_wrong_action)

        case "2":
            CodeActions().fence_code_actions_encode()
        case "3":
            rodzaj = input(EncodeMessages().choose_action).lower().replace(" ","")
            if rodzaj == EncodeMessages().encode:
                CodeActions().modulo_code_actions_encode()
            elif rodzaj == EncodeMessages().decode:
                CodeActions().modulo_code_actions_decode()
            else:

                print(EncodeMessages().error_wrong_action)
        case "4":
            CodeActions().afinic_code_encode_decode()
        case "5":
            CodeActions().digram_code_encode_decode()
        case "6":
            rodzaj = input(EncodeMessages().choose_action).lower().replace(" ","")
            if rodzaj == EncodeMessages().encode:
                CodeActions().matrix_code_encode()
            elif rodzaj == EncodeMessages().decode:
                CodeActions().matrix_code_decode()
        case "7":
            CodeActions().playfair_code_encode()
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
            SolverActions().afinic_solve_actions()

        case "2":
            SolverActions().digram_solve_actions()
        case '3':
            pass
        case _:
            print(EncodeMessages().error_wrong_action)



if __name__ == '__main__':
    print(AppMessages().choose_app)
    choose_app = input(AppMessages().choose_action)
    if choose_app == "1":
        solver_app()
    elif choose_app == "2":
        encode_app()
    else:
        print(AppMessages().app_error)