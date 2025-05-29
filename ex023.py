num = int(input('Digite um número:'))
print('Analisando o número..', num)
Unidade = num//1%10
Dezena = num//10%10
Centena = num//100%10
Milhar = num//1000%10
print('Unidade:{}'.format(Unidade))
print('Dezena:{}'.format(Dezena))
print('Centena:{}'.format(Centena))
print('Milhar:{}'.format(Milhar))

