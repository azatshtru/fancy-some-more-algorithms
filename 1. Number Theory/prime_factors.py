# checks if a number is prime.
def prime(n: int) -> bool:
    if n < 2:
        return False
    x = 2
    while x*x <= n:
        if n%x: return False
        x += 1
    return True

# returns the list of factors of a number n
def factor(n: int) -> list:
    factors = []
    x = 2
    while x*x <= n:
        while n%x == 0:
            factors.append(x)
            n//=x 
        x += 1
    if n > 1:
        factors.append(n)
    return factors