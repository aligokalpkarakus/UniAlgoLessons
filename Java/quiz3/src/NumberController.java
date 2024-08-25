
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class NumberController {
    
    private int[] sayilar;
    
    public NumberController(String fileName) {
        try {
            // Dosyadan sayıları okuma ve diziye ekleme
            Scanner scanner = new Scanner(new File(fileName));
            
            scanner = new Scanner(new File(fileName));
            sayilar = new int[20];
            for (int i = 0; i < 20; i++) {
                sayilar[i] = scanner.nextInt();
            }
            scanner.close();
            
            // Diziyi bubble sort algoritması ile sıralama
            bubbleSort(sayilar);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
    
    public static void bubbleSort(int[] array) { // bubble sort algoritması
        int n = 20;
        for (int i = 0; i < n-1; i++) {
            for (int j = 0; j < n-i-1; j++) {
                if (array[j] > array[j+1]) {
                    int temp = array[j];
                    array[j] = array[j+1];
                    array[j+1] = temp;
                }
            }
        }
    }
    
    public boolean searchBinary(int sayi) { // binary search algoritması
        int sol = 0, sag = sayilar.length - 1;
        while (sol <= sag) {
            int orta = sol + (sag - sol) / 2;
            if (sayilar[orta] == sayi) {
                return true;
            }
            if (sayilar[orta] < sayi) {
                sol = orta + 1;
            } else {
                sag = orta - 1;
            }
        }
        return false;
    }
    
    public boolean searchSequential(int sayi) { // sequential search algoritması
        for (int i = 0; i < sayilar.length; i++) {
            if (sayilar[i] == sayi) {
                return true;
            }
        }
        return false;
    }
}

