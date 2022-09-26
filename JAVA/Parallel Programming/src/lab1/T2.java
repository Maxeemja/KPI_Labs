package lab1;
import static lab1.Lab0.N;

//* F2 - 2.24 MG = SORT(MF - MH * MK)
public class T2 extends Thread {
    int[][] MF, MH, MK, MG;

    T2(String name) {
        setName(name);
    }

    @Override
    public void run() {
        System.out.println("2nd task started");

        MF = Data.initMatrix("T2 (MF)");
        MH = Data.initMatrix("T2 (MH)");
        MK = Data.initMatrix("T2 (MK)");
        MG = Data.f2(MF, MH, MK);

        try {
            sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        if(N <= 10) {
            System.out.println("(T2) MG: ");
            Data.printMatrix(MG);
        }
        System.out.println("2nd task finished. \n");
    }
}
