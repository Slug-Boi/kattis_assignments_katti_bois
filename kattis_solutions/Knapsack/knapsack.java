import java.util.*;
import java.io.*;

public class knapsack {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        String line;

        while ((line = br.readLine()) != null) {
            // Read input
            String[] split = line.split(" ");
            int cap = Integer.valueOf(split[0]);
            int n = Integer.valueOf(split[1]);
            Item[] items = new Item[n];
            for (int i = 0; i < n; i++) {
                split = br.readLine().split(" ");
                items[i] = new Item(Integer.valueOf(split[1]), Integer.valueOf(split[0]));
            }
            
            // Find result
            List<Integer> result = knapsack(items, n, cap);
            
            // Print output
            System.out.println(result.size());
            StringJoiner joiner = new StringJoiner(" ");
            for (int index : result) {
                joiner.add(String.valueOf(index));
            }
            System.out.println(joiner.toString());
        }
    }

    static List<Integer> knapsack(Item[] items, int n, int cap) {
        // Create best value matrix
        int[][] bestValue = new int[n+1][cap+1];
        for (int i = 1; i <= n; i++) {
            int itemIndex = i-1;
            for (int j = 0; j <= cap; j++) {
                int totalWeight = j + items[itemIndex].weight;
                int totalValue = bestValue[i - 1][j] + items[itemIndex].value;
                
                if (totalWeight <= cap) {
                    bestValue[i][totalWeight] = Math.max(totalValue, bestValue[i][totalWeight]);
                }

                bestValue[i][j] = Math.max(bestValue[i-1][j], bestValue[i][j]);
            }
        }
        // Find the index of times used
        List<Integer> itemsChosen = new ArrayList<>();
        int column = cap;
        for (int i = n; i > 0; i--) {
            if (bestValue[i][column] != bestValue[i-1][column]) {
                int itemIndex = i - 1;
                itemsChosen.add(itemIndex);
                column -= items[itemIndex].weight;
            }
        }
        return itemsChosen;
    }

    static class Item {
        int weight;
        int value;
        
        public Item (int weight, int value) {
            this.weight = weight;
            this.value = value;
        }
    }
}
