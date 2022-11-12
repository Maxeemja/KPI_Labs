package lab3;

public class T2 extends Thread {
    private final InputOutputMonitor inputOutputMonitor;
    private final SyncMonitor1 syncMonitor1;
    private final SyncMonitor3 syncMonitor3;
    private final SyncMonitor4 syncMonitor4;
    private final ResourceMonitor resourceMonitor;

    public T2(InputOutputMonitor inputOutputMonitor,
              SyncMonitor1 syncMonitor1,
              SyncMonitor3 syncMonitor3,
              SyncMonitor4 syncMonitor4,
              ResourceMonitor resourceMonitor) {
        this.inputOutputMonitor = inputOutputMonitor;
        this.syncMonitor1 = syncMonitor1;
        this.syncMonitor3 = syncMonitor3;
        this.syncMonitor4 = syncMonitor4;
        this.resourceMonitor = resourceMonitor;
    }

    @Override
    public void run() {
        int id = 2;
        int r2;
        int d2;
        System.out.println("T2 has started");
        // Уведення е, В, МХ
        int[] B = new int[Data.N];
        int[][] MX = new int[Data.N][Data.N];
        for (int i = 0; i < Data.N; i++) {
            B[i] = 1;
        }
        for (int i = 0; i < Data.N; i++) {
            for (int j = 0; j < Data.N; j++) {
                MX[i][j] = 1;
            }
        }
        resourceMonitor.set_e(1);
        resourceMonitor.setB(B);
        resourceMonitor.setMX(MX);
        // Сигнал задачі T1, T3, T4 про введення e, B, MX
        inputOutputMonitor.InputSignal();
        // Чекати на введення Z, d, MM в T1, T4
        inputOutputMonitor.WaitForInputSignal();

        // Обчислення 1
        r2 = resourceMonitor.maxBPart(id);
        // Обчислення 2
        resourceMonitor.compare_r(r2);
        // Копія d2 = d
        d2 = resourceMonitor.copy_d();
        // Обчислення 3
        resourceMonitor.calculateAndSortXPart(d2, id);
        // Чекати на закінчення обчислень r, Xh в T1
        syncMonitor1.WaitForSortT1();
        // Обчислення 4
        resourceMonitor.mergeXParts(1);
        // Чекати на закінчення обчислень X2h в T4
        syncMonitor3.WaitForMergeT4();
        // Обчислення 5
        resourceMonitor.calculateX();
        // Сигнал Т1, T3, T4 про завершення обчислень X
        syncMonitor4.MergeEndT2Signal();
        // Копія r2 = r
        r2 = resourceMonitor.copy_r();
        // Обчислення 6
        resourceMonitor.calculateResultPart(r2, id);
        // Сигнал Т4 про завершення обчислень Ah
        inputOutputMonitor.OutputSignal();
        System.out.println("T2 has finished");
    }
}
