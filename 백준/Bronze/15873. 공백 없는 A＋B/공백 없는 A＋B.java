import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int num = scanner.nextInt();

        if(num % 10 == 0) {
            num /= 100;
            System.out.println(10+num);
        }
        else {
            int a = num%10;
            num /= 10;
            if (num == 10)
                System.out.println(10 + a);
            else
                System.out.println(a + num);

        }
    }
}
