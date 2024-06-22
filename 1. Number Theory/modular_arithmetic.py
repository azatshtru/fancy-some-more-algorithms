# calculate modulo of some power n of x w.r.t. some m
def modpow(x, n, m):
    if n == 0:
        return 1%m
    u = modpow(x, n//2, m)
    u = (u*u)%m
    if n%2 == 1:
        u = (u*x)%m
    return u