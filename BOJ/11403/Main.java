import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int[][] adj = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                adj[i][j] = scanner.nextInt();
            }
        }

        int[][] ans = new int[n][n];
        for (int i = 0; i < n; i++) {
            ArrayList<Integer> queue = new ArrayList<>();
            queue.add(i);
            int idx = 0;

            boolean[][] visited = new boolean[n][n];

            while(idx < queue.size()){
                int now = queue.get(idx++);

                for(int next = 0;next< n;next++){
                    if(adj[now][next] == 1 && !visited[now][next]){
                        queue.add(next);
                        visited[now][next] = true;
                        ans[i][next] = 1;
                    }
                }
            }
        }

        for(int[] row:ans){
            for(int val:row){
                System.out.print(val + " ");
            }
            System.out.println();
        }

        scanner.close();
    }
}