package lab1;

import java.util.concurrent.BrokenBarrierException;

public class T1 extends Thread {
    private int a1;
    private int p1;
    private int d1;

    @Override
    public void run() {
        try {
            System.out.println("T1 has started.");

            //Введення MC, E
            for (int i = 0; i < Data.N; i++) {
                Data.E[i] = 1;
            }

            for (int i = 0; i < Data.N; i++) {
                for (int j = 0; j < Data.N; j++) {
                    Data.MC[i][j] = 1;
                }
            }

            //Сигнал задачі T2, T3, T4 про введення MC, E
            Data.Sem3.release(3);
            //Чекати на введення MD, d в T2
            Data.Sem6.acquire(1);
            //Чекати на введення B, p в T3
            Data.Sem9.acquire(1);
            //Чекати на введення R, Z в T4
            Data.Sem12.acquire(1);
            //Обчислення1 a1 = (BH * ZH)
            a1 = Data.scalarProductPart(Data.B, Data.Z, 0, Data.H);
            //Обчислення2 a = a + a1
            Data.a.addAndGet(a1);
            //Сигнал задачі T2, T3, T4 про завершення обчислень a
            Data.Sem4.release(3);
            //Чекати на завершення обчислень a в T2
            Data.Sem7.acquire(1);
            //Чекати на завершення обчислень a в T3
            Data.Sem10.acquire(1);
            //Чекати на завершення обчислень a в T4
            Data.Sem13.acquire(1);
            // Обчислення3 Хн = R * MCh
            Data.calculation3(0, Data.H);
            //Сигнал задачі T2, T3, T4 про завершення обчислень Хн
            Data.Sem5.release(3);
            //Чекати на завершення обчислень Хн в T2
            Data.Sem8.acquire(1);
            //Чекати на завершення обчислень Хн в T3
            Data.Sem11.acquire(1);
            //Чекати на завершення обчислень Хн в T4
            Data.Sem14.acquire(1);
            //Копія a1 = a
            Data.Sem2.acquire();
                a1 = Data.a.get();
            Data.Sem2.release();
            //Копія p1 = p
            synchronized (Data.Y) {
                p1 = Data.p;
            }
            //Копія d1 = d
            synchronized (Data.W) {
                d1 = Data.d;
            }
            //Обчислення  Ан = X*MDн*p1 + a1*Eн*d1
            Data.calculateResultPart(a1, p1, d1, 0, Data.H);
            //Сигнал задачі T3 про завершення обчислень AH
            Data.Bar1.await();

            System.out.println("T1 has finished.");
        } catch (InterruptedException | BrokenBarrierException e) {
            e.printStackTrace();
        }
    }
}
