"""
ST0270 Formal Languages and Compilers
Assignment 2: Elimination of Left Recursion
Implementation of the algorithm from Aho et al. 2006, Section 4.3.3
"""

def parse_grammar(lines):
    """
    Parse grammar productions from input lines.
    Returns a dictionary where keys are nonterminals and values are lists of productions.
    """
    grammar = {}
    for line in lines:
        if '->' not in line:
            continue
        parts = line.strip().split('->')
        nonterminal = parts[0].strip()
        productions = parts[1].strip().split()
        # Acumular producciones si el no terminal aparece en varias líneas
        if nonterminal not in grammar:
            grammar[nonterminal] = []
        grammar[nonterminal].extend(productions)
    return grammar


def is_nonterminal(symbol):
    """Check if a symbol is a nonterminal (uppercase letter)."""
    return symbol and symbol[0].isupper()


def substitute_productions(grammar, A, B):
    """
    Substitute all productions of B into productions of A that start with B.
    This eliminates productions of the form A -> Bα by replacing them with A -> δα
    for each production B -> δ.
    """
    new_productions = []
    
    for production in grammar[A]:
        if production[0] == B:  # Production starts with B
            # Get the rest of the production after B
            alpha = production[1:] if len(production) > 1 else ''
            
            # For each production of B, create a new production for A
            for b_prod in grammar[B]:
                new_productions.append(b_prod + alpha)
        else:
            # Keep productions that don't start with B
            new_productions.append(production)
    
    grammar[A] = new_productions


def eliminate_immediate_left_recursion(grammar, A, new_nonterminals):
    """
    Eliminate immediate left recursion for nonterminal A.
    Transforms productions:
        A -> Aα1 | Aα2 | ... | Aαm | β1 | β2 | ... | βn
    Into:
        A -> β1A' | β2A' | ... | βnA'
        A' -> α1A' | α2A' | ... | αmA' | ε
    """
    alpha_productions = []  # Productions with left recursion (A -> Aα)
    beta_productions = []   # Productions without left recursion (A -> β)
    
    # Separate recursive and non-recursive productions
    for production in grammar[A]:
        if production[0] == A:  # Left recursive
            alpha = production[1:] if len(production) > 1 else ''
            alpha_productions.append(alpha)
        else:  # Not left recursive
            beta_productions.append(production)
    
    # If no left recursion, nothing to do
    if not alpha_productions:
        return
    
    # Find a new nonterminal name (next available letter)
    new_nt = get_next_nonterminal(new_nonterminals)
    new_nonterminals.add(new_nt)
    
    # Create new productions for A
    new_A_productions = []
    for beta in beta_productions:
        new_A_productions.append(beta + new_nt)
    
    # Create productions for the new nonterminal
    new_nt_productions = []
    for alpha in alpha_productions:
        new_nt_productions.append(alpha + new_nt)
    new_nt_productions.append('e')  # Add ε production
    
    # Update grammar
    grammar[A] = new_A_productions
    grammar[new_nt] = new_nt_productions


def get_next_nonterminal(used_nonterminals):
    """
    Find the next available nonterminal (uppercase letter).
    """
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if letter not in used_nonterminals:
            return letter
    # If all single letters are used, this shouldn't happen in typical cases
    raise ValueError("No more nonterminal names available")


def eliminate_left_recursion(grammar):
    """
    Eliminate all left recursion from the grammar using the algorithm
    from Aho et al. 2006, Section 4.3.3.
    
    Algorithm:
    1. Order nonterminals: A1, A2, ..., An
    2. For i = 1 to n:
        a. For j = 1 to i-1:
            Replace each production Ai -> Ajα with Ai -> δ1α | δ2α | ... | δkα
            where Aj -> δ1 | δ2 | ... | δk
        b. Eliminate immediate left recursion among Ai productions
    """
    # Get ordered list of nonterminals (starting with S if present)
    nonterminals = list(grammar.keys())
    if 'S' in nonterminals:
        nonterminals.remove('S')
        nonterminals.insert(0, 'S')
    else:
        nonterminals.sort()
    
    # Keep track of newly created nonterminals
    new_nonterminals = set(nonterminals)
    
    n = len(nonterminals)
    
    # Main algorithm
    for i in range(n):
        Ai = nonterminals[i]
        
        # Step 2a: Substitute previous nonterminals
        for j in range(i):
            Aj = nonterminals[j]
            substitute_productions(grammar, Ai, Aj)
        
        # Step 2b: Eliminate immediate left recursion
        eliminate_immediate_left_recursion(grammar, Ai, new_nonterminals)
    
    return grammar


def format_output(grammar):
    """
    Format grammar for output.
    Maintains order with original nonterminals first, then new ones.
    """
    lines = []
    
    # Get nonterminals in order: S first, then alphabetically
    nonterminals = sorted(grammar.keys())
    if 'S' in nonterminals:
        nonterminals.remove('S')
        nonterminals.insert(0, 'S')
    
    for nt in nonterminals:
        productions = ' '.join(grammar[nt])
        lines.append(f"{nt} -> {productions}")
    
    return '\n'.join(lines)


def main():
    # Read number of cases
    n = int(input().strip())
    
    results = []
    
    for case in range(n):
        # Read number of nonterminals
        k = int(input().strip())
        
        # Read productions
        lines = []
        for _ in range(k):
            lines.append(input().strip())
        
        # Parse grammar
        grammar = parse_grammar(lines)
        
        # Eliminate left recursion
        grammar = eliminate_left_recursion(grammar)
        
        # Format output
        results.append(format_output(grammar))
    
    # Print all results
    for i, result in enumerate(results):
        print(result)
        if i < len(results) - 1:
            print()  # Blank line between cases


if __name__ == "__main__":
    main()