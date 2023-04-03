from dics import *

def solve_afinic_code(par1:str, par2:str, out1:str, out2:str):
    x = set.get(par1)
    y = set.get(par2)
    out1 = set.get(out1)
    out2 = set.get(out2)
    for a in range(26):
        for b in range(26):
            res1 = (a*x+b)%26
            res2 = (a*y+b)%26
            if res1 == out1 and res2 == out2:
                print({'a': a, 'b': b})


def solve_digram(par1:str,par2:str, out1:str,out2:str):
    par_1_num = [set.get(i) for i in par1]
    par_2_num = [set.get(i) for i in par2]
    x = par_1_num[0]*26+par_1_num[1]
    y = par_2_num[0]*26+par_2_num[1]
    out1_num =  [set.get(i) for i in out1]
    out2_num = [set.get(i) for i in out2]
    out1 = out1_num[0]*26+out1_num[1]
    out2 = out2_num[0]*26+out2_num[1]
    for a in range(676):
        for b in range(676):
            res1 = (a*x+b)%676
            res2 = (a*y+b)%676
            if res1 == out1 and res2 == out2:
                print({'a': a, 'b': b})
