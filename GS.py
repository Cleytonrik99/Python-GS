def Inicio():
    consumo = []
    wt_gerados = 0
    Saldo = 0

    while True:
        try:
            perg_inicio = int(input("\nBem Vindo a Plataforma SolarCash\n\n1 - Adicionar Watts gerados\n2 - Encerrar Programa\nO que deseja?\nR: "))
            if perg_inicio in {1, 2}:
                break
            print("\nOpção inválida. Escolha uma opção entre 1 ou 2.")
        except ValueError:
            print("\nEntrada inválida. Digite um número.")

    if perg_inicio == 1:
        Geracao(wt_gerados, consumo, Saldo)
    elif perg_inicio == 2:
        Encerrar()

    return Saldo        


def Menu_Principal(wt_gerados, consumo, Saldo):
    while True:
        try:
            perg_menu = int(input("\nMenu principal\n\n1 - Adicionar Watts gerados\n2 - Adicionar consumo\n3 - Calcular Media do consumo\n4 - Converter kWh em saldo\n5 - Visualizar seus dados\n6 - Trocar SolarCoins por produtos\n7 - Encerrar Programa\nO que deseja?\nR: "))
            if perg_menu in {1, 2, 3, 4, 5, 6, 7}:
                break
            else: print("\nOpção inválida")
        except ValueError:
            print("\nEntrada inválida, Digite um número.")

    if perg_menu == 1:
        Geracao(wt_gerados, consumo, Saldo)
    elif perg_menu == 2:
        Add_Consumo(wt_gerados, consumo, Saldo)
    elif perg_menu == 3:
        Media(wt_gerados, consumo, Saldo)
    elif perg_menu == 4:
        Conversao(wt_gerados, consumo, Saldo)
    elif perg_menu == 5:
        Visualizar(wt_gerados, consumo, Saldo) 
    elif perg_menu == 6:
        Compra(wt_gerados, consumo, Saldo)
    elif perg_menu == 7:
        Encerrar()        


def Geracao(wt_gerados, consumo, Saldo):
    while True:
        try:
            perg_wt_gerados = int(input("\nInsira a quantidade de kWh gerados: "))
            if perg_wt_gerados > 0:
                break
            print("\nOpção inválida")
        except ValueError:
            print("\nEntrada inválida, Digite um número.")

    wt_gerados += perg_wt_gerados

    print(f"\nFoi adicionado {wt_gerados} kWh em seu saldo de Geração")
    input("\nPressione enter para continuar")

    return wt_gerados, Menu_Principal(wt_gerados, consumo, Saldo)    


def Add_Consumo(wt_gerados, consumo, Saldo):
    periodo = 0
    verificar_consumo = 0
   
    while wt_gerados == 0:
        print("\nNão é possível usar esta função")
        input("\nPressione enter para continuar")
        Menu_Principal(wt_gerados, consumo, Saldo)

    while True:
        try:
            perg_periodo_consumo = int(input("\nInsira o periodo de consumo\n1 - Dia\n2 - Semana\n3 - Mês\nQual seria?\nR: "))
            if perg_periodo_consumo in {1, 2, 3}:
                break
            print("\nOpção inválida.")
        except ValueError:
            print("\nEntrada inválida. Digite um número.")    

    if perg_periodo_consumo == 1:
        periodo = 1
    elif perg_periodo_consumo == 2:
        periodo = 7
    elif perg_periodo_consumo == 3:
        periodo = 30

    for i in range(periodo):
        i += 1

        while True:
            try:
                consumo_no_periodo = float(input(f"Consumo no dia {i}: "))
                if consumo_no_periodo > 0:
                    break
                print("\nOpção inválida.")
            except ValueError:
                print("\nEntrada inválida. Digite um número.")

        verificar_consumo += consumo_no_periodo

        if verificar_consumo <= wt_gerados:
            consumo.append({"Dia": i, "consumo": consumo_no_periodo})
        else: 
            print("\nEntrada não aceita\nVocê tentou consumir mais do que gerou")
            break    

    print(f"\nSeu consumo adicionado é: \n{consumo}")

    input("\nPressione enter para continuar")

    wt_gerados -= verificar_consumo

    return consumo, Menu_Principal(wt_gerados, consumo, Saldo)


def Media(wt_gerados, consumo, Saldo):
    while not consumo:
        print("\nNão é possível executar esta função pois não há nenhum dado de consumo")
        Menu_Principal(wt_gerados, consumo, Saldo)
        
    media = 0

    for dias in consumo:
        media += dias["consumo"]

    tamanho = len(consumo)

    media_consumo = media / tamanho

    print(f"\nAtualmente, este é seu consumo\n{consumo}")
    print(f"\nA média do consumo é: {media_consumo:.4f}kWh")            

    input("\nPressione enter para continuar")

    return consumo, Menu_Principal(wt_gerados, consumo, Saldo)    


def Conversao(wt_gerados, consumo, Saldo):
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


def Visualizar(wt_gerados, consumo, Saldo):
    print("\nAtualmente, estes são seus dados")

    print(f"\nSeus dados de consumo:\n{consumo}")

    print(f"\nSeu saldo de kWh gerados: {wt_gerados} kWh")

    print(f"\nSeu saldo de SolarCoins: {Saldo} SolarCoins")

    input("\nPressione enter para continuar")

    Menu_Principal(wt_gerados, consumo, Saldo)


def Compra(wt_gerados, consumo, Saldo):
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


def Encerrar():
    exit()


Inicio()    