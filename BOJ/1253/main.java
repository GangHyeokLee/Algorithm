import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String line = scanner.nextLine();
        int n = Integer.parseInt(line);

        String[] l = scanner.nextLine().split(" ");

        int[] nums = new int[n];

        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(l[i]);
        }

        nums = Arrays.stream(nums).sorted().toArray();

        ArrayList<Integer> answer = new ArrayList<>();

        for(int x = 0;x<n;x++){
            int i = 0, j = n - 1;
            while (i < j){
                if (i == x){
                    i++;
                }
                else if(j == x){
                    j--;
                }
                else if (nums[i]+nums[j] < nums[x]){
                    i++;
                } else if (nums[i] + nums[j] > nums[x]){
                    j--;
                } else{
                    answer.add(nums[x]);
                    break;
                }
            }
        }

        System.out.println(answer.size());

        scanner.close();

    }
}