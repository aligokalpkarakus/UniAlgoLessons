
import java.util.Stack;

public class main {    
    public static void main(String[] args) {
        MyLinkedList myLinkedList = new MyLinkedList();

        // Listeye öğe ekleme kısmı
        myLinkedList.addtoStart("Transformers");
        myLinkedList.addtoStart("Orumcek Adam");
        myLinkedList.addtoStart("Inanilmaz Aile");
        myLinkedList.addtoStart("Django");
        myLinkedList.addtoStart("Green Book");
        
        System.out.println("Silinmeden Once:");
        myLinkedList.printOut();
        System.out.println("*************");
        
        // 3. elemanı siliyorum
        myLinkedList.remove(2);
        
        System.out.println("Silindikten Sonra:");
        
        // Listeyi yazdırma
        myLinkedList.printOut();
        System.out.println("*************");
        
        System.out.println("Tersten Yazdirma:");
        // Stack ile listeyi tersten yazdırma
        Stack<String> stack = new Stack<>();
        MyLinkedList.Node current = myLinkedList.head;
        
        while (current != null) {
            stack.push(current.item);
            current = current.next;
        }

        while (!stack.empty()) {
            System.out.println(stack.pop());
        }
    }
}
