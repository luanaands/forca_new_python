def find_boneco(chute):
    tela = { 6 : "", 
        5 : "  \n||\n||\n", 
        4 : "\n(||\n ||\n",
        3 : "\n(||)\n ||\n",
        2 : "\n(||)\n ||\n /" ,
        1 : "\n(||)\n ||\n /|",
        0 : "  O\n(||)\n ||\n /|"}
    return tela[chute]

def letra_existe(palavra, letra):
    cont = 0 # casa, a
    for index,valor in enumerate(palavra):
        if (valor == letra):
            palavraAuxiliar[index] = letra 
            cont += 1
    return cont

print('\033[1;32;40mJOGO DA FORCA\033[m')
palavraFixa = "casa"
tamanho = len(palavraFixa)
palavraAuxiliar = list('-' * tamanho) 
chutes = 6
letras = 0
while chutes > 0:
    boneco = find_boneco(chutes)
    print(boneco)
    print('Sua chance atual é {}'.format(chutes))
    print("Descubra a palavra {}".format(palavraAuxiliar))
    if tamanho == letras:
        break
    letra = input()
    valor = letra_existe(palavraFixa, letra)
    if valor > 0: 
        letras += valor
        print("Acertou a letra \t")
        print("Descubra a palavra {}".format(palavraAuxiliar))
    else:
        print("Não acertou \t")
        print("Descubra a palavra {}".format(palavraAuxiliar))
        chutes-= 1
if chutes == 0:
    boneco = find_boneco(chutes)
    print("Perdeu!")
    print(boneco)
else:
    print("Ganhou!")


