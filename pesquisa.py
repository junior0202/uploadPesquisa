print('Para responder esta pesquisa sobre avaliação do produto utilize:\n 1: péssimo \n 2: ruim \n 3: regular \n 4: bom \n 5: ótimo')

f = 0
m = 0
idade = 0
f20b = 0
f30r = 0
mp = 0

while True:
    idade = int(input("\nIdade: "))
    sexo = str(input("Sexo (M ou F): ")).lower()
    if sexo == 'f':
        f += 1
    if sexo == 'm':
        m += 1

    avaliacao = int(input("Digite sua avaliação sobre o produto (1-5): "))
    if sexo == 'f' and idade > 20 and avaliacao == 4:
        f20b += 1
    if sexo == 'f' and idade > 30 and avaliacao == 2:
        f30r += 1
    if sexo == 'm' and avaliacao == 1:
        mp += 1

    escolha = str(input("Você deseja encerrar sua pesquisa (S/N)? ")).lower()
    if escolha == "s":
        break

print ('\nMulheres com mais de 20 anos que responderam bom: ', f20b)
print ('Mulheres com mais de 30 anos que responderam ruim: ', f30r)
print ('Homens que respoderam pessimo: ', mp)
print ('Total de homens que responderam à pesquisa: ', m)
print ('Total de mulheres que responderam à pesquisa: ', f)