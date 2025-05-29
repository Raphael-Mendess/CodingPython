L = float(input('Largura da parede:'))
A = float(input('Altura da parede:'))
Area = L * A
T = Area / 2 
print('Sua parede tem a dimensão de {}X{} e sua área é de {}m2'.format(L, A, Area))
print('Para pintar essa parede você precisará de {}t de tinta'.format(T))          