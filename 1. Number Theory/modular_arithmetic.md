# Modular Arithmetic

## Some identities

$$(x+y) \mod m = ((x \mod m)+(y \mod m)) \mod m$$
$$(x-y) \mod m = ((x \mod m)-(y \mod m)) \mod m$$
$$(xy) \mod m = ((x \mod m)(y \mod m)) \mod m$$
$$x^n \mod m = (x \mod m)^n \mod m$$

## Euler's modulo theorem

$$x^{\phi(m)} \mod m = 1$$

### Fermat's modulo theorem

Fermat's theorem follows from Euler's theorem using the fact that $\phi(n)=n-1$ if n is prime.

If m is prime and m and x are coprime, then:
$$x^{m-1} \mod m = 1$$
Also:
$$x^k \mod m = x^{k \mod (m-1) \mod m}$$

## Modular inverse

The \modular inverse of a number x is a number y such that $xy \mod m = 1$.
A modular inverse only exists if both numbers are coprime.
Using Euler's modulo theorem, an expression for calculating the inverse can be derived.
We know that:
$$xx^{-1}\mod m = 1 \space  (1)$$
and:
$$x^{\phi(m)} \mod m = 1$$
or:
$$xx^{\phi(m)-1} \mod m = 1 \space  (2)$$
Comparing this with the first statement:
$$x^{-1}=x^{\phi(m)-1}$$
If m is prime, then:
$$x^{-1}=x^{m-2}$$