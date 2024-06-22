# Primes and Factors

A number is called a factor of another number if it divides the other number completely.
A number is called prime if the only factors it has are 1 and itself.

---

## Factorization of a number

Every number has a prime factorization where it can be written as the product of prime numbers.
$$n=p_1^{a_1}p_2^{a_2}\dots p_n^{a_n}$$
Each factor of the number can be written as the product of some subset of its prime factors.

### Number of factors

Number of factors of a number is $\tau(n)$, where
$$\tau(n)=\prod(a_i+1)$$
This is because there are $a_i+1$ ways to choose how many times each prime factor appears for constructing a factor.

### Sum of factors

The sum of factors is $\sigma(n)$, where
$$\sigma(n)=\prod(1+p_i+p_i^2+\dots+p_i^{a_i})=\prod\frac{p_i^{a_i+1}-1}{p_i-1}$$

### Product of factors

The product of factors is $\mu(n)$, where
$$\mu(n)=n^{\tau(n)/2}$$
This is because there are n/2 pairs of factors whose product is 84

### Perfect number

A number $n$ is called a perfect number if $n=\sigma(n)-n$, for example: 28.

---

## Number of Primes

There are infinite number of prime numbers.
**PROOF**: Consider all the prime numbers in a set, if all of them are multiplied and 1 is added to the product, we get a unique prime.

## Density of Primes

Let $\pi(n)$ denote the number of primes between 1 to n, then
$$\pi(n)\approx\frac{n}{ln(n)}$$

## Conjectures related to number of primes

### Goldbach's conjecture
Each even integer greater than 2 can be represented as a sum of two primes.

### Twin prime conjecture
There are infinite number of pairs of the form (p, p+2) where p and p+2 are both primes.

### Legendre's conjecture
There is always a prime number between $n^2$ and $(n+1)^2$

---

## Euler's totient function

Two numbers a and b are coprime if gcd(a, b) = 1. Euler's totient function $\phi(n)$ gives the number of coprimes of n between 1 and n.
$$\phi(n)=\prod p_i^{a_i-1}(p_i-1)$$

If some number n is prime, then it is coprime with every number before it, hence:
$$\phi(n)=n-1$$