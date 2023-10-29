from src.app import *

if __name__ == '__main__':
    print(AppMessages().choose_app)
    choose_app = input(AppMessages().choose_action)
    if choose_app == "1":
        solver_app()
    elif choose_app == "2":
        encode_app()
    else:
        print(AppMessages().app_error)