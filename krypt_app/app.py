from code_class import CodeActions
from MessageClass import Messages


def app():
    print(Messages().code_types_info)
    ask = input(Messages().enter_code_type).replace(" ","")
    match ask:
        case "1":
            rodzaj = input(Messages().choose_action).lower().replace(" ","")
            if rodzaj == Messages().encode:
                CodeActions().cesar_code_actions_encode()
            elif rodzaj == Messages().decode:
                CodeActions().cesar_code_actions_decode()
            else:
                print(Messages().error_wrong_action)

        case "2":
            CodeActions().fence_code_actions_encode()
        case "3":
            rodzaj = input(Messages().choose_action).lower().replace(" ","")
            if rodzaj == Messages().encode:
                CodeActions().modulo_code_actions_encode()
            elif rodzaj == Messages().decode:
               CodeActions().modulo_code_actions_decode()
            else:
                print(Messages().error_wrong_action)
        case "4":
            CodeActions().afinic_code_encode_decode()
        case _ :
            reapet = input(Messages().error_type_code).lower().replace(" ","")
            if reapet == Messages().yes:
                app()
            else:
                print(Messages().message_for_haters)
                return 0
    try_again = input(Messages().restart_question).lower().replace(" ","")
    if try_again == Messages.yes:
        app()
    else:
        print(Messages().message_for_kumpels)


app()