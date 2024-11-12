"""

Aplicativo vai focar no algoritmo de conversão de energia para o saldo

Por enquanto no código cru, o usuário vai inserir as informações

Vai ser bem parecido a cp3
Com menu inicial e menu principal sendo liberado depois

- Entrada do usuário
- Menu
- 

"""

def Inicio():
    consumo = []

    perg_inicio = input("\nBem Vindo a Plataforma SolarCash\n\n1 - Adicionar consumo\n2 - Calcular Media do consumo\n3 - Encerrar Programa\nO que deseja?: ")

    while perg_inicio.isnumeric() == False and (perg_inicio != "1" or perg_inicio != "2"):
        perg_inicio = input("\nOpção inválida\n\n1 - Adicionar consumo\n2 - Calcular Media do consumo\n3 - Encerrar Programa\nO que deseja?: ")

    if perg_inicio == "1":
        Add_Consumo(consumo)
    elif perg_inicio == "2":
        Media(consumo)
    elif perg_inicio == "3":
        Encerrar()    


def Menu_Principal(consumo):

    perg_menu = input("\nMenu principal\n\n1 - Adicionar consumo\n2 - Calcular Media do consumo\n3 - Encerrar Programa\nO que deseja?: ")

    while perg_menu.isnumeric() == False and (perg_menu != "1" or perg_menu != "2"):
        perg_menu = input("\nOpção inválida\n\n1 - Adicionar consumo\n2 - Calcular Media do consumo\n3 - Encerrar Programa\nO que deseja?: ")

    if perg_menu == "1":
        Add_Consumo(consumo)
    elif perg_menu == "2":
        Media(consumo)        


def Add_Consumo(consumo):
    periodo = 0
    

    perg_periodo_consumo = input("\nInsira o periodo de consumo\n1 - Dia\n2 - Semana\n3 - Mês\nQual seria?: ")

    while perg_periodo_consumo.isnumeric() == False and (perg_periodo_consumo != "1" or perg_periodo_consumo != "2" or perg_periodo_consumo != "3"):
        perg_periodo_consumo = input("\nOpção inválida\nTente novamente\n1 - Dia\n2 - Semana\n3 - Mês\nQual seria?: ")

    if perg_periodo_consumo == "1":
        periodo = 1
    elif perg_periodo_consumo == "2":
        periodo = 7
    elif perg_periodo_consumo == "3":
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