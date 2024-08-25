
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Ornek4 {
    public static void main(String[] args) {
        Scanner fileIn = null;
        try{
            fileIn = new Scanner(new FileInputStream("words.txt"));
        }catch(FileNotFoundException e){
            System.out.println("File not found");
            System.exit(0);
        }
        
        String word;
        String longest = "";
        String shortest = "";
        int sayac = 0;
        while(fileIn.hasNext()){
            word = fileIn.next();
            int start,end;
            start = 0;
            end = word.length() - 1;
            
            boolean isPalindrome = true;
            
            while((start < end) && (isPalindrome == true)){
                if(word.charAt(start) != word.charAt(end))
                    isPalindrome = false;
                    
                start++;
                end--;
            }
            if(isPalindrome){
                System.out.println(word);
                sayac++;
                if(word.length() >= longest.length()){
                    longest = word;
                }
                if(shortest.equals(""))
                    shortest = word;
                
                else{
                    if(word.length() < shortest.length())
                        shortest = word;
                    
                }
            }
        }
        System.out.println("En son bulunan en uzun palindrom: " + longest);
        System.out.println("Ilk bulunan en kisa palindrom: " + shortest);
        System.out.println("Toplam palindrom sayisi: " + sayac);
        
        fileIn.close();
    }
}
