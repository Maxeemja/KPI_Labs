package lab0;

import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class Data {

    private static final Random random = new Random();
    private static final Boolean r = false;
    private static final int N = Lab0.N;


    // блок технічних ф-цій
    public static int[] initVector(String name) {
        Scanner sc = new Scanner(System.in);
        int[] result = new int[N];
        if (N < 5) {
            for (int i = 0; i < N; i++) {
                System.out.println(name + "[" + i + "] = ");
                result[i] = sc.nextInt();
            }
        } else {
            if (r) {
                for (int i = 0; i < N; i++)
                    result[i] = random.nextInt(10) + 1;
            } else {
                for (int i = 0; i < N; i++)
                    result[i] = 1;
            }
        }
        return result;
    }

    public static int[][] initMatrix(String name) {
        Scanner sc = new Scanner(System.in);
        int[][] result = new int[N][N];
        if (N < 5) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    System.out.println(name + "[" + i + "]" + "[" + j + "] = ");
                    result[i][j] = sc.nextInt();
                }
            }
        } else {
            if (r) {
                for (int i = 0; i < N; i++) {
                    for (int j = 0; j < N; j++) {
                        result[i][j] = random.nextInt(10) + 1;
                    }
                }
            } else {
                for (int i = 0; i < N; i++)
                    for (int j = 0; j < N; j++)
                        result[i][j] = 1;
            }
        }

        return result;
    }

    public static void printMatrix(int[][] matrix) {
        for (int[] ints : matrix) {
            for (int anInt : ints) {
                System.out.print(anInt + " ");
            }
            System.out.println();
        }
    }

    public static int[][] sortMatrix(int[][] matrix) {
        for (int[] row : matrix) {
            Arrays.sort(row);
        }
        return matrix;
    }


    // блок функцій для обчислення завдання за варіантами
    // * F1 - 1.18 d = (A*B) + (C*(B*(MA*MD)))
    public static int[] f1(int[] a, int[] b, int[] c, int[][] ma, int[][] md) {
        return sumV(multiplyV(a, b), (multiplyV(c, (multiplyVecM(b, multiplyM(ma, md))))));
    }

    //* F2 - 2.24 MG = SORT(MF - MH * MK)
    public static int[][] f2(int[][] mf, int[][] mh, int[][] mk) {
        return  sortMatrix(differenceM(mf, multiplyM(mh, mk)));
    }

    // * F3 - 3.23 s = MAX((MO*MP)(R + V))
    public static int f3(int[] r, int[] v, int[][] mo, int[][] mp) {
        return maxVector(multiplyVecM(sumV(r, v), multiplyM(mo, mp)));
    }


    // блок допоміжних функцій-обчислювальників
    private static int maxVector(int[] A) {
        int r = A[0];
        for (int i = 1; i < N; i++) {
            if (A[i] > r) {
                r = A[i];
            }
        }
        return r;
    }

    private static int[] sumV(int[] a, int[] b) {
        int[] c = new int[N];
        for (int i = 0; i < N; i++) {
            c[i] = a[i] + b[i];
        }
        return c;
    }

    private static int[][] differenceM(int[][] ma, int[][] mb) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                ma[i][j] = ma[i][j] - mb[j][i];
            }
        }
        return ma;
    }

    private static int[] multiplyVecM(int[] a, int[][] ma) {
        int[] c = new int[N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                c[i] += a[j] * ma[j][i];
            }
        }
        return c;
    }

    private static int[] multiplyV(int[] a, int[] b) {
        int[] c = new int[N];
        for (int i = 0; i < N; i++) {
            c[i] = a[i] * b[i];
        }
        return c;
    }

    private static int[][] multiplyM(int[][] ma, int[][] mb) {
        int[][] c = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < N; k++) {
                    c[i][j] += ma[i][k] * mb[k][j];
                }
            }
        }
        return c;
    }


}
