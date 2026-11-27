import random

historico = []

disponiveis = list(range(1, 76))

while disponiveis:
    comando = input("\nPressione ENTER para sortear (ou digite 'sair'): ").strip().lower()
    if comando == "sair":
        break

    numero = random.choice(disponiveis)
    disponiveis.remove(numero)

    historico.append(numero)

    print(f"\nNúmeros sorteados: {numero}")
    print(f"Histórico (ordem do sorteio): {historico}")
    print(f"Histórico (em ordem crescente): {sorted(historico)}")