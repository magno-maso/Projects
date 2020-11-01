nome = input("Quantas vezes o loop deve rodar? ")
print(f'Essa aplicação fará um "Loop" {nome} vezes!')
for i in range(int(nome) + 1):
    print(f'Esse é o {i} loop como numero')
for i in nome:
    print(f'Esse é o {i} loop como string')