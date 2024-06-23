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

---

# Chinese Remainder Theorem

A set of equations of the form:
$$x=a_1\mod m_1$$
$$x=a_2\mod m_2$$
$$\dots$$
$$x=a_n\mod m_n$$
where $m_1,m_2\dots m_n$ are coprime can be solved using the Chinese Remainder theorem.

Let $X_k=\frac{m_1m_2\dots m_n}{m_k}$
And its inverse with respect to some $m_k$ is $X^{-1}_k_m_k$

Using the notation above,
$$x = a_1X_1X^{-1}_1_m_1 + a_2X_2X^{-1}_2_m_2 + \dots + a_nX_nX^{-1}_n_m_n  \space  (1)$$

**PROOF** We know that $X_kX^{-1}_k_m_k\mod m_k = 1$,
$a_kX_kX^{-1}_k_m_k\mod m_k = a_k$
If we calculate the modulo of x w.r.t. some $m_k$ in statement $(1)$ above, all other terms but the kth one will become zero since they contain $m_k$ and the kth term will become $a_k$.

If we have a solution $x$, all other solutions can be found as $x+m_1+m_2+\dots+m_n$