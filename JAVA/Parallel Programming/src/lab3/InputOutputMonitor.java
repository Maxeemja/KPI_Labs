package lab3;

public class InputOutputMonitor {
    private int F1 = 0;
    private int F2 = 0;

    public synchronized void InputSignal() {
        F1++;
        if (F1 >= 3) {
            notifyAll();
        }
    }

    public synchronized void WaitForInputSignal() {
        try {
            if (F1 < 3) {
                wait();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public synchronized void OutputSignal() {
        F2++;
        if (F2 >= 3) {
            notify();
        }
    }

    public synchronized void WaitForOutputSignal() {
        try {
            if (F2 < 3) {
                wait();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
