def exibir_circulo(raio):
    """Exibe um círculo em asteriscos com o raio fornecido."""
    # Define o tamanho da grade com base no raio
    for y in range(-raio, raio + 1):
        linha = ""
        for x in range(-raio, raio + 1):
            # Verifica se o ponto (x, y) está próximo do perímetro do círculo
            if x**2 + y**2 <= raio**2 + raio * 0.5 and x**2 + y**2 >= raio**2 - raio * 0.5:
                linha += "*"
            else:
                linha += " "
        print(linha)

# Solicita ao usuário o raio do círculo
raio = int(input("Digite o raio do círculo (número inteiro): "))
exibir_circulo(raio)
input()