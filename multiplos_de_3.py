#48 - Programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500.


sum = int(0)
for c in range(1, 501):
    if c%3==0:
        sum += c
    
print(f"A soma de todos múltiplos de 3 de 1 a 500 é: {sum}")
