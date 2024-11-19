def Geracao(wt_gerados, consumo, Saldo):
    # Função de Geração de kWh

    from Menu import Menu_Principal

    # Entrada do usuário, informando sua quantidade de kWh gerados
    while True:
        try:
            perg_wt_gerados = int(input("\nInsira a quantidade de kWh gerados: "))
            if perg_wt_gerados > 0:
                break
            print("\nOpção inválida")
        except ValueError:
            print("\nEntrada inválida, Digite um número.")

    # Adição dos kWh ao saldo correspondente
    wt_gerados += perg_wt_gerados

    # Confirmação da ação 
    print(f"\nFoi adicionado {wt_gerados} kWh em seu saldo de Geração")
    input("\nPressione enter para continuar")

    return wt_gerados, Menu_Principal(wt_gerados, consumo, Saldo)


def Add_Consumo(wt_gerados, consumo, Saldo):
    # Função de consumo

    from Menu import Menu_Principal
    
    # Criação de variáveis de periodo e verificação de consumo
    periodo = 0
    verificar_consumo = 0
   
    # Tratamento de erro no caso do saldo de kWh gerado seja 0
    while wt_gerados == 0:
        print("\nNão é possível usar esta função")
        input("\nPressione enter para continuar")
        Menu_Principal(wt_gerados, consumo, Saldo)

    # Entrada do usuário, informando o periodo do consumo
    while True:
        try:
            perg_periodo_consumo = int(input("\nInsira o periodo de consumo\n1 - Dia\n2 - Semana\n3 - Mês\nQual seria?\nR: "))
            if perg_periodo_consumo in {1, 2, 3}:
                break
            print("\nOpção inválida.")
        except ValueError:
            print("\nEntrada inválida. Digite um número.")    

    # Modificação da variável "periodo" de acordo com a entrada do usuário
    if perg_periodo_consumo == 1:
        periodo = 1
    elif perg_periodo_consumo == 2:
        periodo = 7
    elif perg_periodo_consumo == 3:
        periodo = 30

    # Entrada do usuário sobre consumo nos dias
    # A quantidade de dias será o número armazenado na variável "periodo"
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


        # Tratamento de erro, em caso do usuário tentar consumir mais do que seu saldo de kWh
        verificar_consumo += consumo_no_periodo

        if verificar_consumo <= wt_gerados:
            consumo.append({"Dia": i, "consumo": consumo_no_periodo})
        else: 
            print("\nEntrada não aceita\nVocê tentou consumir mais do que gerou")
            break    

    # Confirmação de consumo adicionado
    print(f"\nSeu consumo adicionado é: \n{consumo}")

    input("\nPressione enter para continuar")

    # Quantidade de energia utilizada sendo descontada do saldo
    wt_gerados -= verificar_consumo

    return consumo, Menu_Principal(wt_gerados, consumo, Saldo)


def Media(wt_gerados, consumo, Saldo):
    # Função de media

    from Menu import Menu_Principal

    # Tratamento de erro em caso de o usuário não ter adicionado nenhum consumo
    while not consumo:
        print("\nNão é possível executar esta função pois não há nenhum dado de consumo")
        Menu_Principal(wt_gerados, consumo, Saldo)
    
    # Criação da variável de média
    media = 0

    # Adição do consumo de cada dia fornecido pelo usuário, sendo adicionado na variável "media"
    for dias in consumo:
        media += dias["consumo"]

    # Variável de tamanho, tendo o numero de dias de consumo do usuário
    tamanho = len(consumo)

    # Cálculo de média, com a variável "media" sendo dividida pela variável "tamanho" 
    media_consumo = media / tamanho

    # Exibição do consumo, junto da média do mesmo
    print(f"\nAtualmente, este é seu consumo\n{consumo}")
    print(f"\nA média do consumo é: {media_consumo:.2f}kWh")            

    input("\nPressione enter para continuar")

    return consumo, Menu_Principal(wt_gerados, consumo, Saldo)


def Visualizar(wt_gerados, consumo, Saldo):
    # Função de visualização de dados

    from Menu import Menu_Principal

    # Exibição dos dados de consumo, saldo de kWh e saldo de SolarCoins do usuário
    print("\nAtualmente, estes são seus dados")

    print(f"\nSeus dados de consumo:\n{consumo}")

    print(f"\nSeu saldo de kWh gerados: {wt_gerados} kWh")

    print(f"\nSeu saldo de SolarCoins: {Saldo} SolarCoins")

    input("\nPressione enter para continuar")

    Menu_Principal(wt_gerados, consumo, Saldo)