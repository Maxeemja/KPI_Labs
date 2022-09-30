import java.util.Scanner;

public class Lab1 {
    static final int C = 0;
    // 0210
    // за варіантом константа С=0 , операція О1 "+" , О2 "*"


    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Введіть a,b,n,m: ");
        final int a = input.nextInt();
        final int b = input.nextInt();
        final int n = input.nextInt();
        final int m = input.nextInt();
        input.close();
        int S = 0;
        // TODO:  negative integer  input possibility (?)
        if (a == 0) {
            System.out.println("Ділення на нуль неможливе");
        } else {
            if (a > n || b > m) {
                System.out.println("S дорівнює 0");
            } else {
                for (int i = a; i <= n; i++) {
                    for (int j = b; j <= m; j++) {
                        //delta; сума арифметичної прогресії
                        // upd: тут не дуже доречна арифм прогресія оскільки j змінюється

                        S += j;
                    }
                }
                System.out.println("S дорівнює : " + S);
            }
        }
    }


}
