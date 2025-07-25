import random 
print('\033 [1;33m -=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= \033[m')
print('\033 [1;31m Vou pensar em um número entre 0 e 5.Tente adivinhar: \033[m')
print('\033 [1;35m -=-=-=-=-==-=-=-=-=-==-=-=-=-==-=-=-=-=-==-=-=-=-=  \033[m')
n = int (input ('Em qual número eu pensei ?'))
print(' \033[1;35m Processando.. \033[m')
x = [0,1,2,3,4,5]
embaralhar = random.choice(x)
if n == embaralhar:
    print(' \033[1;33m Parabéns!Você conseguiu me vencer \033[m ')
else:
    print(' \033[1;31m  Ganhei!Eu pensei no número {} e não no {}  \033[m'.format(embaralhar, n))