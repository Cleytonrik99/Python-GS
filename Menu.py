def Inicio():
    # Função de menu inicial

    from Consumo import Geracao

    # Criação da lista de consumo, saldo de kWh gerados e saldo de SolarCoins
    consumo = []
    wt_gerados = 0
    Saldo = 0

    # Entrada do usuário, sendo limitado a adicionar geração de energia
    while True:
        try:
            perg_inicio = int(input("\nBem Vindo a Plataforma SolarCash\n\n1 - Adicionar Watts gerados\n2 - Encerrar Programa\nO que deseja?\nR: "))
            if perg_inicio in {1, 2}:
                break
            print("\nOpção inválida. Escolha uma opção entre 1 ou 2.")
        except ValueError:
            print("\nEntrada inválida. Digite um número.")

    # Chamada de função correspondente a escolha do usuário
    if perg_inicio == 1:
        Geracao(wt_gerados, consumo, Saldo)
    elif perg_inicio == 2:
        Encerrar()

    return Saldo        


def Menu_Principal(wt_gerados, consumo, Saldo):
    # Função do Menu principal

    from Consumo import Geracao, Add_Consumo, Media, Visualizar
    from Saldo import Conversao, Compra

    # Entrada do usuário, sendo apresentado as opções
    while True:
        try:
            perg_menu = int(input("\nMenu principal\n\n1 - Adicionar Watts gerados\n2 - Adicionar consumo\n3 - Calcular Media do consumo\n4 - Converter kWh em saldo\n5 - Visualizar seus dados\n6 - Trocar SolarCoins por produtos\n7 - Encerrar Programa\nO que deseja?\nR: "))
            if perg_menu in {1, 2, 3, 4, 5, 6, 7}:
                break
            else: print("\nOpção inválida")
        except ValueError:
            print("\nEntrada inválida, Digite um número.")

    # Chamada de função correspondente a escolha do usuário
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


def Encerrar():
    exit()


def main():
    Inicio()


if __name__ == "__main__":
    main()

# Mostrar para Pedro e Matheus
# Fazer o vídeo