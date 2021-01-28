# fixo 
# chances = 5
# chute  
cont = 0
palavraFixa = "gato"
tamanho = len(palavraFixa)

""" aqui converte em lista (string to lista), 
isso foi feito para a gente conseguir substituir a letra encotrada, 
mas ainda temos o problema de ter mais de uma letra na palavra """
palavraAuxiliar = list('-' * tamanho) 

print("Descubra a palavra {}".format(palavraAuxiliar))
letra = input()
index = palavraFixa.find(letra)
if (index != -1):
    palavraAuxiliar[index] = letra
print("Descubra a palavra {}".format(palavraAuxiliar))



"""
QuatidadeDeChances = 5
while True:
   
    print('-' * tamanho)


    for i in range(QuatidadeDeChances):
        print('Sua chance atual é {}'.format(QuatidadeDeChances-i))
        letra = input()
        
   """


  

