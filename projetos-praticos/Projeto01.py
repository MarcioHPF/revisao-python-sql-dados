print('Calculadora\n')
res = 0
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
print('Para calcular os números, digite a operação desejada:')
op = int(input('1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \nDigite a sua opção:'))

if (op == 1):
    res = num1 + num2
    print (f'O resultado é: {res}')
elif (op == 2):
    res = num1 - num2
    print (f'O resultado é: {res}')
elif (op == 3):
    res = num1 * num2
    print (f'O resultado é: {res}')
elif(op == 4):
    if num2 != 0:
        res = num1 / num2
        print (f'O resultado é: {res}')
    else:
        print('Divisão por 0 não é válida!')
else:
    print('Operação inválida!')
