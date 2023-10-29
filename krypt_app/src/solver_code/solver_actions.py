from MessageClass import *
from encrypt_actions import *

def afinic_solve_actions():
    try:
        par1 = input(SolverMessages().x_input).replace(" ", "")
        out1 = input(SolverMessages().out1_input).replace(" ", "")
        par2 = input(SolverMessages().y_input).replace(" ", "")
        out2 = input(SolverMessages().out2_input).replace(" ", "")
        solve_afinic_code(par1=par1, par2=par2, out1=out1, out2=out2)
    except ValueError:
        print(SolverMessages().message_invalid_type)

def digram_solve_actions():
    try:
        par1 = input(SolverMessages().x_input).replace(" ", "")
        out1 = input(SolverMessages().out1_input).replace(" ", "")
        par2 = input(SolverMessages().y_input).replace(" ", "")
        out2 = input(SolverMessages().out2_input).replace(" ", "")
        solve_digram(par1=par1, par2=par2, out1=out1, out2=out2)
    except ValueError:
        print(SolverMessages().message_invalid_type)

def matrix_solve_actions():
    try:
        par1 = input(SolverMessages().x_input).replace(" ", "")
        out1 = input(SolverMessages().out1_input).replace(" ", "")
        par2 = input(SolverMessages().y_input).replace(" ", "")
        out2 = input(SolverMessages().out2_input).replace(" ", "")
        solve_matrix(par1=par1, par2=par2, out1=out1, out2=out2)
    except ValueError:
        print(SolverMessages().message_invalid_type)