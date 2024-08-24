import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int length = scanner.nextInt();
        ArrayList<Integer> nums = new ArrayList<>();

        for (int i = 0; i < length; i++) {
            nums.add(scanner.nextInt());
        }

        int[] next = new int[length];

        Arrays.fill(next, 1);

        for (int i = 0; i < length; i++) {
            for (int j = i + 1; j < length; j++) {
                if (nums.get(i) < nums.get(j)) {
                    next[j] = Math.max(next[i] + 1, next[j]);
                }
            }
        }

        System.out.println(Arrays.stream(next).max().getAsInt());
        scanner.close();
    }
}