package lab3;

public class SyncMonitor4 {
    private int F4 = 0;

    public synchronized void MergeEndT2Signal() {
        F4++;
        if (F4 >= 1) {
            notifyAll();
        }
    }

    public synchronized void WaitForMergeT2() {
        try {
            if (F4 < 1) {
                wait();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
