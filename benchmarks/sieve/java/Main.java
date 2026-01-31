
public class Main {
    public static void main(String[] args) {
        int limit = 10_000_000;
        boolean[] isPrime = new boolean[limit + 1];
        for (int i = 2; i <= limit; i++) isPrime[i] = true;

        int count = 0;
        for (int p = 2; p <= limit; p++) {
            if (isPrime[p]) {
                count++;
                if ((long)p * p <= limit) {
                    for (int i = p * p; i <= limit; i += p)
                        isPrime[i] = false;
                }
            }
        }
        System.out.println("Count: " + count);
    }
}
