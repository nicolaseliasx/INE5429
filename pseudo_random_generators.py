import time
import json

# Gerador Congruencial Linear (LCG)
class LinearCongruentialGenerator:
    def __init__(self, a, c, m, seed):
        self.a = a
        self.c = c
        self.m = m
        self.seed = seed

    def next(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed

def generate_large_lcg(bits, seed):
    a = 1664525
    c = 1013904223
    m = 2**bits
    lcg = LinearCongruentialGenerator(a, c, m, seed)
    return lcg.next()

# XORShift
class XORShift:
    def __init__(self, seed):
        self.seed = seed

    def next(self):
        self.seed ^= (self.seed << 13) & 0xFFFFFFFFFFFFFFFF
        self.seed ^= (self.seed >> 7)
        self.seed ^= (self.seed << 17) & 0xFFFFFFFFFFFFFFFF
        return self.seed

def generate_large_xorshift(bits, seed):
    xorshift = XORShift(seed)
    return xorshift.next() & ((1 << bits) - 1)

# Script principal para gerar números
bit_sizes = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

# Gerar e testar números pseudo-aleatórios
lcg_numbers = []
xorshift_numbers = []

for bits in bit_sizes:
    seed = int(time.time() * 1000000) % (2**bits - 1)  # Usar o tempo atual em microssegundos como semente para variar
    lcg_number = generate_large_lcg(bits, seed)
    lcg_numbers.append(lcg_number)
    
    # Introduzir um pequeno atraso para garantir sementes diferentes
    time.sleep(0.001)
    seed = int(time.time() * 1000000) % (2**bits - 1)  # Usar o tempo atual em microssegundos como semente para variar
    xorshift_number = generate_large_xorshift(bits, seed)
    xorshift_numbers.append(xorshift_number)

# Salvar números em um arquivo
with open("random_numbers.json", "w") as f:
    json.dump({"lcg_numbers": lcg_numbers, "xorshift_numbers": xorshift_numbers}, f)

print("Números pseudo-aleatórios salvos em random_numbers.json")
