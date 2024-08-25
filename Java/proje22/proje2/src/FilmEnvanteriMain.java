
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class FilmEnvanteriMain {
    
    public static void main(String[] args) throws InterruptedException {
        
        // scanner ve cift bagli dugum listesi objeleri oluşturuldu
        DoublyLinkedList doublyLinkedList = new DoublyLinkedList();
        
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Dosya Okunuyor...");
        Thread.sleep(1000);
        
        //dosya okunuyor
        try {
            File file = new File("bilgiler.txt");
            Scanner reader = new Scanner(file);

            String satir;
            while (reader.hasNextLine()) {
                satir = reader.nextLine();

                if (satir.startsWith("{")) { // Satırın başlangıcını kontrol eder
                    satir = satir.substring(1); // İlk parantezi atlar
                }

                if (satir.endsWith("}")) { // Satırın sonunu kontrol eder
                    satir = satir.substring(0, satir.length() - 1); // Son parantezi atlar
                }

                String[] parts = satir.split(",", 5);

                int year = Integer.parseInt(parts[0]);
                String title = parts[1].trim();
                String genre = parts[2].trim();
                String director = parts[3].trim();

                String actorsString = parts[4].trim();
                actorsString = actorsString.substring(1, actorsString.length() - 1); // Aktörlerin parantezlerini atlar

                String[] actorsParts = actorsString.split("\\)");

                ArrayList<Actor> actors = new ArrayList<>();
                for (String actorPart : actorsParts) {
                    String actorData = actorPart.trim();
                    actorData = actorData.substring(1); // İlk parantezi atlar

                    String[] actorInfo = actorData.split(",");

                    String actorName = actorInfo[0].trim();
                    String gender = actorInfo[1].trim();
                    String nationality = actorInfo[2].trim();

                    Actor actor = new Actor(actorName, gender, nationality);
                    actors.add(actor);
                }

                Movie movie = new Movie(year, title, genre, director, actors);
                doublyLinkedList.filmEkleme(movie);
            }

            System.out.println("Dosya Basariyla Okundu...");
            
        } catch (FileNotFoundException e) {
            System.out.println("Dosya bulunamadı: " + e.getMessage());
        }

        System.out.println("Liste Olusturuldu...\n");
        
        Thread.sleep(1000);
        
        //menu
        System.out.println("************FILM ENVANTERI************");
        System.out.println("""
                           Islemler:
                           1 - Film Ekleme
                           2 - Film Arama
                           3 - Film Silme
                           4 - Listeyi Bastan Sona Yazdirma
                           5 - Listeyi Sondan Basa Yazdirma
                           6 - Yapim Yili 2000'den Once Olan Filmler
                           7 - Kayit ve Cikis
                           """);
        
        
        boolean bitis = true;
        
        //istenilen metodlarla menu isleyisi gerceklestirildi
        while(bitis){
            boolean giris3 = false;
            
            int secim = 0;
            System.out.print("\nIslem Numarasi Giriniz: ");        
                while (!giris3) {

                    if (scanner.hasNextInt()) {
                        secim = scanner.nextInt();
                        giris3 = true;
                    } 
                    else {
                        System.out.print("Hatali Giris. Lutfen Integer Bir Deger Giriniz: ");
                        scanner.next();
                    }
                }
            

            System.out.println("");
            
            switch (secim) {
                
            case 1:

                boolean giris1 = false;
                boolean giris2 = false;
  
                System.out.print("Film Yapim Yilini Giriniz: ");
                
                int year = 0;
                while (!giris1) {

                    if (scanner.hasNextInt()) {
                        year = scanner.nextInt();
                        giris1 = true;
                    } 
                    else {
                        System.out.print("Hatali Giris. Lutfen Integer Bir Deger Giriniz: ");
                        scanner.next();
                    }
                }
                scanner.nextLine();
                System.out.print("Film Adini Giriniz: ");
                String title = scanner.nextLine();

                System.out.print("Film Turunu Giriniz: ");
                String category = scanner.nextLine();
                
                System.out.print("Yonetmenin Adini Ve Soyadini Giriniz: ");
                String director = scanner.nextLine();
                
                ArrayList<Actor> actors = new ArrayList<>();
                
                System.out.print("Kac Tane Aktor Girilecek: ");
                int sayi = 0;
                
                while(!giris2){
                    if(scanner.hasNextInt()){
                        sayi = scanner.nextInt();
                        scanner.nextLine();
                        for (int i = 0; i < sayi; i++) {
                            
                            System.out.print((i+1) + ". Aktorun Adini Ve Soyadini Giriniz: ");
                            String fullName = scanner.nextLine();
                            //scanner.nextLine();

                            System.out.print((i+1) + ". Aktorun Cinsiyetini Giriniz: ");
                            String gender = scanner.nextLine();

                            System.out.print((i+1) + ". Aktorun Ulkesini Giriniz: ");
                            String nationality = scanner.nextLine();

                            Actor actor = new Actor(fullName, gender, nationality);
                            actors.add(actor);
                        }
                        giris2 = true;
                    }
                    else{
                        System.out.print("Hatali Giris. Lutfen Integer Bir Deger Giriniz: ");
                        scanner.next();
                    }
                    
                }
                
                
                Movie movie = new Movie(year, title, category, director, actors);
                doublyLinkedList.filmEkleme(movie);
                
                break;

                
            case 2:
                scanner.nextLine();
                System.out.print("Bilgilerini Istediginiz Filmi Giriniz: ");
                String title1 = scanner.nextLine();
                doublyLinkedList.filmBilgileri(title1);

                break;
                
            case 3:
                scanner.nextLine();
                System.out.print("Hangi Filmin Silinmesini Istiyorsunuz: ");
                String title2 = scanner.nextLine();
                doublyLinkedList.filmSilme(title2);
                
                break;
                
            case 4:
                System.out.println("Listenin Bastan Sona Gosterimi:");
                System.out.println("***********************");
                doublyLinkedList.bastanSona();
                
                break;
                
            case 5:
                System.out.println("Listenin Sondan Basa Gosterimi:");
                System.out.println("***********************");
                doublyLinkedList.sondanBasa();
                break;
                
            case 6:
                
                System.out.println("2000 Yilindan Onceki Filmler:");
                System.out.println("***********************");
                doublyLinkedList.ikiBindenOnce();
                break;
                
            case 7:
                
                doublyLinkedList.dosyayaKaydetme();
                Thread.sleep(1000);
                System.out.println("Cikis Yapiliyor...");
                Thread.sleep(1000);
                bitis = false;
                break;   
                
            default:
                System.out.println("Hatali Giris. Lutfen 1-7 Sayılarını Kullaniniz...");
        }
        }         
    }
   
}