def Conversao(wt_gerados, consumo, Saldo):
    from Menu import Menu_Principal

    taxa_de_conversao = 6.5

    while not wt_gerados:
        print("\nVocê não possui nenhum saldo de energia para ser convertido.")
        input("\nPressione enter para continuar")
        Menu_Principal(wt_gerados, consumo, Saldo)

    while True:
        try:
            perg_conversão = int(input(f"\nProsseguindo, você irá converter todos os seus kWh gerados em saldo de SolarCoins\nNeste momento você possui: {wt_gerados} kWh\nVocê deseja converter?\n1 - Sim\n2 - Não\nR: "))
            if perg_conversão in {1, 2}:
                break
            else: 
                print("Opção inválida.")
        except ValueError:
            print("\nEntrada inválida. Digite um número.")

    # 1 SolarCoin vale 10 centavos
    # 1 kWh vale 65 centavos
    # 1 kWh vale 6,5 SolarCoins

    if perg_conversão == 1:
        Saldo =+  wt_gerados * taxa_de_conversao
        wt_gerados = 0
        print(f"\nSeu saldo é de: {Saldo} SolarCoins")
        input("\nPressione enter para continuar")
        return Saldo and wt_gerados, Menu_Principal(wt_gerados, consumo, Saldo)

    elif perg_conversão == 2:
        print("\nRetornando ao Menu Principal")
        Menu_Principal(wt_gerados, consumo, Saldo)


def Compra(wt_gerados, consumo, Saldo):
    from Menu import Menu_Principal

    while True:
        try:
            perg_compra = int(input("\nBem-vindo a nossa loja\n\n1 - 1 Mês de Alura\nPreço: 1250 SolarCoins\n\n2 - Gift Card Playstation\nPreço: 1000 SolarCoins\n\n3 - Gift Card Spotify \nPreço: 219 SolarCoins\n\n4 - Pix equivalente ao saldo\nOBS: 1 SolarCoin = R$0.10\n\nO que deseja?\nR: "))
            if perg_compra in {1, 2, 3, 4}:
                break
            else: print("\nOpção inválida")
        except ValueError:
            print("\nEntrada inválida, Digite um número.")

    if perg_compra == 1:
        print("\nO código para 1 mês de Alura será enviado para o seu e-mail")
        Saldo -= 1250
        print(f"\nSeu saldo agora é de {Saldo} SolarCoins")
        input("\nPressione enter para continuar")

    elif perg_compra == 2:
        print("\nO código para R$100 na plataforma Playstation será enviado para o seu e-mail")
        Saldo -= 1000
        print(f"\nSeu saldo agora é de {Saldo} SolarCoins")
        input("\nPressione enter para continuar")

    elif perg_compra == 3:
        print("\nO código para 1 mês de Spotify Premium será enviado para o seu e-mail")
        Saldo -= 219
        print(f"\nSeu saldo agora é de {Saldo} SolarCoins")
        input("\nPressione enter para continuar")

    elif perg_compra == 4:
        print("\nO pix equivalente ao saldo de SolarCoins da sua conta será enviado para sua conta bancária")
        Saldo = 0
        print(f"\nSeu saldo agora é de {Saldo} SolarCoins")
        input("\nPressione enter para continuar")

    return Saldo, Menu_Principal(wt_gerados, consumo, Saldo)