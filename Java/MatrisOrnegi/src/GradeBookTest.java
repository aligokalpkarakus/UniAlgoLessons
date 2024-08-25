public class GradeBookTest {
    
    int[] gradesArray{(87, 96, 70),{68, 87, 90}, {94, 100, 90}, {100, 81, 82}, {83, 65, 85}, {78, 87, 65},{85, 75, 83}, {91, 94, 100}, {}};
    
    public static void main(String[] args) {
        GradeBook gb = new GradeBook("JAVA 101", gradesArray);
        gb.processGrades();
    }
}
