#Desenvolva um programa que leia o nome,idade e sexo de 4 pessoas. No final do programa, mostre:
#A média de idade do grupo
#Qual é o nome do homem mais velho
#Quantas mulheres têm menos de 20 anos  
somaidade = 0
mediaidade = 0
maior_idadehomem = 0
nomevelho = ""
totalmulher20 = 0

for r in range (1, 5):  
    print("------- {} PESSOA -------".format(r))

    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()    
    somaidade += idade

    if r == 1 and sexo in "Mm":
        maior_idade = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maior_idadehomem:  
       maior_idadehomem = idade
       nomevelho = nome 
    if sexo in "Ff" and idade < 20:
        totalmulher20 += 1       

mediaidade = somaidade / 4

print("A média de idade do grupo é de {}anos".format(mediaidade)) 
print("O homem mais velho tem {}anos e se chama {}".format(maior_idadehomem, nomevelho))   
print("Ao todo são {}mulheres com menos de 20 anos".format(totalmulher20))
