import java.util.*;

class Cell implements Comparable<Cell>{
    int cost, y, x;

    public Cell(int cost, int y, int x){
        this.cost = cost;
        this.y = y;
        this.x = x;
    }

    @Override
    public int compareTo(Cell other){
        return Integer.compare(this.cost, other.cost);
    }
}

public class Main { 
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String line = scanner.nextLine();

        int n = Integer.parseInt(line);

        int[] dy = {-1, 1, 0, 0};
        int[] dx = {0, 0, -1, 1};

        int[][] room = new int[n][n];
        int[][] cost = new int[n][n];


        for (int i=0;i<n;i++){
            line = scanner.nextLine().strip();
            for(int j = 0;j<n;j++){
                room[i][j] = line.charAt(j) - '0';
                cost[i][j] = n*n;
            }
        }

        scanner.close();

        cost[0][0] = 0;

        PriorityQueue<Cell>  queue = new PriorityQueue<>();

        queue.add(new Cell(0, 0, 0));

        while(!queue.isEmpty()){
            Cell current = queue.poll();
            int count = current.cost;
            int y = current.y;
            int x = current.x;

            if(cost[y][x] < count){
                continue;
            }

            for(int d=0;d<4;d++){
                int ny = y + dy[d];
                int nx = x + dx[d];

                if(0 <= ny && ny < n && 0 <= nx && nx < n){
                    if(cost[ny][nx] > count + Math.abs(room[ny][nx] - 1) ){
                        cost[ny][nx] = count + Math.abs(room[ny][nx] - 1);
                        queue.add(new Cell(cost[ny][nx], ny, nx));
                    }
                }
            }
        }

        System.out.println(cost[n-1][n-1]);
    }
}