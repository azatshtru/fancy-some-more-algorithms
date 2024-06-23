# Diophantine equations

Diophantine equations are of the form ax+by=c.
They can be solved if c is divisible by gcd(a, b).

Using euclid's algorithm, the solutions to Diophantine equations can be easily derived.
A solution for diophantine equation exists if and only if c is divisible by gcd(a, b).
Then we can write ax+by = gcd(a, b) and solve for x and y by going through Euclid's algorithm for gcd in reverse.
After than we can multiply the equation by constants to derive the values in the original equation.

If one set of solution in known, the others can be derived using the relations:
$$x_k=x+\frac{kb}{gcd(a,b)}$$
$$x_k=y-\frac{ka}{gcd(a,b)}$$