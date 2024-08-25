public class EmployeeTest {
    public static void main(String[] args) {
        Date birth = new Date(1, 14, 2000);
        Date hire = new Date(3,12,2018);
        
        Employee worker1 = new Employee("Ali", "Tunc", birth, hire);
        
        Employee worker2 = new Employee("Ayse", "Demir", new Date(8, 19, 1980), new Date(5,11,2005));
        
        System.out.println(worker1);
        
        System.out.println(worker2);
    }
}
