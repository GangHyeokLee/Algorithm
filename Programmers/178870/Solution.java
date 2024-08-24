import java.util.Arrays;

class Solution {
    public int[] solution(int[] sequence, int k) {
        int[] answer = {0, sequence.length};

        int start = 0;
        int end = 1;
        int sum = sequence[start];

        while (end <= sequence.length) {
            if (sum < k) {
                if(end < sequence.length) sum += sequence[end++];
                else break;
            } else if (sum > k) {
                sum -= sequence[start++];
            } else if(sum == k) {
                if(answer[1] - answer[0] > end - start - 1){
                    answer = new int[]{start, end - 1};
                }
                else if (answer[1] - answer[0] == end - start - 1 && answer[0] > start) {
                    answer = new int[]{start, end - 1};
                }
                sum -= sequence[start++];
            }
        }

        return answer;
    }
}