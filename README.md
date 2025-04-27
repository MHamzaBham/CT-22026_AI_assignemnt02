# AI Assignment 02: Tic-Tac-Toe with Minimax and Alpha-Beta Pruning

This project implements a Tic-Tac-Toe game with two AI strategies: **Minimax** and **Alpha-Beta Pruning**. It also includes performance measurement and visualization of the two algorithms.

## Features
- Play Tic-Tac-Toe against an AI.
- Two AI strategies:
  - **Minimax**: Basic decision-making algorithm.
  - **Alpha-Beta Pruning**: Optimized version of Minimax.
- Performance comparison between the two algorithms.
- Visualization of performance metrics using Matplotlib.

## How to Run
1. Clone the repository or download the code.
2. Ensure you have Python installed along with the required libraries:
   ```bash
   pip install matplotlib
   ```
3. Run the script:
   ```bash
   python script_name.py
   ```
4. Follow the on-screen instructions to play the game or view the performance comparison.

## Video Demonstration
[![Watch the video](https://via.placeholder.com/640x360.png?text=Click+to+Watch+Demo)](https://drive.google.com/file/d/1qm6AaaMYNVYmr2wJHyCfan7VlPmNvdpV/view?usp=sharing)

## Notebook Link
[Google Colab Notebook](https://colab.research.google.com/drive/16coLSgZ4AK57J4SAebzyWHW7ZmmHg-th?usp=sharing).

## Code Overview
- **Game Logic**: Implements the Tic-Tac-Toe game, including board creation, move validation, and winner detection.
- **Minimax Algorithm**: Explores all possible moves to determine the best outcome.
- **Alpha-Beta Pruning**: Optimized version of Minimax that reduces the number of nodes evaluated.
- **Performance Measurement**: Compares the average execution time of both algorithms.
- **Visualization**: Plots the performance comparison using Matplotlib.

## Example Output
### Game Board
```
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
```

### Performance Comparison
- **Minimax Average Time**: 0.012345 seconds
- **Alpha-Beta Pruning Average Time**: 0.006789 seconds
