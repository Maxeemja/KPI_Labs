import java.util.Scanner;
public class Lab2 {
    //0210
    //double
    // перша операція множення на константу(C=a×B, a - const) , друга - (раніше було обчислення середнього значення рядка наскільки пам'ятаю)
    //                                                                  Обчислити суму найменших елементів кожного рядка матриці


    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Введіть бажану константу: ");
        double a = input.nextDouble();
        input.close(); // закрив сканер
        double[][] B = {
            {6, 2, 3, 4, 5, 1},
            {5, 4, 3, 6, 7, 8},
            {4, 5, 6, 7, 8, 9},
            {7, 6, 8, 5, 9, 10},
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
            System.out.println(";");
        }
        //друга дія
        double sum = 0;
        for (double[] row : C) {
            double smallestNum = row[0];
            for (int j = 0; j < C[0].length; j++) {
                if(row[j] < smallestNum) {
                    smallestNum = row[j];
                }
            }
            sum += smallestNum;
        }
        System.out.println("Результат другої дії: " + (sum));
    }
}