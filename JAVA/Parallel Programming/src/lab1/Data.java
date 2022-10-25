package lab1;

import java.util.Arrays;
import java.util.concurrent.CyclicBarrier;
import java.util.concurrent.Semaphore;
import java.util.concurrent.atomic.AtomicInteger;

public class Data {
    public static final int N = 4;
    public static final int P = 4;
    public static final int H = N / P;

    public static int[][] MC = new int[N][N];
    public static int[][] MD = new int[N][N];

    public static int[] A = new int[N];
    public static int[] B = new int[N];
    public static int[] R = new int[N];
    public static int[] Z = new int[N];
    public static int[] E = new int[N];
    public static int[] X = new int[N];

    public static int d = 0;
    public static int p = 0;
    public static AtomicInteger a = new AtomicInteger();

    public static final Object W = new Object();
    public static final Object Y = new Object();

    // Елементи взаємодії
    public static Semaphore Sem2 = new Semaphore(1, true);
    public static Semaphore Sem3 = new Semaphore(0, true);
    public static Semaphore Sem4 = new Semaphore(0, true);
    public static Semaphore Sem5 = new Semaphore(0, true);
    public static Semaphore Sem6 = new Semaphore(0, true);
    public static Semaphore Sem7 = new Semaphore(0, true);
    public static Semaphore Sem8 = new Semaphore(0, true);
    public static Semaphore Sem9 = new Semaphore(0, true);
    public static Semaphore Sem10 = new Semaphore(0, true);
    public static Semaphore Sem11 = new Semaphore(0, true);
    public static Semaphore Sem12 = new Semaphore(0, true);
    public static Semaphore Sem13 = new Semaphore(0, true);
    public static Semaphore Sem14 = new Semaphore(0, true);


    public static CyclicBarrier Bar1 = new CyclicBarrier(4);

    public static void calculateResultPart(int ai, int pi,int di, int start, int end) {
        writeSubVectorToResult(addSubVectors(multiplySubVectorByScalar(multiplyVectorBySubMatrix(X, MD, start, end), pi, start, end), multiplySubVectorByScalar(E, ai*di, start, end), start, end), start, end);
    }

    public static void writeSubVectorToResult(int[] G, int start, int end) {
        if (end - start >= 0) System.arraycopy(G, start, A, start, end - start);
    }

    static int[] multiplySubVectorByScalar(int[] X, int x, int start, int end) {
        int[] result = new int[X.length];
        for (int i = start; i < end; i++) {
            result[i] = X[i] * x;
        }
        return result;
    }

    static int[] addSubVectors(int[] X, int[] Y, int start, int end) {
        int[] result = new int[X.length];
        for (int i = start; i < end; i++) {
            result[i] = X[i] + Y[i];
        }
        return result;
    }

    static int scalarProductPart(int[] X, int[] Y, int start, int end) {
        int result = 0;
        for (int i = start; i < end; i++) {
            result += X[i] * Y[i];
        }
        return result;
    }

    static int[] multiplyVectorBySubMatrix(int[] vec, int[][] ma, int start, int end) {
        int[] res = new int[N];
        for (int i = start; i < end; i++) {
            for (int j = 0; j < N; j++) {
                res[i] += vec[j] * ma[j][i];
            }
        }
        return res;
    }

    // Xh = R * MCh
    static void calculation3(int start, int end){
        int[] res = multiplyVectorBySubMatrix(R, MC, start, end);
        System.arraycopy(res, start, X, start, H);
    }

    public static void printVector(int[] X) throws InterruptedException {
        System.out.println(Arrays.toString(X));
    }
}
