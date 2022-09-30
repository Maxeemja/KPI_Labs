import java.util.*;

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
                {6, 1, 3, 4, 5, 1, 7, 1, 4, 1, 3, 4},
                {5, 4, 3, 6, 7, 8},
                {4, 5, 6, 7, 8, 9},
                {7, 6, 8, 5, 9, 10},
                {6, 7, 8, 9, 10, 11, 1, 2},
                {7, 8, 9, 10, 11, 12, 7, 8, 7}
        };

        double[][] C = Arrays.copyOf(B, B.length);

        //перша дія
        for (int i = 0; i < B.length; i++) {
            for (int j = 0; j < B[i].length; j++) {
                C[i][j] = B[i][j] * a;
            }
        }
        System.out.println("Результат першої дії: ");
        for (int i = 0; i < B.length; i++) {
            for (int j = 0; j < B[i].length; j++) {
                System.out.print(C[i][j] + "\t");
            }
            System.out.println(";");
        }
        //друга дія
        double sum = 0;
        for (double[] row : C) {
            double smallestNum = row[0];
            for (double num : row) {
                if(num < smallestNum) {
                    smallestNum = num;
                }
            }
            double finalSmallestNum = smallestNum;
            int count = (int) Arrays.stream(row).filter(el -> el == finalSmallestNum).count();
            sum += (smallestNum * count);
        }
        System.out.println("Результат другої дії: " + (sum));
    }
}