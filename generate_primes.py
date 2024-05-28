import time
import json
from primality_tests import miller_rabin, fermat_primality_test

# Função para gerar números primos grandes
def generate_large_prime(number, test_func, k=5):
    if number % 2 == 0:
        number += 1
    start_time = time.time()
    if test_func(number, k):
        end_time = time.time()
        return number, end_time - start_time
    return None, 0

# Carregar números aleatórios
with open("random_numbers.json", "r") as f:
    random_numbers = json.load(f)

lcg_numbers = random_numbers["lcg_numbers"]
xorshift_numbers = random_numbers["xorshift_numbers"]

bit_sizes = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

# Resultados de Miller-Rabin
miller_rabin_results = []

# Resultados de Fermat
fermat_results = []

for bits, lcg_number, xorshift_number in zip(bit_sizes, lcg_numbers, xorshift_numbers):
    # Miller-Rabin com número LCG
    prime, time_taken = generate_large_prime(lcg_number, miller_rabin)
    if prime:
        miller_rabin_results.append((bits, prime, time_taken))

    # Fermat com número XORShift
    prime, time_taken = generate_large_prime(xorshift_number, fermat_primality_test)
    if prime:
        fermat_results.append((bits, prime, time_taken))

# Imprimir resultados
print("\nResultados de Miller-Rabin:")
for result in miller_rabin_results:
    print(f"Bits: {result[0]}, Primo: {result[1]}, Tempo: {result[2]:.8f} segundos")

print("\nResultados de Fermat:")
for result in fermat_results:
    print(f"Bits: {result[0]}, Primo: {result[1]}, Tempo: {result[2]:.8f} segundos")

# Salvar resultados em um arquivo
with open("prime_generator_results.txt", "w") as f:
    f.write("\nResultados de Miller-Rabin:\n")
    for result in miller_rabin_results:
        f.write(f"Bits: {result[0]}, Primo: {result[1]}, Tempo: {result[2]:.8f} segundos\n")

    f.write("\nResultados de Fermat:\n")
    for result in fermat_results:
        f.write(f"Bits: {result[0]}, Primo: {result[1]}, Tempo: {result[2]:.8f} segundos\n")

print("Resultados salvos em prime_generator_results.txt")
