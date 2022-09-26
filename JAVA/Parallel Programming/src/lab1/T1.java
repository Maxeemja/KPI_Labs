package lab1;

// * F1 - 1.18 d = (A*B) + (C*(B*(MA*MD)))
import java.util.Arrays;
import static lab1.Lab0.N;

public class T1 extends Thread {

    int[] A, B, C, d;
    int[][] MA, MD;

    T1(String name) {
        setName(name);
    }

    @Override
    public void run() {
        System.out.println("1st task started");

        A = Data.initVector("T1 (A)");
        B = Data.initVector("T1 (B)");
        C = Data.initVector("T1 (C)");

        MA = Data.initMatrix("T1 (MA)");
        MD = Data.initMatrix("T1 (MD)");

        d = Data.f1(A, B, C, MA, MD);

        if(N <= 10) {
            System.out.println("T1 d = " + Arrays.toString(d));
        }
        System.out.println("1st task finished. \n");
    }
}
