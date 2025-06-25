from random import randint

# Gera um número aleatório
numpc = randint(0,10)

print('O computador escolheu um número de 0 a 10. Será que você consegue adivinhar qual é? ')

while True:
    try:
        num = int(input('Digite o seu palpite: '))
        
        if num < 0 or num > 10:
            print('Número inválido! Insira um número de 0 a 10.')
            continue

    # Compara os dois números e informa se acertou ou se o número é maior ou menor que o do computador
        print('-' * 85)
        if num > numpc:
            print('\033[31mO seu número é MAIOR que o número do computador.\033[m Tente outra vez. ')
        elif num < numpc:
            print('\033[31mO seu número é MENOR que o número do computador.\033[m Tente outra vez. ')
        else:
            print(f'\033[32mParabéns! O computador escolheu o número {numpc}! Você acertou!\033[m')
            break
        
    except ValueError:
        print('\033[33mEntrada inválida! Por favor, digite um número inteiro.\033[m')