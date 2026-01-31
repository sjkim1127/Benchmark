
public class Main {
    public static void main(String[] args) {
        int width = 2048;
        int height = 2048;
        int maxIter = 255;
        int count = 0;

        for (int y = 0; y < height; y++) {
            double cy = -1.5 + (double)y * 2.0 / height;
            for (int x = 0; x < width; x++) {
                double cx = -2.0 + (double)x * 2.5 / width;
                double zr = 0.0, zi = 0.0;
                int iter = 0;
                while (zr * zr + zi * zi <= 4.0 && iter < maxIter) {
                    double tr = zr * zr - zi * zi + cx;
                    zi = 2.0 * zr * zi + cy;
                    zr = tr;
                    iter++;
                }
                if (iter == maxIter) count++;
            }
        }
        System.out.println("Done");
    }
}
