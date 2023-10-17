//Landon Reese - Conways Game of Life in Java

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        
        Board b = new Board();
        int letter;

        System.out.println("Welcome to Conway's Game of Life!");
        String fileName = "/Users/landonreese/Documents/GitHub/Resume-Collection/Resume-Projects/Game-Of-Life/Start.txt";
        FileInputStream file = null;
        //String fileName = "LandonReeseGameOfLife/src/Start.txt";
        try {
            // Read the file from desired location.
            file = new FileInputStream(new File(fileName));

            for(int r = 0; r < 20; r++){
                for(int c = 0; c < 20; c++) {
                    letter = file.read();
                    if (letter == 10)
                        letter = file.read();
                    if (letter == 88)
                        b.setAliveCell(r, c);
                }

            }

        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        int generations = file.read(); //10 for the new line right before generations

        generations = file.read();
        generations = generations - '0'; //Converts ascii back to an integer



        GameState gs = new GameState(b);

        b.displayBoard();

        System.out.println("Simulating " + generations + " generations: ");

        for(int i = 0; i < generations; i++) {
            gs.Update();
            System.out.println();
            b.displayBoard();
        }
        
        s.close();
    }

}

/*
John Conway's Game of Life

Write a Java program to implement the Game of Life, as defined by John Conway:

1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.


Your program should use a 20 x 20 grid, and accept the initial grid configuration in a form similar to the following
(this example would be for a 4 x 4 grid):

....
.XX.
.XX.
....
5


Where the dot (period) indicates an empty square, and some other character
(‘X’ in the example) indicates an inhabited square.

The last line of the file will contain an integer value, indicating the number of generations to compute.
Your program should compute and show the final configuration in the same format as the input.

Think about proper class design, loosely-coupled classes, testability, etc.

 */
