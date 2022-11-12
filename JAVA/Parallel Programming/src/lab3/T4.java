package lab3;

import java.util.Arrays;

public class T4 extends Thread {
    private final InputOutputMonitor inputOutputMonitor;
    private final SyncMonitor2 syncMonitor2;
    private final SyncMonitor3 syncMonitor3;
    private final SyncMonitor4 syncMonitor4;
    private final ResourceMonitor resourceMonitor;

    public T4(InputOutputMonitor inputOutputMonitor,
              SyncMonitor2 syncMonitor2,
              SyncMonitor3 syncMonitor3,
              SyncMonitor4 syncMonitor4,
              ResourceMonitor resourceMonitor) {
        this.inputOutputMonitor = inputOutputMonitor;
        this.syncMonitor2 = syncMonitor2;
        this.syncMonitor3 = syncMonitor3;
        this.syncMonitor4 = syncMonitor4;
        this.resourceMonitor = resourceMonitor;
    }

    @Override
    public void run() {
        int id = 4;
        int r4;
        int d4;
        System.out.println("T4 has started");
        // Уведення Z
        int[] Z = new int[Data.N];
        for (int i = 0; i < Data.N; i++) {
            Z[i] = 1;
        }
        resourceMonitor.setZ(Z);
        // Сигнал задачі T1, T2, T3 про введення Z
        inputOutputMonitor.InputSignal();
        // Чекати на введення d, MM, e, B, MX в T1, T2
        inputOutputMonitor.WaitForInputSignal();
        // Обчислення 1
        r4 = resourceMonitor.maxBPart(id);
        // Обчислення 2
        resourceMonitor.compare_r(r4);
        // Копія d4 = d
        d4 = resourceMonitor.copy_d();
        // Обчислення 3
        resourceMonitor.calculateAndSortXPart(d4, id);
        // Чекати на закінчення обчислень r, Xh в T3
        syncMonitor2.WaitForSortT3();
        // Обчислення 4
        resourceMonitor.mergeXParts(2);
        // Сигнал задачі T2 про закінчення обчислень X2h
        syncMonitor3.MergeEndT4Signal();
        // Чекати на закінчення обчислень X в T2
        syncMonitor4.WaitForMergeT2();
        // Копія r4 = r
        r4 = resourceMonitor.copy_r();
        // Обчислення 5
        resourceMonitor.calculateResultPart(r4, id);
        // Чекати на завершення обчислень Ah в T1,T2,T3
        inputOutputMonitor.WaitForOutputSignal();
        // Вивід A
        System.out.println(Arrays.toString(resourceMonitor.getA()));
        System.out.println("T4 has finished");
    }
}
