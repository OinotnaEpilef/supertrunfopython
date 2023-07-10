#Autor: Antônio Felipe Ferreira de Jesus Moreira
#Componente curricular: Algoritimos I
#Concluido em 03/02/2020
#declaro que este código foi elaborado por mim de forma individual e não contém nenhum trecho de código de outro colega ou de outro autor, tais como provindos de livros e apostilas, e páginas ou documentos eletrônicos da internet. Qualquer trecho de código de outra autoria  que não a minha está destacado com uma citação para o autor e a fonte do código, e estou ciente que estes trechos não serão considerados para fins de avaliação
import random
escolha = 1
while escolha == 1 or escolha == 2:
    cartas = ['Anão', 'Elfo', 'Humano', 'Draconato', 'Gnomo', 'Meio-Elfo', 'Meio-Orc']
    print ("1- Novo jogo")
    print ("2- Instruções")
    print ("3- Sair do jogo")
    escolha = int (input ("Escolha uma opção: "))
    if escolha == 2:
        print ("Instruções")
        print ("Três cartas serão distribuidas para cada jogador(a), sendo que cada carta possui três atributos.\nO(A) jogador(a) que inicia a partida deve escolher a carta e o atributo que mais lhe convém para ser comparado.\nO(A) segundo(a) jogador(a) irá escolher apenas a carta, para que o mesmo atributo seja comparado com a carta do(a) primeiro(a) jogador(a).\nA carta com maior valor de atributo ganha, e uma pontuação será comtabilizada para definir o vencedor ao final da partida, dependendo do atributo \nInteligência = 100 pontos\nForça = 50 pontos\nDestreza = 25 pontos")
    elif escolha == 1:
        name0 = input ("Digite nickname 1: ")
        name1 = input ("Digite nickname 2: ")
        rodadas = 0
        while rodadas < 3:
            rodadas = int (input ("Digite o número de rodadas(mínimo 3): "))
    #menu de início do jogo, e seleção do número de rodadas
        for count in range(rodadas):
            num = random.randint (0,1)
            if num == 0 and num % 2 == 0:
                print (name0, "joga")
                inteligencia_c1 = random.randint(1, 10)
                forca_c1 = random.randint(11, 20)
                destreza_c1 = random.randint(21, 30)
                inteligencia_c2 = random.randint(1, 10)
                forca_c2 = random.randint(11, 20)
                destreza_c2 = random.randint(21, 30)
                inteligencia_c3 = random.randint(1, 10)
                forca_c3 = random.randint(11, 20)
                destreza_c3 = random.randint(21, 30)
                C1 = random.choice(cartas)
                C2 = random.choice(cartas)
                C3 = random.choice(cartas)
                print('1. ', C1, name0, '\n  1. Inteligência: ', inteligencia_c1, '\n  2. Força: ', forca_c1, '\n  3. Destreza: ',
                      destreza_c1)
                print('2. ', C2, name0, '\n  1. Inteligência: ', inteligencia_c2, '\n  2. Força: ', forca_c2, '\n  3. Destreza: ',
                      destreza_c2)
                print('3. ', C3, name0, '\n  1. Inteligência: ', inteligencia_c3, '\n  2. Força: ', forca_c3, '\n  3. Destreza: ',
                      destreza_c3)
            else:
                print (name1, "joga")
                inteligencia_c1 = random.randint(1, 10)
                forca_c1 = random.randint(11, 20)
                destreza_c1 = random.randint(21, 30)
                inteligencia_c2 = random.randint(1, 10)
                forca_c2 = random.randint(11, 20)
                destreza_c2 = random.randint(21, 30)
                inteligencia_c3 = random.randint(1, 10)
                forca_c3 = random.randint(11, 20)
                destreza_c3 = random.randint(21, 30)
                C1 = random.choice(cartas)
                C2 = random.choice(cartas)
                C3 = random.choice(cartas)
                print('1. ', C1, name1, '\n  1. Inteligência: ', inteligencia_c1, '\n  2. Força: ', forca_c1, '\n  3. Destreza: ',
                      destreza_c1)
                print('2. ', C2, name1, '\n  1. Inteligência: ', inteligencia_c2, '\n  2. Força: ', forca_c2, '\n  3. Destreza: ',
                      destreza_c2)
                print('3. ', C3, name1, '\n  1. Inteligência: ', inteligencia_c3, '\n  2. Força: ', forca_c3, '\n  3. Destreza: ',
                      destreza_c3)
            carta_escolhida = int(input('Digite o número da carta escolhida: '))
            atributo_escolhido = int(input('Digite o número do atributo escolhido: '))
            if carta_escolhida == 1:
                if atributo_escolhido == 1:
                    atributo_escolhido = inteligencia_c1
                elif atributo_escolhido == 2:
                    atributo_escolhido = forca_c1
                elif atributo_escolhido == 3:
                    atributo_escolhido = destreza_c1
            elif carta_escolhida == 2:
                if atributo_escolhido == 1:
                    atributo_escolhido = inteligencia_c2
                elif atributo_escolhido == 2:
                    atributo_escolhido = forca_c2
                elif atributo_escolhido == 3:
                    atributo_escolhido = destreza_c2
            elif carta_escolhida == 3:
                if atributo_escolhido == 1:
                    atributo_escolhido = inteligencia_c3
                elif atributo_escolhido == 2:
                    atributo_escolhido = forca_c3
                elif atributo_escolhido == 3:
                    atributo_escolhido = destreza_c3
