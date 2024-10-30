import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        scanner.nextLine();

        ArrayList<ArrayList<Integer>> friend = new ArrayList<>(n+1);
        for(int i=0;i<=n;i++){
            friend.add(new ArrayList<>());
        }

        while(true){
            String[] line = scanner.nextLine().trim().split(" ");

            int a= Integer.parseInt(line[0]);
            int b= Integer.parseInt(line[1]);

            if(a == -1 && b == -1){
                break;
            }
            friend.get(a).add(b);
            friend.get(b).add(a);
        }

        int[] score = new int[n+1];
        for(int i=0;i<n+1;i++){
            score[i] = 100;
        }

        for(int i=1;i<n+1;i++){
            ArrayList<int[]> que = new ArrayList<>();
            que.add(new int[]{i,0});
            int idx = 0;
            boolean[] visited = new boolean[n+1];
            for(int v=0;v<=n;v++){
                visited[v] = true;
            }
            visited[i] = false;

            while(idx < que.size()){
                int[] now = que.get(idx++);
                ArrayList<Integer> next = friend.get(now[0]);
                for(Integer ne : next){
                    if(visited[ne]){
                        visited[ne] = false;
                        que.add(new int[]{ne, now[1] + 1});
                    }
                }
            }

            int s = 0;
            for(int[] q:que){
                if(s < q[1]){
                    s = q[1];
                }
            }

            score[i] = s;
        }

        int ans = Arrays.stream(score).min().getAsInt();
        int count = 0;
        ArrayList<Integer> candi = new ArrayList<>();
        for(int i=1;i<=n;i++){
            if(score[i] == ans){
                count++;
                candi.add(i);
            }
        }

        System.out.printf("%d %d\n",ans, count);
        String answer = "";
        for(int c : candi){
            answer += c + " ";
        }
        System.out.println(answer);

        scanner.close();
    }
}