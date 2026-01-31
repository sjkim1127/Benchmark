
import java.util.*;
import java.nio.file.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        String content = new String(Files.readAllBytes(Paths.get("../../data/input.txt")));
        String[] words = content.split("\\s+");
        Map<String, Integer> counts = new HashMap<>();
        for (String word : words) {
            if (!word.isEmpty()) {
                counts.put(word, counts.getOrDefault(word, 0) + 1);
            }
        }
        System.out.println("Done");
    }
}
