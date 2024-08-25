
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Ornek3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Bir karakter giriniz: ");
        char key = scanner.next().charAt(0);
        
        Scanner fileIn = null;
        
        try{
            fileIn = new Scanner(new FileInputStream("words.txt"));
        }catch(FileNotFoundException e){
            System.out.println("File not found");
            System.exit(0);
        }
        
        String word;
        int sayac = 0;
        
        while(fileIn.hasNext()){
            word = fileIn.next();
            
            if((word.charAt(word.length()-1) == key) && (word.length() == 6)){
                System.out.println("Kelimelerimiz: " + word);
                sayac++;
                
            }
        }
        System.out.println("Toplam sayi: " + sayac);
        fileIn.close();
            
        
        
        
    }
}
