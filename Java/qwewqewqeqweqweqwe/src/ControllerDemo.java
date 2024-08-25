import java.util.Scanner;

public class ControllerDemo {
    public static void main(String[] args) {
        try {
            NumberController controller = new NumberController("Numbers.txt");

            Scanner scanner = new Scanner(System.in);

            System.out.print("Enter a number to search using binary search: ");
            int num1 = scanner.nextInt();
            boolean found1 = controller.searchBinary(num1);
            if (found1) {
                System.out.println(num1 + " is found in the array.");
            } else {
                System.out.println(num1 + " is not found in the array.");
            }

            System.out.print("Enter a number to search using sequential search: ");
            int num2 = scanner.nextInt();
            boolean found2 = controller.searchSequential(num2);
            if (found2) {
                System.out.println(num2 + " is found in the array.");
            } else {
                System.out.println(num2 + " is not found in the array.");
            }

            scanner.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}