# while True:
#     try:
#         perg_inicio = int(input("\nBem Vindo a Plataforma SolarCash\n\n1 - Adicionar Wolts gerados\n2 - Adicionar consumo\n3 - Calcular Media do consumo\n4 - Encerrar Programa\nO que deseja?: "))
        
#         if perg_inicio not in [1, 2, 3, 4]:
#             raise ValueError("\nOpção inválida. Escolha uma opção entre 1 e 4.")
#         break  # Encerra o loop se a entrada for válida

#     except ValueError as e:
#         print(e)  # Exibe a mensagem de erro

while True:
    try:
        perg_inicio = int(input("\nBem Vindo a Plataforma SolarCash\n\n1 - Adicionar Wolts gerados\n2 - Adicionar consumo\n3 - Calcular Media do consumo\n4 - Encerrar Programa\nO que deseja?: "))
        if perg_inicio in {1, 2, 3, 4}:
            break  # Encerra o loop se a entrada for válida
        print("\nOpção inválida. Escolha uma opção entre 1 e 4.")
    except ValueError:
        print("\nEntrada inválida. Digite um número.")
