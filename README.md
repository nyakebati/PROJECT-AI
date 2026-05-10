# Project Overview

This repository contains multiple independent tasks covering machine learning, algorithms, constraint satisfaction, logic programming, and search strategies. Each task is separate and can be executed independently.

## Tasks by Category

### Machine Learning

#### `learnNumbers (1).py`
- A handwritten neural network classifier for the MNIST digit recognition task.
- Loads the MNIST dataset from `keras.datasets`, normalizes the image data, builds a feedforward neural network with dropout, and trains the model.
- Evaluates the model on the test set and displays a few sample images with predicted vs actual labels.
- Suitable for exploring TensorFlow/Keras image classification and basic model training.

### Constraint Satisfaction Problems (CSP)

### `learnNumbers (1).py`
- A handwritten neural network classifier for the MNIST digit recognition task.
- Loads the MNIST dataset from `keras.datasets`, normalizes the image data, builds a feedforward neural network with dropout, and trains the model.
- Evaluates the model on the test set and displays a few sample images with predicted vs actual labels.
- Suitable for exploring TensorFlow/Keras image classification and basic model training.

### Constraint Satisfaction Problems (CSP)

#### `MNIST/part a (1).py`
- Implements a simple graph coloring problem for a small map of Australian regions.
- Uses recursive backtracking to assign one of three colors to regions so that no adjacent regions share the same color.
- Prints the resulting color assignment and visualizes the map using `matplotlib`.
- This is a standalone algorithmic task focused on constraint satisfaction and backtracking.

#### `MNIST/part b (1).py`
- Solves a larger graph coloring problem using Nairobi sub-counties.
- Computes the minimum number of colors needed for the map and visualizes the region graph with `networkx` and `matplotlib`.
- Uses recursive backtracking with dynamic color set selection.
- Demonstrates a more complex example of map coloring and graph visualization.

### Local Search Algorithms

#### `n_queens_hill_climbing.ipynb`
- A Jupyter notebook for the N-Queens problem using hill climbing.
- Likely includes problem setup, heuristic evaluation, and iterative improvement to place N queens safely on a chessboard.
- Ideal for interactive exploration of local search algorithms and visualization of the N-Queens solution process.

### Search Algorithms

#### `search algorithms/BFS.ipynb`
- A Jupyter notebook implementing Breadth-First Search (BFS) and Depth-First Search (DFS).
- Builds a graph structure using a Node class and visualizes the search process.
- Demonstrates how BFS explores all neighbors at the current depth before moving deeper (using a queue).
- Shows how DFS explores deeply along each branch before backtracking (using a stack).
- Includes graph visualization using `networkx` and `matplotlib`.

### Logic Programming

#### `PROLOG/` folder
- Contains Prolog logic programming exercises.
- See [prolog.md](PROLOG/prolog.md) for detailed information.

#### `PROLOG/family.pl`
- Models family relationships using Prolog facts and rules.
- Demonstrates knowledge representation and logical inference through family relationship definitions.
- Shows how to query complex relationships like siblings, grandparents, aunts, uncles, and cousins.
## Notes

- Each task is self-contained and can be run independently.
- Folders are organized by task category:
  - `MNIST/` - Graph coloring constraint satisfaction problems
  - `search algorithms/` - Search algorithm implementations
  - `PROLOG/` - Logic programming exercises
- The repository includes a `.venv/` directory for a virtual environment and a `.gitignore` file.
- Dependencies are listed in `requirements.txt` at the root level and in individual folders if needed.

## Getting Started

1. Create or activate your Python virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run Python tasks:
   ```bash
   python "learnNumbers (1).py"
   python "MNIST/part a (1).py"
   python "MNIST/part b (1).py"
   ```
4. Open Jupyter notebooks:
   ```bash
   jupyter notebook n_queens_hill_climbing.ipynb
   jupyter notebook "search algorithms/BFS.ipynb"
   ```
5. Run Prolog (requires SWI-Prolog installation):
   ```bash
   swipl PROLOG/family.pl
   ```
   Then query at the Prolog prompt:
   ```prolog
   ?- mother(X, jacob).
   ?- sibling(esau, jacob).
   ?- cousin(X, Y).
   ```
