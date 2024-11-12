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
    perg_inicio = int(input("\nBem Vindo a Plataforma SolarCash\n\n\npiriri pororo: "))

    if perg_inicio == 1:
        calculo()

    

def calculo():
    consumo = []
    periodo = 0
    media = 0

    perg_periodo_consumo = input("\nInsira o periodo de consumo\n1 - Semana\n2 - Mês\nQual seria?: ")

    while perg_periodo_consumo.isnumeric() == False and (perg_periodo_consumo != 1 or perg_periodo_consumo != 2):
        perg_periodo_consumo = input("\nOpção inválida\nTente novamente\n1 - Semana\n2 - Mês\nQual seria?: ")

    if perg_periodo_consumo == "1":
        periodo = 7
    elif perg_periodo_consumo == "2":
        periodo = 30

    for i in range(periodo):
        i+= 1

        consumo_no_periodo = int(input(f"Consumo no dia {i}: "))
        
        consumo.append(consumo_no_periodo)

    print(consumo)
    
    for i in consumo:
        media += i

    media_consumo = media / periodo

    print(media_consumo)    

calculo()    