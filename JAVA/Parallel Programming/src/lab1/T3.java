package lab1;

// * F3 - 3.23 s = MAX((MO*MP)(R + V))
public class T3 extends Thread {
    int s;
    int[] R, V;
    int[][] MO, MP;

    T3(String name) {
        setName(name);
    }

    @Override
    public void run() {
        System.out.println("3rd task started \n");

        R = Data.initVector("T3 (R)");
        V = Data.initVector("T3 (V)");

        MO = Data.initMatrix("T3 (MO)");
        MP = Data.initMatrix("T3 (MP)");

        s = Data.f3(R, V, MO, MP);

        try {
            sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("(T3) s = " + s);
        System.out.println("3rd task finished. \n");
    }
}
