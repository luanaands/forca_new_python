def find_boneco(chute):
    tela = { 7 : "", 
        6 : "  \n||\n||\n", 
        5 : "\n(||\n ||\n",
        4 : "\n(||)\n ||\n",
        3 : "\n(||)\n ||\n /" ,
        2 : "\n(||)\n ||\n /|",
        1 : "\n(||)\n ||\n /|",
        0 : "  O\n(||)\n ||\n /|"}
    return tela[chute]

def letra_existe(palavra, letra):
    cont = 0
    for i, c in enumerate(palavra):
        if (c == letra):
            palavraAuxiliar[i] = letra
            cont += 1
    return cont

palavraFixa = "palavra"
tamanho = len(palavraFixa)
palavraAuxiliar = list('-' * tamanho) 
chutes = 7
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


