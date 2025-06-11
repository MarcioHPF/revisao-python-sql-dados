cod1 = cod2 = 0

#Faz a entrada de dados e verifica se o dado recebido é um valor numérico
while True:
    cpf = input('Digite o seu CPF completo sem dígitos: ').strip()
    if len(cpf) != 11 or not cpf.isdigit():
        print('CPF inválido! Por favor, informe apenas os 11 dígitos do seu CPF.')
    else: 
        break

#Calcula o primeiro código validador do CPF
for c in range (9):
    cod1 += int(cpf[c]) * (10 - c)
cod1 = (cod1 * 10) % 11
#Executa uma regra específica do CPF que diz que quando o resultado é 10, ele conta como 0
if cod1 == 10:
    cod1 = 0

#Calcula o segundo código verificador do CPF
for c in range (10):
    cod2 += int(cpf[c]) * (11 - c)
cod2 = (cod2 * 10) % 11
#Executa uma regra específica do CPF que diz que quando o resultado é 10, ele conta como 0
if cod2 == 10:
    cod2 = 0

#Faz a verificação dos códigos verificadores e informa se o cpf é válido ou inválido
if cod1 == int(cpf[9]) and cod2 == int(cpf[10]):
    print('-' * 28)
    print(f'\033[32mO CPF {cpf} é VÁLIDO\033[m')
    print('-' * 28)
else:
    print('-' * 28)
    print(f'\033[31mO CPF {cpf} é INVÁLIDO\033[m')
    print('-' * 28)
    