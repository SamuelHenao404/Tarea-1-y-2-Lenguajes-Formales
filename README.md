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

- `Tarea 2/`
  - `main.py`: implementación de eliminación de recursión por la izquierda.
  - `input.txt`: ejemplo de entrada con varios casos.


---

### Objetivos de aprendizaje

- Comprender y aplicar el algoritmo de minimización de DFA por llenado de tabla.
- Transformar gramáticas para eliminar recursión por la izquierda siguiendo el método clásico (Aho).
- Practicar lectura y escritura de formatos de entrada/salida estrictos en problemas de compiladores.

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

Ejemplo mínimo:

```
1
3
a b
1
0 1 2
1 1 2
2 2 2
```

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

Ejemplo mínimo:

```
1
1
S -> Sa b
```

Salida esperada (esquema):

```
S -> bA
A -> aA e
```




