package lab3;

public class SyncMonitor2 {
    private int F2 = 0;

    public synchronized void SortEndT3Signal() {
        F2++;
        if (F2 >= 1) {
            notify();
        }
    }

    public synchronized void WaitForSortT3() {
        try {
            if (F2 < 1) {
                wait();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
