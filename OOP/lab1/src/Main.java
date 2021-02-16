import java.util.Scanner;

public class Main {
    /* static final byte a=4;
     static final byte b=5;
     static final byte n=6;
     static final byte m=7;*/
    static final byte C = 0;
    // 0210
    // за варіантом константа С=0 , операція О1 "+" , О2 "*"


    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Введіть a,b,c,d: ");
        byte a = input.nextByte();
        byte b = input.nextByte();
        byte n = input.nextByte();
        byte m = input.nextByte();
        input.close();
        float S = 0;

        if (a == 0) {
            System.out.println("Ділення на нуль неможливе");
        } else {
            if (a > n || b > m) {
                System.out.println("S дорівнює 0");
            } else {
                for (byte i = a; i <= n; i++) {
                    for (byte j = b; j <= m; j++) {
                        S += (float) (i * j) / (i + C);
                    }
                }
                System.out.println("S дорівнює : " + S);
            }
        }
    }


}
