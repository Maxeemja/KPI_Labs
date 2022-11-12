package lab3;

public class ResourceMonitor {
    private static final int N = Data.N;
    private int[] B = new int[N];
    private int[][] MX = new int[N][N];
    private int[][] MM = new int[N][N];
    private int[] Z = new int[N];
    private int e = 0;
    private int d = 0;
    private int[] X = new int[N];
    private int r = 0;
    private final int[] A = new int[N];

    public synchronized void setB(int[] B) {
        this.B = B;
    }

    public synchronized void setMX(int[][] MX) {
        this.MX = MX;
    }

    public synchronized void setMM(int[][] MM) {
        this.MM = MM;
    }

    public synchronized void setZ(int[] Z) {
        this.Z = Z;
    }

    public synchronized void set_d(int d) {
        this.d = d;
    }

    public synchronized void set_e(int e) {
        this.e = e;
    }

    public synchronized int copy_r() {
        return r;
    }

    public synchronized int copy_d() {
        return d;
    }

    public void calculateAndSortXPart(int d, int i) {
        Data.sort(
                Data.sumVectors(
                        Data.multiplyScalarAndSubVector(d, B, i),
                        Data.multiplyVectorAndMatrix(
                                Z,
                                Data.multiplyMatrixAndSubMatrix(MM, MX, i)
                        )
                ),
                i
        );
    }

    public void mergeXParts(int i) {
        Data.merge(i);
    }

    public void calculateX() {
        X = Data.calculateX();
    }

    public int maxBPart(int i) {
        return Data.max(B, i);
    }

    private boolean first = false;

    public void compare_r(int r) {
        if (first) {
            if (r < this.r) {
                this.r = r;
            }
        } else {
            this.r = r;
            first = true;
        }
    }

    public void calculateResultPart(int ri, int id) {
        int[] temp = Data.multiplyScalarAndVector(e, X);
        int[] temp1 = Data.multiplyScalarAndSubVector(ri, Z, id);
        int[] temp2 = Data.sumVectors(temp, temp1);
        int start = Data.H * (id - 1);
        for (int i = 0; i < Data.H; i++) {
            A[start++] = temp2[i];
        }
    }

    public synchronized int[] getA() {
        return A;
    }

}
