import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        
        int[][] lectures = new int[n][2];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            lectures[i][0] = Integer.parseInt(st.nextToken()); // 시작 시간
            lectures[i][1] = Integer.parseInt(st.nextToken()); // 종료 시간
        }
        
        // 시작 시간을 기준으로 오름차순 정렬, 같으면 종료 시간을 기준으로 정렬
        Arrays.sort(lectures, (a, b) -> a[0] == b[0] ? Integer.compare(a[1], b[1]) : Integer.compare(a[0], b[0]));
        
        // 종료 시간을 관리하는 우선순위 큐 (최소 힙)
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        pq.add(lectures[0][1]); // 첫 강의 종료 시간 추가
        
        for (int i = 1; i < n; i++) {
            // 현재 강의의 시작 시간이 가장 빨리 끝나는 강의보다 늦거나 같다면
            if (lectures[i][0] >= pq.peek()) {
                pq.poll(); // 기존 강의실 사용 가능 (가장 빨리 끝나는 강의 제거)
            }
            pq.add(lectures[i][1]); // 현재 강의 종료 시간 추가
        }
        
        System.out.println(pq.size()); // 우선순위 큐 크기가 필요한 강의실 수
    }
}
