public class LandonThread extends Thread{
    int r;
    int c;
    boolean status;
    public LandonThread(int r, int c){
        this.r = r;
        this.c = c;
    }

    public void run() {
        
    }
    
    public int getRow(){
        return r;
    }
    public int getCol(){
        return c;
    }
    public boolean getStatus(){
        return status;
    }
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
