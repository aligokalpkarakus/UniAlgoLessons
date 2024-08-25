
import java.util.Random;
import java.util.Scanner;

public class quiz1 {
    public static void main(String[] args) {
        Random random = new Random();
        
        Scanner scanner = new Scanner(System.in);
        
        int para = 0;
        int topHarcanan = 0;
        int topKazanilan = 0;
        String meyve = "", meyve1 = "", meyve2 = "", meyve3 = "";
        char devam = 'y';
        
        while(devam == 'y' || devam == 'Y'){
            System.out.print("Bahsi giriniz: ");
            para = scanner.nextInt();
            topHarcanan += para;
            for(int i = 0; i < 3; i++){
                int rakam = random.nextInt(6);
                switch (rakam) {  // meyveyi random sayı vererek seçiyorum
                    case 0:
                      meyve = "Cilek";
                      break;
                    case 1:
                      meyve = "Portakal";
                      break;
                    case 2:
                      meyve = "Elma";
                      break;
                    case 3:
                      meyve = "Muz";
                      break;
                    case 4:
                      meyve = "Kiraz";
                      break;
                    case 5:
                      meyve = "Kavun";
                      break;
                }
                
                if(i == 0){  // meyve isimlerini karşılaştırmak için değişkenlere atama
                    meyve1 = meyve;
                }
                else if(i == 1){
                    meyve2 = meyve;
                }
                else{
                    meyve3 = meyve;
                }
            }
            System.out.println("Meyvveler: " + meyve1 + " " + meyve2 + " " + meyve3);
            
            if(meyve1.equals(meyve2) && meyve1.equals(meyve3)){  // para kazancını kontrol etme
                System.out.println("Tebrikler! Uc kelime de ayni. Bastaki para miktarinin 3 katini kazandiniz.");
                topKazanilan += para * 3;
            }
            else if(meyve1.equals(meyve2) || meyve1.equals(meyve3) || meyve2.equals(meyve3)){
                System.out.println("Tebrikler! Uc kelimeden ikisi ayni. Bastaki para miktarinin 2 katini kazandiniz.");
                topKazanilan += para * 2;
            }
            else{
                System.out.println("Maalesef tum kelimeler farkli. 0 TL kazandiniz.");
            }
            
            System.out.print("Oynamaya devam edecek misiniz (devam icin y-Y, cikis icin bu iki karakterden farkli bir karakter giriniz): "); // devam edecek misiniz diye soru sorma
            devam = scanner.next().charAt(0);
        }
        
        int netKazanc = topKazanilan - topHarcanan;  // sonuçlar
        System.out.println("Harcanan para: " + topHarcanan);
        System.out.println("Kazanilan para: " + topKazanilan);
        System.out.println("Net kazanc: " + netKazanc);
    }
}
