# Conway's Game of Life Java Implementation

This project presents a multi-threaded Java implementation of Conway's Game of Life, a classic cellular automaton. The implementation utilizes parallel processing to efficiently compute the next generation of the game.

## Features and Implementation

- **Multi-Threaded Processing:** The program leverages multiple threads for the parallel processing of the game, enhancing performance and computation speed.

- **Game Board Management:** Classes have been designed to manage the game board, allowing for efficient storage and manipulation of cell states.

- **Game State Handling:** The implementation includes a mechanism for maintaining the state of the game across multiple generations, facilitating the simulation of the game's evolution.

- **Cell State Representation:** Individual cell states are managed and updated based on the core rules of Conway's Game of Life. A cell can be either alive ('X') or dead ('.').

- **Initial Configuration Input:** Users can input the initial game board configuration by defining the state of each cell in a file, with 'X' representing an alive cell and '.' representing a dead cell.

- **Simulation of Generations:** The program simulates the evolution of the game over a specified number of generations. Each generation represents a new state of the game board.

## Getting Started

To use this program, follow these steps:

1. Open Start.txt to input the initial game board configuration. Use 'X' for alive cells and '.' for dead cells.

2. Specify the number of generations you want to run in the same file.

3. Run the Java program to initiate the simulation.

4. Observe the evolution of the Game of Life over the specified number of generations.

