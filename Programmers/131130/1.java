import java.util.Arrays;

class Solution {
    public int solution(int[] cards) {
        int answer = 0;
        boolean[] visited = new boolean[cards.length + 1];

        for (int start=0;start<cards.length;start++) {
            for (int i = 0; i < cards.length; i++) {
                visited[i + 1] = true;
            }

            int count = dfs(start, cards, visited);
            if (count == cards.length) {
                break;
            }
            for (int i = 0; i < visited.length; i++) {
                if (visited[i]) {
                    boolean[] second = visited.clone();
                    int secondCount = dfs(i, cards, second);
                    answer = Math.max(answer, secondCount * count);
                }
            }
        }

        return answer;
    }

    public int dfs(int start, int[] cards, boolean[] visited) {
        int count = 0;
        while (visited[start]) {
            int next = cards[start];
            visited[start] = false;
            count++;
            start = next;
        }

        return count;
    }
}