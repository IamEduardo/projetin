import math

# Faça um exercício que envolva: a soma dos números 14 + 15 = ?, a multiplicação dos numeros: 30 * 12 = ? e a divisão dos números 40 / 2 = ? Usando o .format para "formatar" e indentar os números corretamente.'''

soma1 = int(input('Qual é o valor da primeira soma? '))
soma2 = int(input('Qual é o valor da segunda soma?  '))
soma_numeros = soma1 + soma2


print('O primeiro valor {} mais a soma do segundo valor {} é: {}'.format(soma1, soma2, soma_numeros))


# Agora faça esse mesmo exercício que envolva a multiplicação dos números ao alcance e veja o resultado, utilize o .format(value1, value2, mult3)

multi = float(input('Qual é o valor que você deseja multiplicar?  '))
multi2 = float(input("Qual é o segundo valor que você deseja multiplicar?  "))
multi3 = float(input("Qual é o terceiro valor que você deseja multiplicar?  "))

mult_valores = multi * multi2 * multi3
print('Parabéns! Você selecionou como primeiro valor: {}, você também selecionou o segundo valor: {} \nVocê também selecionou o terceiro valor {}. Agora façamos a multiplicação: {}'.format(multi, multi2, multi3, mult_valores))


# Faça o mesmo com a divisão e o menos, usando o .format

valor_div1 = float(input('Qual é o valor que você deseja dividir? '))
valor_div2 = float(input('Qual é o segundo valor que você deseja dividir? '))
div_sum = valor_div1 / valor_div2

print('A divisão do 1º número {} e do 2º número {} é de: {}'.format(valor_div1, valor_div2, div_sum))

# Subtraia
choose_number1 = float(input('Qual é o número desejado para subtrair: '))
choose_number2 = float(input('Qual é o segundo número para efetuar a subtração: '))
subminus_result = choose_number1 - choose_number2 

print('O resultado da subtração dos valores: {} e {} é de: {} '.format(choose_number1, choose_number2, subminus_result))


# Descubra a raiz quadrada  referente qualquer número que você deseja.


raiz_quadrada = int(input('Qual o valor da raíz quadrada de: '))
print(math.isqrt(raiz_quadrada), math.sqrt(raiz_quadrada))