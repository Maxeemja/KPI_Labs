package lab1;

import java.util.concurrent.BrokenBarrierException;

public class T4 extends Thread {
    private int a4;
    private int p4;
    private int d4;

    @Override
    public void run() {
        try {
            System.out.println("T4 has started.");

            //Введення R, Z
            for (int i = 0; i < Data.N; i++) {
                Data.R[i] = 1;
                Data.Z[i] = 1;
            }

            //Сигнал задачі T1, T2, T3 про введення R, Z
            Data.Sem12.release(3);
            //Чекати на введення MC, E в T1
            Data.Sem3.acquire(1);
            //Чекати на введення MD, d в T2
            Data.Sem6.acquire(1);
            //Чекати на введення B, p в T3
            Data.Sem9.acquire(1);
            //Обчислення1 a4 = (BH * ZH)
            a4 = Data.scalarProductPart(Data.B, Data.Z, Data.H*3, Data.H*4);
            //Обчислення2 a = a + a4
            Data.a.addAndGet(a4);
            //Сигнал задачі T1, T2, T3 про завершення обчислень a
            Data.Sem13.release(3);
            //Чекати на завершення обчислень a в T1
            Data.Sem4.acquire(1);
            //Чекати на завершення обчислень a в T2
            Data.Sem7.acquire(1);
            //Чекати на завершення обчислень a в T3
            Data.Sem10.acquire(1);
            // Обчислення3 Хн = R * MCh
            Data.calculation3(Data.H*3, Data.H*4);
            //Сигнал задачі T1, T3, T4 про завершення обчислень Хн
            Data.Sem14.release(3);
            //Чекати на завершення обчислень Хн в T1
            Data.Sem5.acquire(1);
            //Чекати на завершення обчислень Хн в T2
            Data.Sem8.acquire(1);
            //Чекати на завершення обчислень Хн в T3
            Data.Sem11.acquire(1);
            //Копія a4 = a
            Data.Sem2.acquire();
                a4 = Data.a.get();
            Data.Sem2.release();
            //Копія p4 = p
            synchronized (Data.Y) {
                p4 = Data.p;
            }
            //Копія d4 = d
            synchronized (Data.W) {
                d4 = Data.d;
            }
            //Обчислення  Ан = X*MDн*p4 + a4*Eн*d4
            Data.calculateResultPart(a4, p4, d4, Data.H*3, Data.H*4);
            //Сигнал задачі T3 про завершення обчислень AH
            Data.Bar1.await();

            System.out.println("T4 has finished.");
        } catch (InterruptedException | BrokenBarrierException e) {
            e.printStackTrace();
        }

    }
}