#Sorteio do primeiro jogador rodar as cartas, distribuir os atributos e definir o primeiro jogador e solicitar a carta e o atributo
            print('\n'*100)
            proximo_jogador = input('Aperte enter se você for o próximo jogador')
            if num == 0:
                print (name1, "joga")
                inteligencia_c1 = random.randint(1, 10)
                forca_c1 = random.randint(11, 20)
                destreza_c1 = random.randint(21, 30)
                inteligencia_c2 = random.randint(1, 10)
                forca_c2 = random.randint(11, 20)
                destreza_c2 = random.randint(21, 30)
                inteligencia_c3 = random.randint(1, 10)
                forca_c3 = random.randint(11, 20)
                destreza_c3 = random.randint(21, 30)
                C1 = random.choice(cartas)
                C2 = random.choice(cartas)
                C3 = random.choice(cartas)
                print('1. ', C1, name1, '\n  1. Inteligência: ', inteligencia_c1, '\n  2. Força: ', forca_c1, '\n  3. Destreza: ',
                      destreza_c1)
                print('2. ', C2, name1, '\n  1. Inteligência: ', inteligencia_c2, '\n  2. Força: ', forca_c2, '\n  3. Destreza: ',
                      destreza_c2)
                print('3. ', C3, name1, '\n  1. Inteligência: ', inteligencia_c3, '\n  2. Força: ', forca_c3, '\n  3. Destreza: ',
                      destreza_c3)
            else:
                print (name0, "joga")
                inteligencia_c1 = random.randint(1, 10)
                forca_c1 = random.randint(11, 20)
                destreza_c1 = random.randint(21, 30)
                inteligencia_c2 = random.randint(1, 10)
                forca_c2 = random.randint(11, 20)
                destreza_c2 = random.randint(21, 30)
                inteligencia_c3 = random.randint(1, 10)
                forca_c3 = random.randint(11, 20)
                destreza_c3 = random.randint(21, 30)
                C1 = random.choice(cartas)
                C2 = random.choice(cartas)
                C3 = random.choice(cartas)
                print('1. ', C1, name0, '\n  1. Inteligência: ', inteligencia_c1, '\n  2. Força: ', forca_c1, '\n  3. Destreza: ',
                      destreza_c1)
                print('2. ', C2, name0, '\n  1. Inteligência: ', inteligencia_c2, '\n  2. Força: ', forca_c2, '\n  3. Destreza: ',
                      destreza_c2)
                print('3. ', C3, name0, '\n  1. Inteligência: ', inteligencia_c3, '\n  2. Força: ', forca_c3, '\n  3. Destreza: ',
                      destreza_c3)
            if atributo_escolhido == inteligencia_c1 or atributo_escolhido == inteligencia_c2 or atributo_escolhido == inteligencia_c3:
                atributo_escolhido2 = int(input('digite a carta para o seu atributo Inteligência ser comparado'))
                if atributo_escolhido2 == 1:
                    atributo_escolhido2 =inteligencia_c1
                elif atributo_escolhido2 == 2:
                    atributo_escolhido2 = inteligencia_c2
                elif atributo_escolhido2 == 3:
                    atributo_escolhido2 = inteligencia_c3
            elif atributo_escolhido == forca_c1 or atributo_escolhido == forca_c2 or atributo_escolhido == forca_c3:
                atributo_escolhido2 = int(input('digite a carta para o seu atributo Força ser comparado'))
                if atributo_escolhido2 == 1:
                    atributo_escolhido2 = forca_c1
                elif atributo_escolhido2 == 2:
                    atributo_escolhido2 = forca_c2
                elif atributo_escolhido2 == 3:
                    atributo_escolhido2 = forca_c3
            elif atributo_escolhido == destreza_c1 or atributo_escolhido == destreza_c2 or atributo_escolhido == destreza_c3:
                atributo_escolhido2 = int(input('digite a carta para o seu atributo Destreza ser comparado'))
                if atributo_escolhido2 == 1:
                    atributo_escolhido2 = destreza_c1
                elif atributo_escolhido2 == 2:
                    atributo_escolhido2 = destreza_c2
                elif atributo_escolhido2 == 3:
                    atributo_escolhido2 = destreza_c3
