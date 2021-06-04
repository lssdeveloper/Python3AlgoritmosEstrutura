# uma função que chama a si própria
"""
def fat(n):
    if(n == 0):
        return 1
    return n * fat(n -1)

print(fat(3))    # = 6


# fibonacci = 1, 1, 2, 3, 5, 8, 13, ...

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(7))

base, exp
base = 2
exp = 10
2**10 = 1024
"""


def pot(base, exp):
    if (exp == 0):
        return 1
    return base * pot(base, exp - 1)


print(pot(2, 10))
