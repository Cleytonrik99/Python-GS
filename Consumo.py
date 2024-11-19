def Geracao(wt_gerados, consumo, Saldo):
    from Menu import Menu_Principal

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
    from Menu import Menu_Principal
    
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
    from Menu import Menu_Principal

    while not consumo:
        print("\nNão é possível executar esta função pois não há nenhum dado de consumo")
        Menu_Principal(wt_gerados, consumo, Saldo)
        
    media = 0

    for dias in consumo:
        media += dias["consumo"]

    tamanho = len(consumo)

    media_consumo = media / tamanho

    print(f"\nAtualmente, este é seu consumo\n{consumo}")
    print(f"\nA média do consumo é: {media_consumo:.2f}kWh")            

    input("\nPressione enter para continuar")

    return consumo, Menu_Principal(wt_gerados, consumo, Saldo)


def Visualizar(wt_gerados, consumo, Saldo):
    from Menu import Menu_Principal

    print("\nAtualmente, estes são seus dados")

    print(f"\nSeus dados de consumo:\n{consumo}")

    print(f"\nSeu saldo de kWh gerados: {wt_gerados} kWh")

    print(f"\nSeu saldo de SolarCoins: {Saldo} SolarCoins")

    input("\nPressione enter para continuar")

    Menu_Principal(wt_gerados, consumo, Saldo)

