def obter_numeros():
    numeros = set()
    contador = 1
    while len(numeros) < 15:
        try:
            valor = int(input(f"Informe o {contador}º número: "))
            if valor in numeros:
                print("Esse número já foi digitado, tente outro.")
            else:
                numeros.add(valor)
                contador += 1
        except ValueError:
            print("Entrada inválida, digite um número inteiro.")
    return list(numeros)


def ordenar_lista(lista):
    lista_ordenada = lista[:]
    lista_ordenada.sort()
    return lista_ordenada


def calcular_dados(lista):
    total = sum(lista)
    maior_num = max(lista)
    menor_num = min(lista)
    media = total / len(lista)
    qtd_pares = len([n for n in lista if n % 2 == 0])
    qtd_impares = len(lista) - qtd_pares
    return {
        "maior": maior_num,
        "menor": menor_num,
        "soma": total,
        "media": media,
        "pares": qtd_pares,
        "impares": qtd_impares
    }


def exibir_relatorio(lista, dados):
    print("\nNúmeros em ordem crescente:", lista)
    print(f"Maior número: {dados['maior']}")
    print(f"Menor número: {dados['menor']}")
    print(f"Soma dos números: {dados['soma']}")
    print(f"Média dos números: {dados['media']:.2f}")
    print(f"Quantidade de números pares: {dados['pares']}")
    print(f"Quantidade de números ímpares: {dados['impares']}")


def executar_programa():
    numeros = obter_numeros()
    ordenados = ordenar_lista(numeros)
    resultados = calcular_dados(ordenados)
    exibir_relatorio(ordenados, resultados)


def main():
    continuar = True
    while continuar:
        executar_programa()
        escolha = input("\nDeseja rodar novamente? (s/n): ").strip().lower()
        if escolha != 's':
            print("\nEncerrando o programa...")
            continuar = False


if __name__ == "__main__":
    main()