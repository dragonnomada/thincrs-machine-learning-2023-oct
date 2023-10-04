print("Hola Python 🐍")

# Evaluate first 20 prime numbers

primos = []

n = 2

while len(primos) < 20:
    esPrimo = True
    for primo in primos:
        if n % primo == 0:
            esPrimo = False
    if esPrimo:
        primos.append(n)
    n += 1

print(primos)
