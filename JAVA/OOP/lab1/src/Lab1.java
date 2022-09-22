import java.util.Scanner;

public class Lab1 {
    static final int C = 0;
    // 0210
    // за варіантом константа С=0 , операція О1 "+" , О2 "*"


    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Введіть a,b,c,d: ");
        int a = input.nextInt();
        int b = input.nextInt();
        int n = input.nextInt();
        int m = input.nextInt();
        input.close();
        float S = 0;

        if (a == 0) {
            System.out.println("Ділення на нуль неможливе");
        } else {
            if (a > n || b > m) {
                System.out.println("S дорівнює 0");
            } else {
                for (int i = a; i <= n; i++) {
                    for (int j = b; j <= m; j++) {
                        S += (float) (i * j) / (i + C);
                    }
                }
                System.out.println("S дорівнює : " + S);
            }
        }
    }


}
