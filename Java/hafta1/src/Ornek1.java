
import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ornek1 {
    public static void main(String[] args) {
        // 1
        System.out.println("Hello World");
        
        // 2
        
        double r = 5.7;
        double pi = 3.1415;
        double area = r * r * pi;
        System.out.println("r: " + r + " Alan: " + area);
        
        // 3 formatlı yazma aşağıda .2 iki basamak yaptı
        
        System.out.printf("r = %.2f Area = %.2f", r, area);
        System.out.println("");
        // 4 math kütüp ile area = r * r *Math.PI yapabiliriz
        
        // 5 pig latin
        
        /*
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter firstname: ");
        String firstname = scanner.nextLine();
        System.out.print("Enter lastname: ");
        String lastname = scanner.nextLine();
        System.out.println(firstname + " " + lastname);
        */
        
        // 6 lowercase yapma ve ilk harfi sona ekleme + ay eklemw
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter firstname: ");
        String firstname = scanner.nextLine();
        System.out.print("Enter lastname: ");
        String lastname = scanner.nextLine();
        
        firstname = firstname.toLowerCase();
        lastname = lastname.toLowerCase();
        
        String pigLatinFirstname = firstname.substring(1) + firstname.substring(0, 1) + "ay";
        String pigLatinLastname = lastname.substring(1) + lastname.substring(0, 1) + "ay";
        
        pigLatinFirstname = pigLatinFirstname.substring(0, 1).toUpperCase() + pigLatinFirstname.substring(1);
        pigLatinLastname = pigLatinLastname.substring(0, 1).toUpperCase() + pigLatinLastname.substring(1);
        
        System.out.println("Pig Latin: " + pigLatinFirstname + " " + pigLatinLastname);
        
        // 7 Joptionpane input dialog ve message dialog kullanımı
        
        String isim = JOptionPane.showInputDialog("Enter isim: ");
        String soyisim = JOptionPane.showInputDialog("Enter soyisim: ");
        JOptionPane.showMessageDialog(null, isim + " " + soyisim);
        
        // 8 Joptionpane ile alınan bilgilerle çıktı verme
        
        String name = JOptionPane.showInputDialog("Enter name: ");
        String inputString;
        double hourlyPayRate = 0;
        boolean isValid = false;
        while (isValid){
            try {
                inputString = JOptionPane.showInputDialog("Enter hourly pay rate: ");
                hourlyPayRate = Double.parseDouble(inputString);
                isValid = true;
            } catch (Exception e) {
                isValid = false;
            }
            
        }
        
        
        inputString = JOptionPane.showInputDialog("Enter hours worked: ");
        double hours = Double.parseDouble(inputString);
        
        double payment = hourlyPayRate * hours;
                
        JOptionPane.showMessageDialog(null,"Hello " + name + " your payment is $" + payment);
    }
}
