### Tareas — Lenguajes Formales y Compiladores (EAFIT)

Este repositorio contiene dos proyectos independientes desarrollados en Python para el curso de Lenguajes Formales y Compiladores.

- **Tarea 1**: Minimización de DFA (algoritmo de tabla de marcación de Kozen, 1997, Lecture 14).
- **Tarea 2**: Eliminación de Recursión por la Izquierda (algoritmo de Aho et al., 2006 §4.3.3).

### Autores
Samuel Henao Castrillón — David Quintero Gallego.

### Estructura

- `Tarea 1/`
  - `main.py`: implementación del algoritmo de minimización de DFA.
  - `input.txt`: ejemplo de entrada con varios casos.
  - `Readme.md` y `readme_assignment_1.md`: descripción detallada (en inglés).
- `Tarea 2/`
  - `main.py`: implementación de eliminación de recursión por la izquierda.
  - `input.txt`: ejemplo de entrada con varios casos.
  - `readme2.md`: descripción detallada (en inglés).

---

### Requisitos

- Python 3.8 o superior (probado con Python 3.11).
- No se requieren dependencias externas.

---

### Cómo ejecutar

#### Tarea 1 — Minimización de DFA

Desde la carpeta `Tarea 1/`:

```powershell
# PowerShell (Windows)
Get-Content input.txt | python .\main.py
```

```bash
# Bash (Linux/macOS/WSL)
python main.py < input.txt
```

Salida: para cada caso, una línea con los pares de estados equivalentes `(p, q)` en orden lexicográfico.

Formato de entrada (por caso):
- Una línea con `n` (cantidad de estados, 0..n-1, estado inicial 0).
- Una línea con el alfabeto separado por espacios (p. ej. `a b`).
- Una línea con los estados finales separados por espacios (puede estar vacía).
- `n` líneas con la tabla de transición, con o sin id de estado al inicio.

#### Tarea 2 — Eliminación de Recursión por la Izquierda

Desde la carpeta `Tarea 2/`:

```powershell
# PowerShell (Windows)
Get-Content input.txt | python .\main.py
```

```bash
# Bash (Linux/macOS/WSL)
python main.py < input.txt
```

Formato de entrada:
- Primera línea: número de casos `c`.
- Por cada caso:
  - Una línea con `k` (número de no terminales a leer).
  - `k` líneas con producciones en la forma `A -> ...` separadas por espacios.

Salida: las producciones resultantes sin recursión por la izquierda para cada caso, en el formato `A -> ...` (casos separados por una línea en blanco).

---

### Observaciones

- En `Tarea 2`, las instrucciones del `readme2.md` mencionan `left_recursion.py`, pero el archivo ejecutable del proyecto es `main.py`.
- Si necesitas ejemplos completos y explicación detallada, consulta los readmes dentro de cada carpeta.

---


