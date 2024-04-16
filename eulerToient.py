#Euler’s Totient function phi (n) for an input n is the count of numbers in {1, 2, 3, …, n-1}
# that are relatively prime to n,
# i.e., the numbers whose GCD (Greatest Common Divisor) with n is 1.

def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a, a)

def complexPhi(n):
    result = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result += 1
    return result

#The formula basically says that the value of phi(n) is equal to n
# multiplied by-product of (1 – 1/p) for all prime factors p of n.
# For example value of phi(6) = 6 * (1-1/2) * (1 – 1/3) = 2.

def phi(n):
    result = n  # Initialize result as n

    # Consider all prime factors
    # of n and for every prime
    # factor p, multiply result with (1 - 1 / p)
    p = 2
    while p * p <= n:

        # Check if p is a prime factor.
        if n % p == 0:

            # If yes, then update n and result
            while n % p == 0:
                n = n // p
            result = result * (1.0 - (1.0 / float(p)))
        p = p + 1

    # If n has a prime factor
    # greater than sqrt(n)
    # (There can be at-most one
    # such prime factor)
    if n > 1:
        result -= result // n
    # Since in the set {1,2,....,n-1}, all numbers are relatively prime with n
    # if n is a prime number

    return int(result)


if __name__ == '__main__':
    for n in range(1, 11):
        print("phi(", n, ") = ",
              phi(n), sep="")
