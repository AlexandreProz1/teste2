# Enunciado:

# Vocês foram designados para criarem uma calculadora simples que permita aos usuários realizar operações básicas, como adição, subtração, multiplicação e divisão. O programa deve continuar executando até que o usuário escolha sair. Cada vez que uma operação é concluída, o usuário deve ter a opção de realizar outra operação ou sair do programa.

# Requisitos:

# Utilize um loop while para permitir que o programa continue executando até que o usuário escolha sair.
# Ofereça as opções de soma, subtração, multiplicação, divisão e saída.
# Solicite ao usuário os números necessários para realizar a operação escolhida.
# Mostre o resultado da operação e pergunte se o usuário deseja realizar outra operação ou sair.

while True:
    # Apresenta as opções ao usuário
    print("\nCalculadora Simples:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    # Solicita a escolha do usuário
    escolha = input("Escolha a operação (1/2/3/4/5): ")

    # Verifica a escolha do usuário
    if escolha == '5':
        print("Obrigado por usar a calculadora. Até logo!")
        break  # Sai do loop se o usuário escolher sair
    elif escolha in {'1', '2', '3', '4'}:
        # Solicita os números para a operação
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        # Realiza a operação escolhida
        if escolha == '1':
            resultado = num1 + num2
            operacao = 'Somaa'
        elif escolha == '2':
            resultado = num1 - num2
            operacao = 'subtração'
        elif escolha == '3':
            resultado = num1 * num2
            operacao = 'multiplicação'
        elif escolha == '4':
            # Certifica-se de não dividir por zero
            if num2 != 0:
                resultado = num1 / num2
                operacao = 'divisão'
            else:
                print("Erro: Não é possível dividir por zero. Tente novamente.")
                continue  # Reinicia o loop sem realizar a operação

        # Exibe o resultado da operação
        print(f"Resultado da {operacao}: {resultado}")
    else:
        print("Escolha inválida. Tente novamente.")