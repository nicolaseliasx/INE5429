import random

# Função para exponenciação modular
def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

# Teste de Primalidade de Miller-Rabin
def miller_rabin(n, k):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    s, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    def check_composite(a, d, n, s):
        x = mod_exp(a, d, n)
        if x == 1 or x == n - 1:
            return False
        for _ in range(s - 1):
            x = mod_exp(x, 2, n)
            if x == n - 1:
                return False
        return True

    for _ in range(k):
        a = random.randint(2, n - 2)
        if check_composite(a, d, n, s):
            return False
    return True

# Teste de Primalidade de Fermat
def fermat_primality_test(n, k):
    if n <= 1:
        return False
    if n <= 3:
        return True
    for _ in range(k):
        a = random.randint(2, n - 2)
        if mod_exp(a, n - 1, n) != 1:
            return False
    return True
