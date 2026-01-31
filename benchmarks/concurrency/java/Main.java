
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        int total = 100_000;
        AtomicInteger count = new AtomicInteger(0);
        ExecutorService executor = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors() * 2);

        for (int i = 0; i < total; i++) {
            executor.submit(() -> count.incrementAndGet());
        }

        executor.shutdown();
        executor.awaitTermination(1, TimeUnit.MINUTES);
        System.out.println("Counter: " + count.get());
        System.out.println("Done");
    }
}
