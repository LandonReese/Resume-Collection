import java.util.ArrayList;

//Landon Reese
public class Board implements Runnable, Update{
    Boolean[][] CurrentBoard = new Boolean[20][20];
    Boolean[][] ThreadBoard  = new Boolean[20][20]; //We use threadboard to update currentboard >:D
    ArrayList<LandonThread> threads = new ArrayList<LandonThread>();
    LandonThread L;

    public Board(){
        for(int i = 0; i < 20; i++){
            for(int j = 0; j < 20; j++) {
                CurrentBoard[i][j] = false;

            }
        }
        ThreadBoard = CurrentBoard;
    }

// 1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
// 2. Any live cell with two or three live neighbors lives on to the next generation.
// 3. Any live cell with more than three live neighbors dies, as if by overpopulation.
// 4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

    //Calculates the next generation and stores in NextBoard
    public Boolean[][] calculateNext(){ //Throw threads here IF POSSIBLE
        Boolean[][] NextBoard = new Boolean[20][20];
        //int ThreadCount = 1;
        for(int i = 0; i < 20; i++) {
            for (int j = 0; j < 20; j++) {
                //Thread t = new Thread(""+ThreadCount);
                //t.start();
                //ThreadCount++;
                if(CurrentBoard[i][j] == true) { //If the cell is alive
                    //Rule #1
                    if (calculateAliveNeighbors(i, j) < 2)
                        NextBoard[i][j] = false;

                    //Rule #2
                    else if (calculateAliveNeighbors(i, j) == 2 || calculateAliveNeighbors(i, j) == 3)
                        NextBoard[i][j] = true;

                    //Rule #3
                    else if (calculateAliveNeighbors(i, j) > 3)
                        NextBoard[i][j] = false;
                } else { //Cell is dead
                    //Rule #4
                    if (calculateAliveNeighbors(i, j) == 3)
                        NextBoard[i][j] = true;
                    else
                        NextBoard[i][j] = false;
                }
            }

        }
        CurrentBoard = NextBoard;
        return CurrentBoard;
    }

    public void setAliveCell(int row, int col){
        if((row > 20 || row < 0) || (col > 20 || col < 0)) {
            System.out.println("Invalid input, please try again.");
        } else {
            CurrentBoard[row][col] = true;
        }
    }

    //calculates and returns the total number of adjacent alive neighbors
    public int calculateAliveNeighbors(int row, int col){
        int num = 0;

        if(row == 0 && col == 0){ //Top left corner case
            if(CurrentBoard[row+1][col])   {num++;} //down
            if(CurrentBoard[row][col+1])   {num++;} //right
            if(CurrentBoard[row+1][col+1]) {num++;} //down-right
        }

        else if(row == 0 && col == 19){ //Top right corner case
            if(CurrentBoard[row+1][col])   {num++;} //down
            if(CurrentBoard[row][col-1])   {num++;} //left
            if(CurrentBoard[row+1][col-1]) {num++;} //down-left
        }

        else if(row == 19 && col == 0){ //Bottom left corner case
            if(CurrentBoard[row-1][col])   {num++;} //up
            if(CurrentBoard[row][col+1])   {num++;} //right
            if(CurrentBoard[row-1][col+1]) {num++;} //up-right
        }

        else if(row == 19 && col == 19){ //Bottom right corner case
            if(CurrentBoard[row-1][col])   {num++;} //up
            if(CurrentBoard[row][col-1])   {num++;} //left
            if(CurrentBoard[row-1][col-1]) {num++;} //up-left
        }

        else if(row == 0 && (col > 0 && col < 19)){ //Top edge case
            if(CurrentBoard[row][col-1])     {num++;} //left
            if(CurrentBoard[row][col+1])     {num++;} //right
            if(CurrentBoard[row+1][col-1])   {num++;} //down-left
            if(CurrentBoard[row+1][col])     {num++;} //down
            if(CurrentBoard[row+1][col+1])   {num++;} //down-right
        }

        else if(row == 19 && (col > 0 && col < 19)){ //Bottom edge case
            if(CurrentBoard[row][col-1])     {num++;} //left
            if(CurrentBoard[row][col+1])     {num++;} //right
            if(CurrentBoard[row-1][col-1])   {num++;} //up-left
            if(CurrentBoard[row-1][col])     {num++;} //up
            if(CurrentBoard[row-1][col+1])   {num++;} //up-right
        }

        else if(col == 0 && (row > 0 && row < 19)){ //Left edge case
            if(CurrentBoard[row-1][col])     {num++;} //up
            if(CurrentBoard[row+1][col])     {num++;} //down
            if(CurrentBoard[row-1][col+1])   {num++;} //up-right
            if(CurrentBoard[row][col+1])     {num++;} //right
            if(CurrentBoard[row+1][col+1])   {num++;} //down-right
        }

        else if(col == 19 && (row > 0 && row < 19)){ //Right edge case
            if(CurrentBoard[row-1][col])     {num++;} //up
            if(CurrentBoard[row+1][col])     {num++;} //down
            if(CurrentBoard[row-1][col-1])   {num++;} //up-left
            if(CurrentBoard[row][col-1])     {num++;} //left
            if(CurrentBoard[row+1][col-1])   {num++;} //down-left
        }

        else {
            if(CurrentBoard[row-1][col-1])   {num++;} //up-left
            if(CurrentBoard[row-1][col])     {num++;} //up
            if(CurrentBoard[row-1][col+1])   {num++;} //up-right
            if(CurrentBoard[row][col-1])     {num++;} //left
            if(CurrentBoard[row][col+1])     {num++;} //right
            if(CurrentBoard[row+1][col-1])   {num++;} //down-left
            if(CurrentBoard[row+1][col])     {num++;} //down
            if(CurrentBoard[row+1][col+1])   {num++;} //down-right
        }

        return num; //returns number of alive neighbors
    }

