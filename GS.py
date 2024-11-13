def Inicio():
    consumo = []
    wt_gerados = 0

    while True:
        try:
            perg_inicio = int(input("\nBem Vindo a Plataforma SolarCash\n\n1 - Adicionar Wolts gerados\n2 - Adicionar consumo\n3 - Calcular Media do consumo\n4 - Encerrar Programa\nO que deseja?: "))
            if perg_inicio in {1, 2, 3, 4}:
                break
            print("\nOpção inválida. Escolha uma opção entre 1 e 4.")
        except ValueError:
            print("\nEntrada inválida. Digite um número.")

    if perg_inicio == 1:
        Geracao(wt_gerados)
    elif perg_inicio == 2:
        Add_Consumo(consumo)
    elif perg_inicio == 3:
        Media(consumo)
    elif perg_inicio == 4:
        Encerrar()    


def Menu_Principal(consumo):
    while True:
        try:
            perg_menu = int(input("\nMenu principal\n\n1 - Adicionar consumo\n2 - Calcular Media do consumo\n3 - Encerrar Programa\nO que deseja?: "))
            if perg_menu in {1, 2, 3}:
                break
            print("\nOpção inválida")
        except ValueError:
            print("\nEntrada inválida, Digite um número.")

    if perg_menu == 1:
        Add_Consumo(consumo)
    elif perg_menu == 2:
        Media(consumo)
    elif perg_menu == 3:
        Encerrar()        


def Geracao(wt_gerados):
    while True:
        try:
            perg_wt_gerados = int(input("\nInsira a quantidade de Watts gerados: "))
            if perg_wt_gerados > 0:
                break
            print("\nOpção inválida")
        except ValueError:
            print("\nEntrada inválida, Digite um número.")


def Add_Consumo(consumo):
    periodo = 0
   
    while True:
        try:
            perg_periodo_consumo = int(input("\nInsira o periodo de consumo\n1 - Dia\n2 - Semana\n3 - Mês\nQual seria?: "))
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
        i+= 1

        consumo_no_periodo = int(input(f"Consumo no dia {i}: "))
        
        consumo.append(consumo_no_periodo)

    print(consumo)
    return consumo, Menu_Principal(consumo)


def Media(consumo):
    while not consumo:
        print("\nNão é possível executar esta função pois não há nenhum dado de consumo")
        Inicio()
        
    media = 0

    for i in consumo:
        media += i

    tamanho = len(consumo)

    media_consumo = media / tamanho

    print(f"\n{media_consumo}")

    return consumo, Menu_Principal(consumo)    


def Encerrar():
    exit()

Inicio()    