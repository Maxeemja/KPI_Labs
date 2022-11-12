package lab3;

import java.util.Arrays;

public class Data {
    public static final int N = 8;
    public static final int P = 4;
    public static int H = N / P;
    public static int[] X1 = new int[H];
    public static int[] X2 = new int[H];
    public static int[] X3 = new int[H];
    public static int[] X4 = new int[H];
    public static int[] X22 = new int[H * 2];
    public static int[] X24 = new int[H * 2];

    public static void sort(int[] X, int i) {
        Arrays.sort(X);
        if (i == 1) {
            X1 = X;
        } else if (i == 2) {
            X2 = X;
        } else if (i == 3) {
            X3 = X;
        } else if (i == 4) {
            X4 = X;
        }
    }

    public static int[] sumVectors(int[] X, int[] Y) {
        int[] result = new int[H];
        for (int i = 0; i < result.length; i++) {
            result[i] = X[i] + Y[i];
        }
        return result;
    }

    public static int[] multiplyScalarAndVector(int d, int[] B) {
        int[] result = new int[H];
        for (int i = 0; i < result.length; i++) {
            result[i] = d * B[i];
        }
        return result;
    }


    public static int[] multiplyScalarAndSubVector(int d, int[] B, int id) {
        int[] result = new int[H];
        int start = (id - 1) * H;
        for (int i = 0; i < result.length; i++) {
            result[i] = d * B[start];
            start++;
        }
        return result;
    }

    public static int[] multiplyVectorAndMatrix(int[] Z, int[][] MY) {
        int cL = MY.length;
        int rL = MY[0].length;
        int[] Y = new int[rL];
        for (int i = 0; i < rL; i++) {
            Y[i] = 0;
            for (int j = 0; j < cL; j++) {
                Y[i] += Z[j] * MY[j][i];
            }
        }
        return Y;
    }

    public static int[][] multiplyMatrixAndSubMatrix(int[][] MX, int[][] MY,
                                                     int id) {
        int start = (id - 1) * H;
        int end = id * H;
        int[][] MT = new int[N][end - start];
        for (int i = 0; i < N; i++) {
            int g = 0;
            for (int j = start; j < end; j++) {
                MT[i][g] = 0;
                for (int k = 0; k < N; k++) {
                    MT[i][g] += MX[i][k] * MY[k][j];
                }
                g++;
            }
        }
        return MT;
    }

    public static void merge(int id) {
        if (id == 1) {
            X22 = mergeArrays(X1, X2, 1);
        } else if (id == 2) {
            X24 = mergeArrays(X3, X4, 1);
        }
    }

    public static int[] calculateX() {
        return mergeArrays(X22, X24, 2);
    }

    private static int[] mergeArrays(int[] a, int[] b, int x) {
        int[] merged = new int[2 * H * x];
        int i = 0, j = 0, k = 0;
        while (i < H * x && j < H * x) {
            if (a[i] < b[j])
                merged[k++] = a[i++];
            else
                merged[k++] = b[j++];
        }
        while (i < H * x)
            merged[k++] = a[i++];
        while (j < H * x)
            merged[k++] = b[j++];
        return merged;
    }

    public static int max(int[] X, int i) {
        int start = (i - 1) * H;
        int end = i * H;
        int max = X[start];
        for (int j = start; j < end; j++) {
            if (X[j] > max) {
                max = X[j];
            }
        }
        return max;
    }
}

