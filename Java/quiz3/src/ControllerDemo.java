
import java.io.IOException;
import java.util.Scanner;

public class ControllerDemo {
    
    public static void main(String[] args) throws IOException {
        
        // scanner objesi ve numbercontroller objesi oluşturuluyor
        NumberController numberController = new NumberController("Numbers.txt");
        Scanner scanner = new Scanner(System.in);
        
        //binary ve sequential search girdileri giriliyor ve dizide olup olmadıkları kontrol edilip feedback veriliyor
        System.out.print("Binary search icin bir sayi giriniz: ");
        int sayi1 = scanner.nextInt();
        scanner.nextLine();
        if(numberController.searchBinary(sayi1) == true){
            System.out.println("Girdiginiz sayi dizide bulunmaktadir.");
        }
        else{
            System.out.println("Girdiginiz sayi dizide bulunmamaktadir.");
        }
        
        System.out.print("Sequential search icin bir sayi giriniz: ");
        int sayi2 = scanner.nextInt();
        scanner.nextLine();
        if(numberController.searchSequential(sayi2) == true){
            System.out.println("Girdiginiz sayi dizide bulunmaktadir.");
        }
        else{
            System.out.println("Girdiginiz sayi dizide bulunmamaktadir.");
        }  
    }
}
