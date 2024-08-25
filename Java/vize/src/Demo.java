public class Demo {
    public static void main(String[] args) {
        //Nesne oluşturma kısmı
        ContactInfo contact = new ContactInfo("Osmaniye/Kadirli", "05367151972", "05210000198@ogrenci.ege.edu.tr");
        Person owner = new Person("Ali Gokalp Karakus", contact);
        Bus bus = new Bus("KARAKUS", "80 LE 331", owner, 80, 20);

        // Bus nesnesini yazdırma
        System.out.println("Bus Information:");
        System.out.println(bus.toString());

        // Motorlu taşıt vergisi hesaplama ve yazdırma
        int tax = bus.calculateTax();
        System.out.println("Motorlu Tasit Vergisi: " + tax + " TL");

        // Bus nesnesinin kopyasını oluşturma
        Bus busCopy = new Bus(bus);

        // İki bus nesnesini karşılaştırma ve true mu false mu değerini alma
        boolean equal = bus.equals(busCopy);
        System.out.println("Bus Objects Equal: " + equal);
    }
}