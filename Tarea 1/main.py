
def minimization_algorithm(n, alphabet, final_states, transitions):
    """Algoritmo de minimización de DFA usando método de llenado de tabla."""
    final_states = set(final_states)
    distinguishable = [[False] * n for _ in range(n)]

    # Marcar pares final vs no-final
    for i in range(n):
        for j in range(i + 1, n):
            if (i in final_states) != (j in final_states):
                distinguishable[i][j] = True

    # Propagación iterativa
    changed = True
    while changed:
        changed = False
        for i in range(n):
            for j in range(i + 1, n):
                if not distinguishable[i][j]:
                    for k in range(len(alphabet)):
                        ni = transitions[i][k]  # Estado destino desde i
                        nj = transitions[j][k]  # Estado destino desde j
                        x, y = (ni, nj) if ni < nj else (nj, ni)  # Normalizar orden
                        if distinguishable[x][y]:
                            distinguishable[i][j] = True
                            changed = True
                            break

    # Recopilar pares equivalentes
    equivalent_pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            if not distinguishable[i][j]:
                equivalent_pairs.append((i, j))
    return equivalent_pairs


def main():
    """Función principal que procesa la entrada y ejecuta la minimización."""
    import sys
    data = sys.stdin.read().strip().splitlines()
    it = iter(data)

    c = int(next(it).strip())  # Número de casos
    for _ in range(c):
        n = int(next(it).strip())  # Número de estados
        alphabet = next(it).strip().split()  # Alfabeto
        final_states = list(map(int, next(it).strip().split()))  # Estados finales

        transitions = []
        for _s in range(n):
            row = list(map(int, next(it).strip().split()))
            # Manejar formato con/sin ID de estado
            if len(row) == len(alphabet) + 1:
                row = row[1:]  # Quitar ID del estado
            if len(row) > len(alphabet):
                row = row[:len(alphabet)]  # Truncar si es necesario
            transitions.append(row)

        pairs = minimization_algorithm(n, alphabet, final_states, transitions)
        print(" ".join(f"({a}, {b})" for a, b in pairs))  # Formato requerido


if __name__ == "__main__":
    main()
