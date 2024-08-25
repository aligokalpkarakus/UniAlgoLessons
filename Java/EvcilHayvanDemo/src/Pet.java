public abstract class Pet {
    
    private String name;
    private int age;
    private double weight;
    
    public Pet(String initialName, int initialAge, double initialWeight){
        
        name = initialName;
        if(initialAge < 0 || initialWeight < 0){
            System.out.println("Error: Negative age or weight");
            System.exit(0);
        }
        else{
            age = initialAge;
            weight = initialAge;
        }
        
    }
    
    public abstract double ilac01Dozaj();
    public abstract double ilac02Dozaj();
    

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public double getWeight() {
        return weight;
    }

    public void setWeight(double weight) {
        this.weight = weight;
    }
    
    
}
