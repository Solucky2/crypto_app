
def solve_afinic_code(x:int, y:int, out1:int, out2:int):
    for a in range(26):
        for b in range(26):
            res1 = (a*x+b)%26
            res2 = (a*y+b)%26
            if res1 == out1 and res2 == out2:
                print({'a': a, 'b': b})


def solve_digram(out1:int, x:int,out2:int, y:int):
    for a in range(676):
        for b in range(676):
            res1 = (a*x+b)%676
            res2 = (a*y+b)%676
            if res1 == out1 and res2 == out2:
                print({'a': a, 'b': b})
