def abc():
    i = 9 # i (abc) -> 4002 (int: 9) (RAM)
    k = 20 # k (abc)

    # a function can be defined inside another function in python

    # 4003 (function object) (RAM)
    # xyz (abc) -> 4003
    def xyz():
        j = 10 # j (xyz) -> 4004 (int: 10) RAM
        k = 30 # k (xyz)
        return j
    
    r = xyz()
    return (r * i) + k # 110

print(abc())
# print(xyz()) # xyz is not visible from outside the abc()

# pqr (module) -> 5004 (function object)
def pqr():
    # mno (pqr) -> 5006 (function object)
    def mno(t):
        return t + 10
    
    # returning a function from another function
    return mno

an = pqr() # an(shell) -> 5006 (function object) -> like a second handle to mno()
print(an(5)) # mno(5)


def ytr():
    i = 10 # i (ytr) -> 4005 - (10:int) RAM

    # ret (ytr) -> 5007 (function object)
    def ret(t):
        # inner function can access (get) enclosing function variables
        # Even after the outer function returns, the inner function maintains
        # the context data (variables) of the outer function - Closures
        return t + i

    return ret

aa = ytr() # aa -> 5007
print(aa(4)) # 14


# callback functions
def tyr(fn, j):
    i = 9
    return fn(i, j) ** 2

def ttt(r, p):
    return r + p

# passing a function as an argument to another function
print(tyr(ttt, 4))