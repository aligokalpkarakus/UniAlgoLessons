import java.util.Scanner;
public class Ornek2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int not, kod;
        do{
            System.out.print("Sayisal Not Degerinizi Giriniz: ");
            not = scanner.nextInt();
            if(not >= 90 && not < 100){
                System.out.println("AA");
            }
            else if(not >= 80 && not < 89){
                System.out.println("BA");
            }
            else if(not >= 70 && not < 79){
                System.out.println("BB");
            }
            else if(not >= 60 && not < 69){
                System.out.println("CB");
            }
            else if(not >= 50 && not < 59){
                System.out.println("CC");
            }
            else{
                System.out.println("FF");
            }
            System.out.print("Cikis icin 0, devan icin herhangi bir rakam giriniz: ");
            kod = scanner.nextInt();
        }
        while(kod != 0);
        System.exit(0);
        
        
    }
}
