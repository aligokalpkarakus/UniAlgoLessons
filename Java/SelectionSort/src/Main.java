
import java.security.SecureRandom;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        
        SecureRandom sr = new SecureRandom();

        int[] array = new int[10];
        
        for(int i = 0; i < array.length; i++){
            array[i] = 10 + sr.nextInt(90);
        }

        System.out.printf("Unsorted Array:\n%s\n\n", Arrays.toString(array));
        
        SelectionSort.sort(array);
        
        System.out.printf("Sorted Array:\n%s\n\n", Arrays.toString(array));
    }
}