#escolha da carta a ser comparada pelo segundo jogador
            num +=1
            print('\n'*100)
            if atributo_escolhido > atributo_escolhido2:
                print(atributo_escolhido, ',', atributo_escolhido2, ',', name0, 'venceu a rodada')
            elif atributo_escolhido < atributo_escolhido2:
                print(atributo_escolhido, ',', atributo_escolhido2, ',', name1, 'venceu a rodada')
            else:
                print('A rodada empatou')
#definição do vencedor da rodada
        best_pontuacao = 0
        best_pontuacao2 = 0
        if atributo_escolhido != atributo_escolhido2:
            if atributo_escolhido > atributo_escolhido2:
                if atributo_escolhido == inteligencia_c1 or inteligencia_c2 or inteligencia_c3:
                    best_pontuacao += 100
                elif atributo_escolhido == forca_c1 or forca_c2 or forca_c3:
                    best_pontuacao += 50
                elif atributo_escolhido == destreza_c1 or destreza_c2 or destreza_c3:
                    best_pontuacao += 25
            elif atributo_escolhido < atributo_escolhido2:
                if atributo_escolhido2 == inteligencia_c1 or inteligencia_c2 or inteligencia_c3:
                    best_pontuacao2 += 100
                elif atributo_escolhido2 == forca_c1 or forca_c2 or forca_c3:
                    best_pontuacao2 += 50
                elif atributo_escolhido2 == destreza_c1 or destreza_c2 or destreza_c3:
                    best_pontuacao2 += 25
#definição do vencedor da partida e de seu score
        if best_pontuacao > best_pontuacao2:
            print ('Nome e pontuação do(a) jogador(a)vencedor(a)', name0, ': ', best_pontuacao)
        elif best_pontuacao2 > best_pontuacao:
            print('Nome e pontuação do(a) jogador(a) vencedor(a)', name1, ': ', best_pontuacao2)
        else:
            print('Jogadores(as)', name0, 'e', name1, 'empataram')
        if best_pontuacao > best_pontuacao and best_pontuacao2:
            print (name0, 'possui a melhor pontuação: ', best_pontuacao)
        elif best_pontuacao2 > best_pontuacao and best_pontuacao2:
            print(name1, 'possui a melhor pontuação: ', best_pontuacao2)
#definição do best score
#prezada professora. Não consegui fazer com que o segundo jogador saiba qual atributo será comparado, uma vez que para todos os atributos ou cartas selecionadas, aparece apenas como se fosse escolhido o atributo inteligência
