package lab1;

import java.util.concurrent.BrokenBarrierException;

public class T2 extends Thread {
    private int a2;
    private int p2;
    private int d2;

    @Override
    public void run() {
        try {
            System.out.println("T2 has started.");

            //Введення MD, d
            for (int i = 0; i < Data.N; i++) {
                for(int j = 0; j < Data.N; j++) {
                    Data.MD[i][j] = 1;
                }
            }

            Data.d = 1;

            //Сигнал задачі T1, T3, T4 про введення MD, d
            Data.Sem6.release(3);
            //Чекати на введення MC, E в T1
            Data.Sem3.acquire(1);
            //Чекати на введення B, p в T3
            Data.Sem9.acquire(1);
            //Чекати на введення R, Z в T4
            Data.Sem12.acquire(1);
            //Обчислення1 a1 = (BH * ZH)
            a2 = Data.scalarProductPart(Data.B, Data.Z, Data.H, Data.H*2);
            //Обчислення2 a = a + a2
            Data.a.addAndGet(a2);
            //Сигнал задачі T1, T3, T4 про завершення обчислень a
            Data.Sem7.release(3);
            //Чекати на завершення обчислень a в T1
            Data.Sem4.acquire(1);
            //Чекати на завершення обчислень a в T3
            Data.Sem10.acquire(1);
            //Чекати на завершення обчислень a в T4
            Data.Sem13.acquire(1);
            // Обчислення3 Хн = R * MCh
            Data.calculation3(Data.H, Data.H*2);
            //Сигнал задачі T1, T3, T4 про завершення обчислень Хн
            Data.Sem8.release(3);
            //Чекати на завершення обчислень Хн в T2
            Data.Sem5.acquire(1);
            //Чекати на завершення обчислень Хн в T3
            Data.Sem11.acquire(1);
            //Чекати на завершення обчислень Хн в T4
            Data.Sem14.acquire(1);
            //Копія a2 = a
            Data.Sem2.acquire();
            a2 = Data.a.get();
            Data.Sem2.release();
            //Копія p2 = p
            synchronized (Data.Y) {
                p2 = Data.p;
            }
            //Копія d2 = d
            synchronized (Data.W) {
                d2 = Data.d;
            }
            //Обчислення  Ан = X*MDн*p2 + a2*Eн*d2
            Data.calculateResultPart(a2, p2, d2, Data.H, Data.H*2);
            //Сигнал задачі T3 про завершення обчислень AH
            Data.Bar1.await();

            System.out.println("T2 has finished.");
        } catch (InterruptedException | BrokenBarrierException e) {
            e.printStackTrace();
        }

    }
}
