public class Doctor extends SalariedEmployee{
    
    private String brans;
    private double viziteUcreti;
    
    public Doctor(){
        super();
        brans = "None";
        viziteUcreti = 0.0;
    }

    public Doctor(String brans, double viziteUcreti, String theName, Date theDate, double theSalary) {
        super(theName, theDate, theSalary);
        if(brans == null){
            System.out.println("Fatal Error: Empty Speciality.");
            System.exit(0);
        }
        if(viziteUcreti < 0){
            System.out.println("Fatal Error: Negative Office Visit Fee.");
            System.exit(0);
        }
        this.brans = brans;
        this.viziteUcreti = viziteUcreti;
    }

    public Doctor(Doctor other){
        super(other);
        brans = other.brans;
        viziteUcreti = other.viziteUcreti;
    }
    
    public boolean equals(Object other){
        if(other == null){
            return false;
        }
        else if(this.getClass()!=other.getClass()){
            return false;
        }
        else{
            Doctor doctor = (Doctor)other;
            return (this.getName().equals(doctor.getName()) && this.getHireDate().equals(doctor.getHireDate()) && this.getSalary() == doctor.getSalary());
        }
    }
    
    public String to String(){
        String result = super.toString();
        result += ", " + getBrans() + ", $" + getViziteUcreti() + "per office visit.";
        return result;
    }
    
    public double getPay(int aylikToplamHastaSayisi){
        return super.getPay() +
        
    }
    
}
