def sieve_of_eratosthenes(n: int) -> list:
    sieve = [None] * (n+1)
    x = 2
    while x <= n:
        if(sieve[x]):
            continue
        u = 2*x
        while u <= n:
            sieve[u] = x
            u += x
    return sieve