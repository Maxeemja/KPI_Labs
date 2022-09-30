package lab1;

/**
 * Parallel programming.
 * Labwork 02, Threads in Java
 * Maksym Hrytsiuk
 * IO-02
 * 26.09.22
 * F1 - 1.18 d = (A*B) + (C*(B*(MA*MD)))
 * F2 - 2.24 MG = SORT(MF - MH * MK)
 * F3 - 3.23 s = MAX((MO*MP)(R + V))
 **/

public class Lab0 extends Thread {
    public static final int N = 1000;

    public static void main(String[] args) {
        (new Lab0()).start();
    }

    @Override
    public void run() {
        System.out.println("Lab0 started\n");

        T1 t1 = new T1("Function 1");
        T2 t2 = new T2("Function 2");
        T3 t3 = new T3("Function 3");

        t1.start();
        t2.start();
        t3.start();

        try {
            t1.join();
            t2.join();
            t3.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("Lab 0 ended");
    }
}
