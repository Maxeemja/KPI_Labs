package lab3;

public class SyncMonitor1 {
    private int F1 = 0;

    public synchronized void SortEndT1Signal() {
        F1++;
        if (F1 >= 1) {
            notify();
        }
    }

    public synchronized void WaitForSortT1() {
        try {
            if (F1 < 1) {
                wait();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