    public void displayBoard(){
        for(int i = 0; i < 20; i++){
            for(int j = 0; j < 20; j++){
                if(CurrentBoard[i][j] == true) {
                    System.out.print('X');// + " "); //if true
                } else {
                    System.out.print('.');// + " "); //if false
                }
            }
            System.out.println();
        }

    }

    public void displayThreadBoard(){
        for(int i = 0; i < 20; i++){
            for(int j = 0; j < 20; j++){
                if(ThreadBoard[i][j] == true) {
                    System.out.print('X');// + " "); //if true
                } else {
                    System.out.print('.');// + " "); //if false
                }
            }
            System.out.println();
        }
    }

    public void setDefaultBoard(){
        for(int i = 1; i < 19; i++){
            for(int j = 1; j < 19; j++){
                CurrentBoard[i][j] = true;
            }
        }
    }


    public boolean calculateOneCell(int r, int c){ //Throw threads here IF POSSIBLE
        if(CurrentBoard[r][c]) { //If the cell is alive
            //System.out.println("Entering calculateOneCell(r,c)");
            //Rule #1
            if (calculateAliveNeighbors(r, c) < 2)
                return false;

                //Rule #2
            else if (calculateAliveNeighbors(r, c) == 2 || calculateAliveNeighbors(r, c) == 3)
                return true;

                //Rule #3
            else if (calculateAliveNeighbors(r, c) > 3)
                return false;
        } else { //Cell is dead
            //Rule #4
            if (calculateAliveNeighbors(r, c) == 3)
                return true;
            else
                return false;
        }
        return false;
    }
    @Override
    public void run() {
        //System.out.println("Board-speak");
        for(int r = 0; r < 20; r++){
            for(int c = 0; c < 20; c++) {
                LandonThread t = new LandonThread(r, c);
                threads.add(t);
                t.start();

                t.status = calculateOneCell(r, c); //should adjust every thread's status to true or false

            }
        }
        for(LandonThread t: threads) {
            try {
                t.join();
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }

        for(LandonThread t: threads){
            if(t.status)
                setAliveCell(t.getRow(), t.getCol());
        }
        CurrentBoard = ThreadBoard;
    }

    @Override
    public void Update() {

    }
}

//Revise the previous game of life programming assignment to use
//threads, such that each cell uses a separate thread to determine
//its state in the next generation.  One thread per cell per
//generation is acceptable.  For extra credit, one thread per cell
// that handles multiple generations is better, albeit more difficult.
