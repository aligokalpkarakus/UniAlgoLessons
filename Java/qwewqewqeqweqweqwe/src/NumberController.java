import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class NumberController {
    private int[] numbers;

    public NumberController(String filename) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(filename));
        String line;

        numbers = new int[count];
        reader = new BufferedReader(new FileReader(filename));
        int i = 0;
        while ((line = reader.readLine()) != null) {
            numbers[i] = Integer.parseInt(line);
            i++;
        }
        reader.close();

        bubbleSort(numbers);
    }

    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n-1; i++) {
            for (int j = 0; j < n-i-1; j++) {
                if (arr[j] > arr[j+1]) {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
    }

    public boolean searchBinary(int num) {
        int left = 0, right = numbers.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (numbers[mid] == num) {
                return true;
            }
            if (numbers[mid] < num) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return false;
    }

    public boolean searchSequential(int num) {
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] == num) {
                return true;
            }
        }
        return false;
    }
}

