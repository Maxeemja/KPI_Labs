package lab3;

public class T1 extends Thread {

    private final InputOutputMonitor inputOutputMonitor;
    private final SyncMonitor1 syncMonitor1;
    private final SyncMonitor4 syncMonitor4;
    private final ResourceMonitor resourceMonitor;

    public T1(InputOutputMonitor inputOutputMonitor,
              SyncMonitor1 syncMonitor1,
              SyncMonitor4 syncMonitor4,
              ResourceMonitor resourceMonitor) {
        this.inputOutputMonitor = inputOutputMonitor;
        this.syncMonitor1 = syncMonitor1;
        this.syncMonitor4 = syncMonitor4;
        this.resourceMonitor = resourceMonitor;
    }

    @Override
    public void run() {
        int id = 1;
        int r1;
        int d1;
        System.out.println("T1 has started");
        // Уведення d, MM
        int[][] MM = new int[Data.N][Data.N];
        for (int i = 0; i < Data.N; i++) {
            for (int j = 0; j < Data.N; j++) {
                MM[i][j] = 1;
            }
        }
        resourceMonitor.set_d(1);
        resourceMonitor.setMM(MM);
        // Сигнал задачі T1, T2, T3 про введення d, MM
        inputOutputMonitor.InputSignal();
        // Чекати на введення e, B, MX, Z в T2, T4
        inputOutputMonitor.WaitForInputSignal();
        // Обчислення 1
        r1 = resourceMonitor.maxBPart(id);
        // Обчислення 2
        resourceMonitor.compare_r(r1);
        // Копія d1 = d
        d1 = resourceMonitor.copy_d();
        // Обчислення 3
        resourceMonitor.calculateAndSortXPart(d1, id);
        // Сигнал задачі T2 про завершення обчислення r, Xh
        syncMonitor1.SortEndT1Signal();
        // Чекати на закінчення обчислень X в T2
        syncMonitor4.WaitForMergeT2();
        // Копія r1 = r
        r1 = resourceMonitor.copy_r();
        // Обчислення 4
        resourceMonitor.calculateResultPart(r1, id);
        // Сигнал задачі T4 про завершення обчислення Aн
        inputOutputMonitor.OutputSignal();
        System.out.println("T1 has finished");
    }
}
