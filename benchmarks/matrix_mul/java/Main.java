
public class Main {
    public static void main(String[] args) {
        int n = 512;
        double[] a = new double[n * n];
        double[] b = new double[n * n];
        double[] c = new double[n * n];

        for (int i = 0; i < n * n; i++) {
            a[i] = 1.0;
            b[i] = 1.0;
        }

        for (int i = 0; i < n; i++) {
            for (int k = 0; k < n; k++) {
                double r = a[i * n + k];
                for (int j = 0; j < n; j++) {
                    c[i * n + j] += r * b[k * n + j];
                }
            }
        }

        if (c[0] == (double)n) {
            System.out.println("Done");
        } else {
            System.out.println("Fail");
        }
    }
}
