c = input('Digite uma sequencia de numeros de 1 e 0: ')

ini = 0
qtdPulos = 0 #Variaveis.
print(c)

for i in range(ini, len(c) -1, 1): #Contagem do vetor do começo ao fim.
  if i == ini: #O valor da posição i se torna o inicio para que o programa continue a verificar se pode pular sem recomeçar da primeira posição

    if i < len(c) - 2 and c[i+2] == '1'  : # O i < len(c) - 2 serve para que o programa não conte mais 2 casas para frente se caso ele for sair da quantidade de lajotas se i = 13, então i + 2 não existira e o c[i+2] == 1 serve para verificar se existe o valor 1 duas lajotas depois da posição inicial.
      qtdPulos += 1 #Adiciona 1 pulo.
      ini = i + 2 #O valor i se torna a nova posição incial do gato.

    elif( c[i+1] == '1' ): #Caso o gato não consigo pular duas lajotas ele verifica se é possivel pular para a proxima lajota.
      qtdPulos += 1 #Adiciona 1 pulo.
      ini = i + 1 #O valor i se torna a nova posição inicial do gato.
    else:
      
      qtdPulos = -1 # Caso o gato não consigo pular duas ou uma lajota, ele não pula nenhuma vez.

    print("Posição do gato = " ,ini) #Posição que o gato pulou.

    print("Quantidade de pulos = " ,qtdPulos) #Quantidade de vezes que ele pulou até ali.
