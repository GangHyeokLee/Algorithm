class Solution {
    public int solution(int n, int[] tops) {
        int[] dp = new int[2 * n + 1];
        int[] upper = new int[2 * n + 1];

        for (int i = 0; i < 2 * n + 1; i++) {
            dp[i] = 0;
            upper[i] = 0;
        }

        for (int i = 0; i < tops.length; i++) {
            if (tops[i] == 1) {
                upper[2 * (i + 1) - 1] = 1;
            }
        }

        dp[0] = 1;
        dp[1] = upper[1] == 1 ? 3 : 2;

        for (int i = 2; i < 2 * n + 1; i++) {
            dp[i] = (dp[i - 1] + dp[i - 2] + (upper[i] == 1 ? dp[i - 1] : 0)) % 10007;
        }

        return dp[2 * n] % 10007;
    }
}