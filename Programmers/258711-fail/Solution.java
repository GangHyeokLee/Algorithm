import java.util.*;

class Solution {
    public int[] solution(int[][] edges) {
        int[] answer = {0, 0, 0, 0};
        
        Set<Integer> nodes = new HashSet<>();
        Map<Integer, ArrayList<Integer>> out = new HashMap<>();
        Map<Integer, ArrayList<Integer>> in = new HashMap<>();
        
        for(int[] e: edges){
            nodes.add(e[0]);
            nodes.add(e[1]);
            
            if(!out.containsKey(e[0])){
                out.put(e[0], new ArrayList<>());
            }
            if(!in.containsKey(e[1])){
                in.put(e[1], new ArrayList<>());
            }
            
            out.get(e[0]).add(e[1]);
            in.get(e[1]).add(e[0]);
        }
        
        int target = 0;
        
        // 새로 만든 노드 찾기
        for(int n: nodes){
            if(out.containsKey(n) && out.get(n).size() >=2 && !in.containsKey(n)){
                target = n;
            }
        }
        
        answer[0] = target;
        
        // 노드 찾았으면 각 그래프 루트 기준으로 탐색하기
        for(int r: out.get(target)){
            answer[graphType(out, in, r)]++;
        }
        
        return answer;
    }
    
    public int graphType(Map<Integer, ArrayList<Integer>> out, Map<Integer, ArrayList<Integer>> in, int root){
        // 도넛: 1, 막대: 2, 8자: 3
        ArrayList<Integer> que = new ArrayList<>();
        que.add(root);
        int idx = 0;
        Set<Integer> visited = new HashSet<>();
        visited.add(root);
        int type = 2;
        
        while(idx < que.size()){
            int now = que.get(idx++);
            
            if(out.containsKey(now) && in.containsKey(now) && out.get(now).size() + in.get(now).size() >= 4){
                return 3;
            }
            
            if(!out.containsKey(now)){
                continue;
            }
            
            for(int next: out.get(now)){
                if(visited.contains(next)){
                    type = 1;
                } else {
                    que.add(next);
                    visited.add(next);
                }
            }
        }
        
        return type;
    }
}