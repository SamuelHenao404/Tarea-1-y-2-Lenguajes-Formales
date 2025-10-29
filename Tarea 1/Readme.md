# Assignment 1 - Formal Languages and Compilers  
**University:** EAFIT  
**Course:** Formal Languages and Compilers (Lenguajes Formales y Compiladores)  
**Assignment:** 1 - DFA Minimization (Kozen 1997, Lecture 14)  

---

## **Authors**
- Samuel Henao Castrillón  
- [Add your partner's full name here]  

---

## **Description**
This program implements the DFA minimization algorithm described in *Kozen, Dexter C. (1997), Lecture 14*.  
Given a deterministic finite automaton (DFA) **without inaccessible states**, the algorithm identifies pairs of **equivalent states** that can be merged to produce a minimized automaton.  

The implementation follows the **table-filling algorithm**:
1. **Mark pairs** where one state is final and the other is not.  
2. **Iteratively refine** the marking table: if two states transition to a marked pair under any input symbol, mark them as distinguishable.  
3. **Output unmarked pairs** as equivalent states, in lexicographical order.  

---

## **Input Format**
The input must follow these rules:
1. A line with an integer `c` (> 0) representing the number of cases.  
2. For each case:
   - A line with integer `n` (> 0) for the number of states.  
   - A line with the alphabet symbols, separated by spaces.  
   - A line with the final states, separated by spaces.  
   - `n` lines with the transition table.  
     - Each line starts with the state number, followed by its transitions in the same order as the alphabet.

---

## **Output Format**
For each case, print **all equivalent state pairs** `(p, q)` in lexicographical order, separated by spaces, all in one line per case.

---

## **Example**

**Input:**
