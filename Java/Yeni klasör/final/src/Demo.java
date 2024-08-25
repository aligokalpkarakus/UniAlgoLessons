
import java.util.Scanner;

public class Demo {
    public static void main(String[] args) {
        HashTable hashTable = new HashTable();
        
        // öğeler
        hashTable.put("Transformers");
        hashTable.put("Orumcek Adam");
        hashTable.put("Django");
        hashTable.put("Inanilmaz Aile");
        hashTable.put("Green Book");
        hashTable.put("Makas Eller");

        // listeyi yazdırma
        System.out.println("Liste:");
        hashTable.printHashTable();
        
        //silinmesi istenen film için input
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Silinmesini Istediginiz Film: ");
        String film = scanner.nextLine();
        
        // film silme ve true veya false değeri gönderme
        boolean deleted = hashTable.delete(film);
        if (deleted) {
            System.out.println("Deleted: " + deleted);
        } else {
            System.out.println("Item not found: " + deleted);
        }

        System.out.println("Guncel Liste:");
        hashTable.printHashTable();
    }
}