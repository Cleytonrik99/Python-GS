def Conversao(wt_gerados, consumo, Saldo):
    # Função de conversão

    from Menu import Menu_Principal

    # Criação de variável de conversão
    # 1 SolarCoin vale 10 centavos
    # 1 kWh vale 65 centavos
    # 1 kWh vale 6,5 SolarCoins
    taxa_de_conversao = 6.5

    # Tratamento de erro, caso o saldo de energia gerada seja 0
    while not wt_gerados:
        print("\nVocê não possui nenhum saldo de energia para ser convertido.")
        input("\nPressione enter para continuar")
        Menu_Principal(wt_gerados, consumo, Saldo)

    # Entrada do usuário para confirmação da ação
    while True:
        try:
            perg_conversão = int(input(f"\nProsseguindo, você irá converter todos os seus kWh gerados em saldo de SolarCoins\nNeste momento você possui: {wt_gerados} kWh\nVocê deseja converter?\n1 - Sim\n2 - Não\nR: "))
            if perg_conversão in {1, 2}:
                break
            else: 
                print("Opção inválida.")
        except ValueError:
            print("\nEntrada inválida. Digite um número.")

    # Saldo de energia gerada sendo multiplicada pela taxa de conversão e sendo adicionada ao saldo de SolarCoins
    # Saldo de energia sendo zerado, já que foi "vendido"
    # Exibição do saldo de SolarCoins após a conversão
    if perg_conversão == 1:
        Saldo =+  wt_gerados * taxa_de_conversao
        wt_gerados = 0
        print(f"\nSeu saldo é de: {Saldo} SolarCoins")
        input("\nPressione enter para continuar")
        return Saldo and wt_gerados, Menu_Principal(wt_gerados, consumo, Saldo)

    # Retorno ao menu principal caso a resposta da confirmação seja "Não"
    elif perg_conversão == 2:
        print("\nRetornando ao Menu Principal")
        Menu_Principal(wt_gerados, consumo, Saldo)


def Compra(wt_gerados, consumo, Saldo):
    # Função de loja

    from Menu import Menu_Principal

    # Entrada do usuário, sendo apresentado as opções de itens vendidos
    while True:
        try:
            perg_compra = int(input(f"\nBem-vindo a nossa loja\n\n1 - 1 Mês de Alura\nPreço: 1250 SolarCoins\n\n2 - Gift Card Playstation\nPreço: 1000 SolarCoins\n\n3 - Gift Card Spotify \nPreço: 219 SolarCoins\n\n4 - Pix equivalente ao saldo\nOBS: 1 SolarCoin = R$0.10\n\nAtualmente seu saldo é de {Saldo} SolarCoins\n\nO que deseja?\nR: "))
            if perg_compra in {1, 2, 3, 4}:
                break
            else: print("\nOpção inválida")
        except ValueError:
            print("\nEntrada inválida, Digite um número.")

    # Confirmação de item vendido
    # Desconto do preço do item no saldo do cliente
    # Exibição de saldo atual
    if perg_compra == 1:
        if Saldo >= 1250:
            print("\nO código para 1 mês de Alura será enviado para o seu e-mail")
            Saldo -= 1250
            print(f"\nSeu saldo agora é de {Saldo} SolarCoins")
            input("\nPressione enter para continuar")
        else:
            print("Saldo insuficiente")
            input("\nPressione enter para continuar")

    elif perg_compra == 2:
        if Saldo >= 1000:
            print("\nO código para R$100 na plataforma Playstation será enviado para o seu e-mail")
            Saldo -= 1000
            print(f"\nSeu saldo agora é de {Saldo} SolarCoins")
            input("\nPressione enter para continuar")
        else:
            print("Saldo insuficiente")
            input("\nPressione enter para continuar") 

    elif perg_compra == 3:
        if Saldo >= 219:
            print("\nO código para 1 mês de Spotify Premium será enviado para o seu e-mail")
            Saldo -= 219
            print(f"\nSeu saldo agora é de {Saldo} SolarCoins")
            input("\nPressione enter para continuar")
        else:
            print("Saldo insuficiente")
            input("\nPressione enter para continuar")

    elif perg_compra == 4:
        if Saldo >= 1:
            print("\nO pix equivalente ao saldo de SolarCoins da sua conta será enviado para sua conta bancária")
            Saldo = 0
            print(f"\nSeu saldo agora é de {Saldo} SolarCoins")
            input("\nPressione enter para continuar")
        else:
            print("Saldo insuficiente")
            input("\nPressione enter para continuar")

    return Saldo, Menu_Principal(wt_gerados, consumo, Saldo)