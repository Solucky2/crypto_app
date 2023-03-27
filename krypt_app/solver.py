
def solve(x, y, out1, out2):
    for a in range(26):
        for b in range(26):
            res1 = (a*x+b)%26
            res2 = (a*y+b)%26
            if res1 == out1 and res2 == out2:
                print({'a': a, 'b': b})