package lab3;

/**
 * Паралельне програмування
 * Лабораторна робота No3
 * Варіант 12
 * Завдання: A = sort(d*B + Z*(MM*MX))*e +max(B)*Z
 * • ПВВ1 – d, MM
 * • ПВВ2 – e, B, MX
 * • ПВВ4 – A, Z
 * Грицюк Максим ІО-02
 * Дата 12.11.2022
 **/
public class Lab3 {
    public static void main(String[] args) {
        System.out.println("Lab3 has started");
        System.out.print("N = " + Data.N + "\n");
        InputOutputMonitor inputOutputMonitor = new InputOutputMonitor();
        SyncMonitor1 syncMonitor1 = new SyncMonitor1();
        SyncMonitor2 syncMonitor2 = new SyncMonitor2();
        SyncMonitor3 syncMonitor3 = new SyncMonitor3();
        SyncMonitor4 syncMonitor4 = new SyncMonitor4();
        ResourceMonitor resourceMonitor = new ResourceMonitor();
        // створення потоків
        T1 t1 = new T1(inputOutputMonitor, syncMonitor1, syncMonitor4, resourceMonitor);
        T2 t2 = new T2(inputOutputMonitor, syncMonitor1, syncMonitor3, syncMonitor4, resourceMonitor);
        T3 t3 = new T3(inputOutputMonitor, syncMonitor2, syncMonitor4, resourceMonitor);
        T4 t4 = new T4(inputOutputMonitor, syncMonitor2, syncMonitor3, syncMonitor4, resourceMonitor);
        // запуск потоків
        t3.start();
        t4.start();
        t1.start();
        t2.start();
        // закінчити потоки, а потім головний потік
        try {
            t1.join();
            t2.join();
            t3.join();
            t4.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("Lab3 has finished");
    }


}
