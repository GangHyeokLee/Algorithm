import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] line = scanner.nextLine().split(" ");

        int n = Integer.parseInt(line[0]), m = Integer.parseInt(line[1]);
        line = scanner.nextLine().split(" ");

        ArrayList<Integer> pb = new ArrayList<>();
        ArrayList<Integer> nb = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            if (Integer.parseInt(line[i]) > 0) {
                pb.add(Integer.parseInt(line[i]));
            } else {
                nb.add(-Integer.parseInt(line[i]));
            }
        }

        Collections.sort(pb);
        Collections.sort(nb);

        int ans = 0;
        int[] dp = new int[pb.size()];

        for (int i = 0; i < m; i++) {
            if (i == pb.size()) {
                break;
            }
            dp[i] = pb.get(i);
        }

        for (int i = m; i < dp.length; i++) {
            dp[i] = pb.get(i) + dp[i - m] + pb.get(i - m);
            for (int b = m - 1; b >= 1; b--) {
                dp[i] = Math.min(dp[i], dp[i - b] + pb.get(i - b) + pb.get(i));
            }
        }

        if (dp.length > 0) {
            ans += dp[dp.length - 1];
        }

        dp = new int[nb.size()];
        for (int i = 0; i < m; i++) {
            if (i == nb.size()) {
                break;
            }
            dp[i] = nb.get(i);
        }

        for (int i = m; i < dp.length; i++) {
            dp[i] = nb.get(i) + dp[i - m] + nb.get(i - m);
            for (int b = m - 1; b >= 1; b--) {
                dp[i] = Math.min(dp[i], dp[i - b] + nb.get(i - b) + nb.get(i));
            }
        }

        if (dp.length > 0) {
            ans += dp[dp.length - 1];
        }

        System.out.println(ans + Math.min(!pb.isEmpty() ? pb.get(pb.size() - 1) : 0, !nb.isEmpty() ? nb.get(nb.size() - 1) : 0));

        scanner.close();

    }
}