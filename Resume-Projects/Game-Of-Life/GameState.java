//Landon Reese

import java.util.Stack;
public class GameState implements Update{
    Board Board = new Board();
    Stack GameState = new Stack<Board>();


    public GameState(Board b){
        this.Board = b;
        GameState.push(b);
    }

    @Override
    public void Update() {
        Board NextBoard = Board;
        NextBoard.run();
        NextBoard.CurrentBoard = NextBoard.ThreadBoard;
        addMove(NextBoard);
    }

    public void addMove(Board state){
        GameState.push(state);
    }

    public void deleteMove(){
        GameState.pop();
    }

    /*

arrayList<LandonThread> threads = new ... //then

for(int r = 0; r < 20; r++){
    for(int c = 0; c < 20; c++){


        thread t = new LandonThread(r,c);
        t.start();
        threads.add(t);

        computeonecell(r,c);
        }
}

        for(thread t: threads) t.join();  //join ensures that all of the threads join back together
                                          //into one single thread after each generation finishes
*/
}
