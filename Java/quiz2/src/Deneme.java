import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Deneme {
    public static void main(String[] args) {
        
        // dosya açma
        File file = new File("girdiQuiz1.txt");

        try{
            // input olarak dosyayı scanner ile alıyorum
            Scanner scanner = new Scanner(new FileInputStream(file));
            
            while (scanner.hasNextLine()) {
                
                // satırları okuyorum
                String line = scanner.nextLine().trim();
                
                // input "Default" ise parametresiz employee sınıfı
                if (line.equals("Default")) {
                    Employee employee = new Employee();
                    System.out.println(employee);
                    
                // "Default" değilse StringTokenizer ile ","leri ayırarak inputları uygun olan değişkenlere atıyoruz ve parametreli employee sınıfını kullanıyorum
                } else {
                    StringTokenizer tokenizer = new StringTokenizer(line, ",");
                    String adSoyad = tokenizer.nextToken().trim();
                    int kurumSicilNo = Integer.parseInt(tokenizer.nextToken().trim());
                    String departman = tokenizer.nextToken().trim();
                    String pozisyon = tokenizer.nextToken().trim();
                    Employee employee = new Employee(adSoyad, kurumSicilNo, departman, pozisyon);
                    System.out.println(employee);
                }
            }
        } catch (IOException e) {
        }
    }
}
