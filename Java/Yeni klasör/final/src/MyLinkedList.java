public class MyLinkedList {
    
    //degiskenler
    Node head;
    private Node tail;
    
    // null constructor
    public MyLinkedList(){    
        head = null;
        tail = null;
    }
    
    class Node{
        String item;
        Node next;
        Node prev;
    }

    //constructor
    public MyLinkedList(Node head, Node tail) {
        this.head = head;
        this.tail = tail;
    }
    
    // istenilen metoların yazılımı
    public void addtoStart(String str){
        Node node = new Node();
        node.item = str;
        
        if(head == null){
            head = node;
            tail = node;
        }
        else{
            node.next = head;
            head.prev = node;
            head = node;
        }
    }
    
    public String getElement(int i){
        Node node = head;
        int index = 0;
        
        while(node != null){
            if(index == i){
                return node.item;
            }
            node = node.next;
            index++;
        }
        // index bulunamazsa null döndürecek
        return null; 
    }
    
    public Node removeHead() {
        Node node = head;
        
        if (head == null) {
            return null;
        }

        if (head.next != null) {
            head = head.next;
            head.prev = null;
        } else {
            head = tail = null;
        }

        return node;
    }
    
    public Node removeLast() {
        Node node = tail;
        
        if (tail == null) {
            return null;
        }

        if (tail.prev != null) {
            tail = tail.prev;
            tail.next = null;
        } else {
            head = tail = null;
        }

        return node;
    }
    
    public Node remove(int i) {
        if (i < 0) { // indeks hatası için feedback
            throw new IndexOutOfBoundsException("Gecersiz Index: " + i);
        }

        if (i == 0) {   // 0 ise headi silmek için removeHead metodu
            return removeHead();
        }

        Node current = head;
        int index = 0;

        while (current != null) {
            if (index == i) {
                Node prevNode = current.prev;
                Node nextNode = current.next;

                if (prevNode != null) {
                    prevNode.next = nextNode;
                } else {
                    head = nextNode;
                }

                if (nextNode != null) {
                    nextNode.prev = prevNode;
                } else {
                    tail = prevNode;
                }

                return current;
            }

            current = current.next;
            index++;
        }

        throw new IndexOutOfBoundsException("Gecersiz Index: " + i);
    }

    public void printOut() { // listenin bastan sonra yazımı
        Node current = head;

        while (current != null) {
            System.out.println(current.item);
            current = current.next;
        }
    }
    
}
