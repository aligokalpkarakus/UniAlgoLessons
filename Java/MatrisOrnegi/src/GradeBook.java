public class GradeBook {
    
    private String courseName;
    private int [][] grades;

    public GradeBook() {
    }

    public GradeBook(String courseName, int[][] gradesArray) {
        this.courseName = courseName;
        this.grades = gradesArray;
    }

    public String getCourseName() {
        return courseName;
    }

    public void setCourseName(String courseName) {
        this.courseName = courseName;
    }
    
    public void processGrades(){
        outputGrades();
        outputBarChart();
    }
    
    private void outputGrades(){
        System.out.printf("\nWelcome to the grade book for\n&s\nThe grades are:\n", this.courseName);
        System.out.println("             ");
        
        for (int i = 0; i < grades[0].length; i++) {
            System.out.printf("Test %d", (i+1));
        }
        
        System.out.printf("Average\n");
        
        for(int i = 0; i < grades.length; i++){
            System.out.printf("Student %2d: ", (i + 1));
            for(int grade : grades[i]){
                System.out.printf("%8d", grade);
            }
            double avg = getAverage(grades[i]);
            System.out.printf("%10.2f", avg);
            System.out.println(""); 
        }
    }
    
    private double getAverage(int [] grades){
        double avg = 0;
        for (int grade : grades) {
            avg += grade;
        }
        
        avg /= grades.length;
        
        return avg;
    }
    
    private void outputBarChart(){
        int [] freq = new int[11];
        for (int[] studentGrades : grades) {
            for (int studentGrade : studentGrades) {
                freq[studentGrade/10]++;
            }
        }
        
        for (int i = 0; i < freq.length; i++) {
            if(i < 10){
                int start = i*10;
                int end = i+9;
                System.out.printf("%2d-%2d: ", start, end);
            }
            else{
                System.out.printf("%2d: ", 100);
            }
            for (int j = 0; j < freq[i]; j++) {
                System.out.print("*");
            }
            System.out.println("");
        } 
    }
}
