"""X
# obter os 100 primeiros números pares
pares = [num for num in range(101) if (num % 2 == 0)]
print(pares)
"""
# MAP
lista = [2, 3, 4]
m = map(lambda x: x**2, lista)
m3 = map(lambda x: x**3, lista)

for i in m:
    print(i)

for i in m3:
    print(i)
