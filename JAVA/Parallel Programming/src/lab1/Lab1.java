package lab1;

/**
 * Паралельне програмування
 * Лабораторна робота No1
 * Варіант 6
 * Завдання: A = (R*MC)*MD*p + (B*Z)*E*d
 * • ПВВ1 – MC, E
 * • ПВВ2 – MD, d
 * • ПВВ3 – A, B, p
 * • ПВВ4 – R, Z
 * Грицюк Максим ІО-02
 * Дата 25.10.2022
 **/

public class Lab1 {

    public static void main(String[] args) {
        System.out.println("Lab1 has started.");
        System.out.print("N = " + Data.N + "\n");

        T1 T1 = new T1();
        T2 T2 = new T2();
        T3 T3 = new T3();
        T4 T4 = new T4();

        T1.start();
        T2.start();
        T3.start();
        T4.start();

        try {
            T1.join();
            T2.join();
            T3.join();
            T4.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("Lab1 has finished.");
    }
}

