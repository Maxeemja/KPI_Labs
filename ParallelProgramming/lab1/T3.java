package lab1;

import java.util.concurrent.BrokenBarrierException;

public class T3 extends Thread {
    private int a3;
    private int p3;
    private int d3;

    @Override
    public void run() {
        try {
            System.out.println("T3 has started.");

            //Введення B, p
            for (int i = 0; i < Data.N; i++) {
                Data.B[i] = 1;
            }

            Data.p = 1;

            //Сигнал задачі T1, T2, T4 про введення B, p
            Data.Sem9.release(3);
            //Чекати на введення MC, E в T1
            Data.Sem3.acquire(1);
            //Чекати на введення B, p в T2
            Data.Sem6.acquire(1);
            //Чекати на введення R, Z в T4
            Data.Sem12.acquire(1);
            //Обчислення1 a3 = (BH * ZH)
            a3 = Data.scalarProductPart(Data.B, Data.Z, Data.H*2, Data.H*3);
            //Обчислення2 a = a + a3
            Data.a.addAndGet(a3);
            //Сигнал задачі T1, T2, T4 про завершення обчислень a
            Data.Sem10.release(3);
            //Чекати на завершення обчислень a в T1
            Data.Sem4.acquire(1);
            //Чекати на завершення обчислень a в T2
            Data.Sem7.acquire(1);
            //Чекати на завершення обчислень a в T4
            Data.Sem13.acquire(1);
            // Обчислення3 Хн = R * MCh
            Data.calculation3(Data.H*2, Data.H*3);
            //Сигнал задачі T1, T3, T4 про завершення обчислень Хн
            Data.Sem11.release(3);
            //Чекати на завершення обчислень Хн в T1
            Data.Sem5.acquire(1);
            //Чекати на завершення обчислень Хн в T2
            Data.Sem8.acquire(1);
            //Чекати на завершення обчислень Хн в T4
            Data.Sem14.acquire(1);
            //Копія a3 = a
            Data.Sem2.acquire();
                a3 = Data.a.get();
            Data.Sem2.release();
            //Копія p3 = p
            synchronized (Data.Y) {
                p3 = Data.p;
            }
            //Копія d3 = d
            synchronized (Data.W) {
                d3 = Data.d;
            }
            //Обчислення  Ан = X*MDн*p3 + a3*Eн*d3
            Data.calculateResultPart(a3, p3, d3, Data.H*2, Data.H*3);
            //Чекати на завершення обчислень AH в T1, T2, T4
            Data.Bar1.await();
            // Виведення А
            Data.printVector(Data.A);

            System.out.println("T3 has finished.");
        } catch (InterruptedException | BrokenBarrierException e) {
            e.printStackTrace();
        }

    }
}
