import java.util.Scanner;
public class Main {
    //0210
    // перша операція множення на константу , друга - знаходження середнього значення елементів матриці


    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Введіть бажану константу: ");
        double a = input.nextDouble();
        input.close(); // закрив сканер
        double[][] B = {
                {1, 2, 3, 4, 5, 6},
                {3, 4, 5, 6, 7, 8},
                {4, 5, 6, 7, 8, 9},
                {5, 6, 7, 8, 9, 10},
                {6, 7, 8, 9, 10, 11},
                {7, 8, 9, 10, 11, 12}
        };
        double[][] C = new double[B.length][B[0].length];

        //перша дія
        for (int i = 0; i < B.length; i++) {
            for (int j = 0; j < B[0].length; j++) {
                C[i][j] = B[i][j] * a;
            }
        }
        System.out.println("Результат першої дії: ");
        for (int i = 0; i < B.length; i++) {
            for (int j = 0; j < B[0].length; j++) {
                System.out.print(C[i][j] + "\t");
            }
            System.out.println();
        }
        //друга дія
        double sum = 0;
        double counterEl = 0;
        for (int i = 0; i < C.length; i++) {
            for (int j = 0; j < C[0].length; j++) {
                sum += C[i][j];
                counterEl++;
            }
        }
        System.out.println("Результат другої дії: " + (sum/counterEl));
    }
}