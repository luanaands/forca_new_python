
def letra_existe(palavra, letra):
    cont = 0
    for i, c in enumerate(palavra):
        if (c == letra):
            palavraAuxiliar[i] = letra
            cont += 1
    if (cont > 0): 
        print("Acertou a letra \t")
        print("Descubra a palavra {}".format(palavraAuxiliar))
    else:
        print("Não acertou \t")
        print("Descubra a palavra {}".format(palavraAuxiliar))

# fixo 
# chances = 5
# chute  
cont = 0
palavraFixa = "palavra"
tamanho = len(palavraFixa)

""" aqui converte em lista (string to lista), 
isso foi feito para a gente conseguir substituir a letra encotrada, 
mas ainda temos o problema de ter mais de uma letra na palavra """
palavraAuxiliar = list('-' * tamanho) 

print("Descubra a palavra {}".format(palavraAuxiliar))
letra = input()

letra_existe(palavraFixa, letra)



"""
QuatidadeDeChances = 5
while True:
   
    print('-' * tamanho)


    for i in range(QuatidadeDeChances):
        print('Sua chance atual é {}'.format(QuatidadeDeChances-i))
        letra = input()
        
   """


  

