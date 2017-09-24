import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

public class CreativityScore {
    public static int[] totalScore(int[][] record){
        // key is the number of manager, value is the list of employees
        List<List<Integer>> list = new ArrayList<>();
        int ceo_index = -1;
        for(int i = 0; i < record.length; i++){
            list.add(new ArrayList<Integer>());
        }
        for(int i = 0; i < record.length; i++){
            if(record[i][1] == -1){
                ceo_index = i;
                continue;
            }
            list.get(record[i][1]).add(i);
        }

        Queue<Integer> queue = new LinkedList<>();
        queue.offer(ceo_index);

        while(!queue.isEmpty()){
            int cur = queue.poll();
            // System.out.println(cur);
            int cur_score = record[cur][0];

            for(int i = 0; i < list.get(cur).size(); i++){
                int employee = list.get(cur).get(i);
                record[employee][0] = Math.min(cur_score, record[employee][0]);
                queue.offer(employee);
            }
        }
        int[] result = new int[record.length];
        // System.out.println(record.length);
        for(int i = 0; i < record.length; i++){
            result[i] = record[i][0];
            System.out.println(result[i]);
        }
        return result;
    }

    public static void main(String[] args) {
        // TODO Auto-generated method stub


        Scanner scan = new Scanner(System.in);
        int size = scan.nextInt();
        int[][] a = new int[size][2];
        // {{6,1},{5,2},{5,3},{4,4},{5,-1}};
        for(int i = 0; i < a.length; i++){
            a[i][0] = scan.nextInt();
            a[i][1] = scan.nextInt();
        }
        scan.close();
        totalScore(a);
        // System.out.println(a[0][1]);


    }

}
