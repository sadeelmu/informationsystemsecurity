# The Euclidean algorithm is a way to find the greatest common divisor of two positive integers.
# GCD of two numbers is the largest number that divides both of them

# There are two Euclidean algorithm:
# 1. Basic

#If we subtract a smaller number from a larger one (we reduce a larger number), GCD doesn’t change.
# So if we keep subtracting repeatedly the larger of two, we end up with GCD.
# Now instead of subtraction, if we divide the smaller number,
# the algorithm stops when we find the remainder 0.

# 2. Extended
# Extended Euclidean algorithm also finds integer coefficients x and y such that: ax + by = gcd(a, b)

#The extended Euclidean algorithm updates the results of gcd(a, b)
# using the results calculated by the recursive call gcd(b%a, a).
# Let values of x and y calculated by the recursive call be x1 and y1.
# x and y are updated using the below expressions.

def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)

def extendedEuclidean(a,b):
    if a  == 0:
        return b, 0, 1

    gcd, x1, y1 = extendedEuclidean(b%a, a)

    x = y1 - (b//a) * x1
    y = x1

    return gcd, x, y



if __name__ == "__main__":
    a = 10
    b = 15
    print("gcd(", a, ",", b, ") = ", gcd(a, b))

    a = 35
    b = 10
    print("gcd(", a, ",", b, ") = ", gcd(a, b))

    a = 31
    b = 2
    print("gcd(", a, ",", b, ") = ", gcd(a, b))

    a, b = 35, 15
    g, x, y = extendedEuclidean(a,b)
    print("Extended Euclidean gcd(", a, ",", b, ") = ", g)

#The extended Euclidean algorithm is particularly useful when a and b are coprime (or gcd is 1).
# Since x is the modular multiplicative inverse of “a modulo b”,
# and y is the modular multiplicative inverse of “b modulo a”

