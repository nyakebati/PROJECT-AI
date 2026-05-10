# Project Overview

This repository contains several independent Python tasks and one Jupyter notebook. Each file is a separate exercise and is intended to be executed on its own.

## Files

### `learnNumbers (1).py`
- A handwritten neural network classifier for the MNIST digit recognition task.
- Loads the MNIST dataset from `keras.datasets`, normalizes the image data, builds a feedforward neural network with dropout, and trains the model.
- Evaluates the model on the test set and displays a few sample images with predicted vs actual labels.
- Suitable for exploring TensorFlow/Keras image classification and basic model training.

### `part a (1).py`
- Implements a simple graph coloring problem for a small map of Australian regions.
- Uses recursive backtracking to assign one of three colors to regions so that no adjacent regions share the same color.
- Prints the resulting color assignment and visualizes the map using `matplotlib`.
- This is a standalone algorithmic task focused on constraint satisfaction and backtracking.

### `part b (1).py`
- Solves a larger graph coloring problem using Nairobi sub-counties.
- Computes the minimum number of colors needed for the map and visualizes the region graph with `networkx` and `matplotlib`.
- Uses recursive backtracking with dynamic color set selection.
- Demonstrates a more complex example of map coloring and graph visualization.

### `n_queens_hill_climbing.ipynb`
- A Jupyter notebook for the N-Queens problem using hill climbing.
- Likely includes problem setup, heuristic evaluation, and iterative improvement to place N queens safely on a chessboard.
- Ideal for interactive exploration of local search algorithms and visualization of the N-Queens solution process.

### `requirements.txt`
- Lists Python dependencies used by the repository:
  - `pygame`
  - `numpy`
  - `ipython`
  - `jupyter`

## Notes

- Each `.py` file is a separate task and can be run independently.
- The repository also includes a `.venv/` directory for a virtual environment and a `.gitignore` file to exclude environment or generated files.
- To run the notebook, use Jupyter Lab or Jupyter Notebook and open `n_queens_hill_climbing.ipynb`.

## Getting Started

1. Create or activate your Python virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run one of the Python task files:
   ```bash
   python "learnNumbers (1).py"
   python "part a (1).py"
   python "part b (1).py"
   ```
4. Open the notebook:
   ```bash
   jupyter notebook n_queens_hill_climbing.ipynb
   ```
