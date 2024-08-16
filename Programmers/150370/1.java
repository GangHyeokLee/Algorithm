import java.util.*;

class Solution {
    public Integer[] solution(String today, String[] terms, String[] privacies) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        // 약관 map으로 정리
        Map<String, Integer> term = new HashMap<>();
        for(int i=0;i<terms.length;i++){
            String[] tmp = terms[i].split(" ");
            term.put(tmp[0], Integer.parseInt(tmp[1]));
        }
        
        
        // 약관별 날짜 계산 후 오늘 날짜랑 비교하기
        for(int i=0;i<privacies.length;i++){
            String[] tmp = privacies[i].split(" ");
            int year=0,month=0, date=0;
            year = Integer.parseInt(tmp[0].substring(0, 4));
            month = Integer.parseInt(tmp[0].substring(5, 7));
            date = Integer.parseInt(tmp[0].substring(8));
            date += term.get(tmp[1]) * 28 - 1;
            
            month += date / 28;
            date %= 28;
            
            if (date == 0){
                month--;
                date += 28;
            }
            
            year += month/12;
            month %= 12;
            if(month == 0){
                year --;
                month += 12;
            }
            if(today.compareTo(year+"."+((month+"").length()>1?month:("0"+month))+"."+((date+"").length()>1?date:("0"+date)))>0){
                answer.add(i+1);
            }
        }
        
        return answer.toArray(Integer[]::new);
    }
}