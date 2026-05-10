# Prolog Logic Programming

This folder contains Prolog logic programming exercises focused on knowledge representation and rule-based reasoning.

## Files

### `family.pl`
- A Prolog program that models family relationships using facts and rules.
- Defines base facts about parent relationships and gender.
- Implements logical rules to derive complex relationships such as:
  - Mother, father, and child relationships
  - Sibling relationships
  - Grandparent and grandchild relationships
  - Aunts, uncles, and cousins
- Demonstrates the power of declarative programming where you specify **what** the relationships are rather than **how** to compute them.
- Ideal for learning logic programming fundamentals, unification, and backtracking in Prolog.

## Running the Code

1. Ensure Prolog is installed on your system (e.g., SWI-Prolog).
2. Load the file in a Prolog interpreter:
   ```bash
   swipl family.pl
   ```
3. Query relationships interactively at the Prolog prompt:
   ```prolog
   ?- mother(X, jacob).
   ?- sibling(esau, jacob).
   ?- grandchild(X, abraham).
   ?- cousin(X, Y).
   ```

## Key Concepts

- **Facts**: Base statements about the world (e.g., `parent(sarah, issac)`)
- **Rules**: Logical implications derived from facts (e.g., `mother(M, C) :- parent(M, C), gender(M, female)`)
- **Unification**: Matching variables to values and other variables
- **Backtracking**: Automatic search through possible solutions
- **Queries**: Questions asked about the knowledge base to retrieve solutions

## Relationships Defined

| Relationship | Definition |
|---|---|
| `mother(M, C)` | M is the mother of C |
| `father(F, C)` | F is the father of C |
| `child(C, P)` | C is a child of P |
| `sibling(X, Y)` | X and Y are siblings (share a parent) |
| `grandfather(GF, GC)` | GF is the grandfather of GC |
| `grandmother(GM, GC)` | GM is the grandmother of GC |
| `grandchild(GC, GP)` | GC is a grandchild of GP |
| `uncle(U, C)` | U is an uncle of C |
| `aunt(A, C)` | A is an aunt of C |
| `cousin(X, Y)` | X and Y are cousins |
