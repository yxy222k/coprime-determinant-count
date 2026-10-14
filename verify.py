"""Brute-force check: #{(a,b,c,d) in [0,n)^4 : gcd(ac - bd, n) = 1}
against the closed form n^4 * prod_{p|n} (1 - 1/p)(1 - 1/p^2)."""

from fractions import Fraction
from math import gcd


def brute(n):
    # Tally products mod n once, then pair up (a,c) and (b,d) by product value.
    prod_count = [0] * n
    for a in range(n):
        for c in range(n):
            prod_count[a * c % n] += 1
    return sum(prod_count[x] * prod_count[y]
               for x in range(n) for y in range(n)
               if gcd(x - y, n) == 1)


def prime_factors(n):
    ps, p = [], 2
    while p * p <= n:
        if n % p == 0:
            ps.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        ps.append(n)
    return ps


def formula(n):
    result = Fraction(n ** 4)
    for p in prime_factors(n):
        result *= (1 - Fraction(1, p)) * (1 - Fraction(1, p * p))
    return int(result)


if __name__ == "__main__":
    ok = True
    for n in range(1, 31):
        b, f = brute(n), formula(n)
        ok &= b == f
        print(f"n={n:2d}  brute={b:8d}  formula={f:8d}  {'OK' if b == f else 'MISMATCH'}")
    print("all match" if ok else "MISMATCH FOUND")
