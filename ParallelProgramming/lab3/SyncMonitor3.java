package lab3;

public class SyncMonitor3 {
    private int F3 = 0;
    public synchronized void MergeEndT4Signal() {
        F3++;
        if (F3 >= 1) {
            notify();
        }
    }
    public synchronized void WaitForMergeT4() {
        try {
            if (F3 < 1) {
                wait();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
