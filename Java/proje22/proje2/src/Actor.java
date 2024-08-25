public class Actor {
    
    //degiskenler
    private String fullName;
    private String gender;
    private String nationality;
    
    //null constructor
    public Actor(){
        this.fullName = null;
        this.gender = null;
        this.nationality = null;
    }

    //actor constructor
    public Actor(String fullName, String gender, String nationality) {
        this.fullName = fullName;
        this.gender = gender;
        this.nationality = nationality;
    }
    
    //copy constructor
    public Actor(Actor other) {
        this.fullName = other.fullName;
        this.gender = other.gender;
        this.nationality = other.nationality;
    }
    
    //getter ve setter metodları
    public String getFullName() {
        return fullName;
    }

    public void setFullName(String fullName) {
        this.fullName = fullName;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public String getNationality() {
        return nationality;
    }

    public void setNationality(String nationality) {
        this.nationality = nationality;
    }
   
    //toString metodu, dosyaya kaydederken aktör bilgisini yazdırıyoruz.
    @Override
    public String toString() {
        return fullName + ", " + gender + ", " + nationality;
    }

}
