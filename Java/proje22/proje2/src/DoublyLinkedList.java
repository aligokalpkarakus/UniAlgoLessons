
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class DoublyLinkedList {
    
    //degiskenler
    private Node head;
    private Node tail;
    
    //getter ve setter metodları
    public Node getHead() {
        return head;
    }

    public void setHead(Node head) {
        this.head = head;
    }

    public Node getTail() {
        return tail;
    }

    public void setTail(Node tail) {
        this.tail = tail;
    }
    
    //Film ekleme metodumuz eklenecek film ile ilgili bilgiler girildikten sonra yıl veya alfabetik karşılaştırmaya göre listede uygun yere yerleştiriyor.
    public void filmEkleme(Movie movie) {
        Node eklenen = new Node(movie);

        if (head == null) {
            head = eklenen;
            tail = eklenen;
        } else {
            Node karsilastirilan = head;

            while (karsilastirilan != null) {
                // Yapım yılına göre sıralama kontrolü
                if (movie.getYear() < karsilastirilan.getMovie().getYear()) {
                    if (karsilastirilan == head) {
                        eklenen.setNext(karsilastirilan);
                        karsilastirilan.setPrevious(eklenen);
                        head = eklenen;
                    } else {
                        eklenen.setNext(karsilastirilan);
                        eklenen.setPrevious(karsilastirilan.getPrevious());
                        karsilastirilan.getPrevious().setNext(eklenen);
                        karsilastirilan.setPrevious(eklenen);
                    }
                    break;
                }
                // Yapım yılı aynı ise alfabetik sıralama kontrolü
                else if (movie.getYear() == karsilastirilan.getMovie().getYear()) {
                    if (movie.getTitle().compareToIgnoreCase(karsilastirilan.getMovie().getTitle()) < 0) {
                        if (karsilastirilan == head) {
                            eklenen.setNext(karsilastirilan);
                            karsilastirilan.setPrevious(eklenen);
                            head = eklenen;
                        } else {
                            eklenen.setNext(karsilastirilan);
                            eklenen.setPrevious(karsilastirilan.getPrevious());
                            karsilastirilan.getPrevious().setNext(eklenen);
                            karsilastirilan.setPrevious(eklenen);
                        }
                        break;
                    }
                }

                if (karsilastirilan.getNext() == null) {
                    karsilastirilan.setNext(eklenen);
                    eklenen.setPrevious(karsilastirilan);
                    tail = eklenen;
                    break;
                }

                karsilastirilan = karsilastirilan.getNext();
            }
        }
    }

    //Bilgisi istenilen filmi printliyoruz.
    public void filmBilgileri(String title) {
    Node node = head;
    
    // Listenin başından sonuna kadar döngü
    while (node != null) {
        Movie movie = node.getMovie();
        
        // Film bulundugunda yazdırıyor
        if (movie.getTitle().equals(title)) {
            System.out.println("***********************");
            System.out.println("Film Adi: " + movie.getTitle());
            System.out.println("Yapim Yili: " + movie.getYear());
            System.out.println("Kategori: " + movie.getCategory());
            System.out.println("Yonetmen: " + movie.getDirector());
            
            ArrayList<Actor> actors = movie.getActors();
            System.out.println("Oyuncular:");
            for (Actor actor : actors) {
                System.out.println("Isim: " + actor.getFullName());
                System.out.println("Cinsiyet: " + actor.getGender());
                System.out.println("Ulke: " + actor.getNationality());
            }
            System.out.println("***********************");
            return;
        }
        
        node = node.getNext();
    }
    
    System.out.println("Film Bulunamadi...");
}
    
    //Silinmesi istenilen filmi siliyoruz.
    public void filmSilme(String title) {
        
        boolean filmBulundu = false;
        
        //Silinecek film head ise
        if (head.getMovie().getTitle().equalsIgnoreCase(title)) {
            head = head.getNext();
            if (head != null) {
                head.setPrevious(null);
                System.out.println("Film Basariyla Silindi...");
            }
            filmBulundu = true;
        
        //Silinecek film tail ise
        } else if (tail.getMovie().getTitle().equalsIgnoreCase(title)) {
            tail = tail.getPrevious();
            if (tail != null) {
                tail.setNext(null);
                System.out.println("Film Basariyla Silindi...");
            }
            filmBulundu = true;
        
        //Silinecek film ara dugum ise
        } else {
            Node current = head;
            while (current != null) {
                if (current.getMovie().getTitle().equalsIgnoreCase(title)) {
                    current.getPrevious().setNext(current.getNext());
                    current.getNext().setPrevious(current.getPrevious());
                    filmBulundu = true;
                    break;
                }
                current = current.getNext();
            }
        }
        
        if (filmBulundu) {
            System.out.println("Film Basariyla Silindi...");
        } else {
            System.out.println("Film Bulunamadi...");
        }
}
    
    //Film listesini bastan sona yazdirma
    public void bastanSona(){
        Node node = head;
        
        while(node != null){
            
            System.out.println(node.getMovie().toString() + "***********************");
            node = node.getNext();
        }
    }
    
    //Film listesini sondan basa yazdirma
    public void sondanBasa(){
        Node node = tail;
        
        while(node != null){
           
            System.out.println(node.getMovie().toString() + "***********************");
            node = node.getPrevious();
        }
    }
    
    //Listede bulunan filmlerden yapim yili 2000'den once olanlari printleme
    public void ikiBindenOnce(){
        Node node = head;
        
        while(node != null){
            if(node.getMovie().getYear() < 2000){
                System.out.println(node.getMovie().toString() + "***********************");
            }
            node = node.getNext();
        }
    }
    
    //Dosyaya kaydetme
    public void dosyayaKaydetme() throws InterruptedException {
        try {
            File file = new File("bilgiler.txt");
            FileWriter fileWriter = new FileWriter(file);

            Node node = getHead();
            
            //Dosyaya kaydederken uygun format haline getiriyoruz bu şekilde dosyayı okurken hatalarla karşılaşmıyoruz
            while (node != null) {
                Movie movie = node.getMovie();
                
                StringBuilder stringBuilder = new StringBuilder();
                stringBuilder.append(movie.getYear()).append(",");
                stringBuilder.append(movie.getTitle()).append(", ");
                stringBuilder.append(movie.getCategory()).append(", ");
                stringBuilder.append(movie.getDirector()).append(", ");
                stringBuilder.append("{");

                ArrayList<Actor> actors = movie.getActors();
                for (int i = 0; i < actors.size(); i++) {
                    Actor actor = actors.get(i);
                    stringBuilder.append("(").append(actor.getFullName()).append(", ");
                    stringBuilder.append(actor.getGender()).append(", ");
                    stringBuilder.append(actor.getNationality()).append(")");
                }

                stringBuilder.append("}");

                String dosyayaEkleme = stringBuilder.toString();

                fileWriter.write(dosyayaEkleme);
                fileWriter.write(System.lineSeparator());

                node = node.getNext();
            }

            fileWriter.close();
            System.out.println("Dosya Kaydediliyor...");
            Thread.sleep(1000);
            System.out.println("Dosya Basariyla Guncellendi...");
        } catch (IOException e) {
            System.out.println("Dosya Yazma Hatası: " + e.getMessage());
        }
}
    
    
    
    
    
    
}