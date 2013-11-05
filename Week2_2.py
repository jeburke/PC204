def gcd(a,b):
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b,r)

a = 45
b = 81
print gcd(a,b)
