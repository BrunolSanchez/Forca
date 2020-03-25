palavra = input("Escolha uma palavra: ").lower()
erros = 0
digitadas = [] #Guardar os dados
erradas = [] #Guardar as erradas
acertos = [] #guardar os acertos 

for i in range(100): #deixar um espaço enormossauro entre a palavra secreta e o jogo.
    print("")

while True: #Enquanto
    senha = "" #Serve para guardar a palavra
    for chute in palavra:
        senha += chute if chute in acertos else " _ " #juntar a palavra com a letra
    print(senha)
    if senha == palavra:
        print("Na mosca!") #"Se acertar a palavra entao, ta certo" - Werner, 2019.
        break
    tentativa = input("Digite uma letra: ") #Digitar uma letra dentro do jogo a força
    if tentativa in digitadas:
        print("Você já tentou essa aí... ") #Caso a palavra ja tenha sido digitada
    else:
        digitadas += tentativa #Os chutes serão listados nas tentativas
        if tentativa in palavra:
            acertos += tentativa  #Se o chute estiver certo, ele constará no programa
        else:
            erros = erros +1 #Contagem de erros
            erradas += tentativa 
            print("Você errou!", erradas)
    if erros == 6: 
        print("Enforcado!")
        break #Fim!
