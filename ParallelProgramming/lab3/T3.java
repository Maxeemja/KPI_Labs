package lab3;

public class T3 extends Thread {
    private final InputOutputMonitor inputOutputMonitor;
    private final SyncMonitor2 syncMonitor2;
    private final SyncMonitor4 syncMonitor4;
    private final ResourceMonitor resourceMonitor;

    public T3(InputOutputMonitor inputOutputMonitor,
              SyncMonitor2 syncMonitor2,
              SyncMonitor4 syncMonitor4,
              ResourceMonitor resourceMonitor) {
        this.inputOutputMonitor = inputOutputMonitor;
        this.syncMonitor2 = syncMonitor2;
        this.syncMonitor4 = syncMonitor4;
        this.resourceMonitor = resourceMonitor;
    }

    @Override
    public void run() {
        int id = 3;
        int r3;
        int d3;
        System.out.println("T3 has started");
        // Чекати на введення d, MM, e, B, MX, Z в T1, T2, T4
        inputOutputMonitor.WaitForInputSignal();
        // Обчислення 1
        r3 = resourceMonitor.maxBPart(id);
        // Обчислення 2
        resourceMonitor.compare_r(r3);
        // Копія d3 = d
        d3 = resourceMonitor.copy_d();
        // Обчислення 3
        resourceMonitor.calculateAndSortXPart(d3, id);
        // Сигнал задачі T4 про завершення обчислення r, Xh
        syncMonitor2.SortEndT3Signal();
        // Чекати на закінчення обчислень X в T2
        syncMonitor4.WaitForMergeT2();
        // Копія r1 = r
        r3 = resourceMonitor.copy_r();
        // Обчислення 4
        resourceMonitor.calculateResultPart(r3, id);
        // Сигнал задачі T4 про завершення обчислення Aн
        inputOutputMonitor.OutputSignal();
        System.out.println("T3 has finished");
    }
}
