from sys import exit

print ('- - - CONVERSOR DE MOEDAS - - -')
print ('1 - Real (BRL) ')
print ('2 - Dólar (USD)')
print ('3 - Euro (EUR)')

val = float(input('Digite o valor desejado: '))
opcfonte = int(input('Digite o código da moeda fonte desejada: '))
opcalvo = int(input('Digite o código da moeda desejada para converter: '))
conversor = 0

# Verifica se o usuário não colocou a conversão de duas moedas iguais
if opcfonte == opcalvo:
    print ('Não é possível fazer a conversão de mesmo câmbio')
    exit()

# Verifica se o usuário colocou os códigos de opção válidos
if opcfonte not in [1, 2, 3] or opcalvo not in [1, 2, 3]:
    print('Código de moeda inválido. Encerrando o programa.')
    exit()

print('-' * 55)

# Faz a conversão de acordo com o pedido do usuário 
if opcfonte == 1:
    if opcalvo == 2:
        conversor = val * 0.1802
        print(f'R${val:.2f} equivalem a ${conversor:.2f}')
    if opcalvo == 3:
        conversor = val * 0.1549
        print(f'R${val:.2f} equivalem a €{conversor:.2f}')
elif opcfonte == 2:
    if opcalvo == 1:
        conversor = val * 5.543
        print(f'${val:.2f} equivalem a R${conversor:.2f}')
    elif opcalvo == 3:
        conversor = val * 0.8589
        print(f'${val:.2f} equivalem a €{conversor:.2f}')
elif opcfonte == 3:
    if opcalvo == 1:
        conversor = val * 6.455
        print(f'€{val:.2f} equivalem a R${conversor:.2f}')
    elif opcalvo == 2:
        conversor = val * 1.164
        print(f'€{val:.2f} equivalem a ${conversor:.2f}')

print('-' * 55)
