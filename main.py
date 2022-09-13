import random

jogador1 = ()
jogador2 = ()
maquina1 = ()
maquina2 = ()
escolha = ()
continuar = 1


print("digite 1 para jogador contra maquina")
print("digite 2 para jogador contra jogador")
print("digite 3 para maquina contra maquina")
escolha = float(input("Qual sua escolha?"))
if escolha == 1:
    while continuar == 1:
        print("digite 1 para pedra")
        print("digite 2 para tesoura")
        print("digite 3 para papel")
        jogador1 = float(input("Qual sua jogada?"))
        maquina1 = random.randrange(1, 3)
        if jogador1 == 1:
            if maquina1 == 1:
                print("Deu empate.")
            else:
                if maquina1 == 2:
                    print("Parabéns, você ganhou!!!")
                else:
                    print("Que pena, você perdeu.")
        if jogador1 == 2:
            if maquina1 == 1:
                print("Que pena, você perdeu.")
            else:
                if maquina1 == 2:
                    print("Deu empate.")
                else:
                    print("Que pena, você perdeu.")
        if jogador1 == 3:
            if maquina1 == 1:
                print("Parabéns, você venceu!!!")
            else:
                if maquina1 == 2:
                    print("Que pena, você perdeu.")
                else:
                    print("Deu empate.")
        print("Digite 1 para continuar")
        print("digite 2 para fechar")
        continuar = float(input("qual sua escolha?"))

if escolha == 2:
     while continuar == 1:
        print("digite 1 para pedra")
        print("digite 2 para tesoura")
        print("digite 3 para papel")
        jogador1 = float(input("Jogador 1, qual a sua jogada?"))
        jogador2 = float(input("Jogador 2, qual a sua jogada?"))
        if jogador1 == 1:
            if jogador2 == 1:
                print("Deu empate.")
            else:
                if jogador2 == 2:
                    print("Jogador 1 venceu!!!")
                else:
                    print("Jogador 2 venceu!!!")
        if jogador1 == 2:
            if jogador2 == 1:
                print("Jogador 2 venceu!!!")
            else:
                if jogador2 == 2:
                    print("Deu empate.")
                else:
                    print("Jogador 1 venceu!!!")
        if jogador1 == 3:
            if jogador2 == 1:
                print("jogador 1 venceu!!!")
            else:
                if jogador2 == 2:
                    print("Jogador 2 venceu!!!")
                else:
                    print("Deu empate.")
        print("Digite 1 para continuar")
        print("digite 2 para fechar")
        continuar = float(input("qual sua escolha?"))
if escolha == 3:
     while continuar == 1:
        maquina1 = random.randrange(1, 3)
        maquina2 = random.randrange(1, 3)
        if maquina1 == 1:
            if maquina2 == 1:
                print("Deu empate.")
            else:
                if maquina2 == 2:
                    print("Máquina 1 venceu!!!")
                else:
                    print("Máquina 2 venceu!!!")
        if maquina1 == 2:
            if maquina2 == 1:
                print("Máquina 2 venceu!!!")
            else:
                if maquina2 == 2:
                    print("Deu empate.")
                else:
                    print("Máquina 1 venceu!!!")
        if maquina1 == 3:
            if maquina2 == 1:
                print("Máquina 1 venceu!!!")
            else:
                if maquina2 == 2:
                    print("Máquina 2 venceu!!!")
                else:
                    print("Deu empate.")
        print("Digite 1 para continuar")
        print("digite 2 para fechar")
        continuar = float(input("qual sua escolha?"))

if continuar == 2:
    print("xauzinho:), obrigado por jogar.")