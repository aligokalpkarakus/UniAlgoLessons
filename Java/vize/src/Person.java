public class Person {
    private String name;
    private ContactInfo contactInformation;
    
    public Person(){
        this.name = null;
        this.contactInformation = null;
    }
    
    public Person(String name, ContactInfo contactInformation) {
        this.name = new String(name);
        this.contactInformation = new ContactInfo(contactInformation);
    }
    
    public Person(Person other){
        this.name = new String(other.name);
        this.contactInformation = new ContactInfo(other.contactInformation);
    }

    public String getName() {
        return new String(name);
    }

    public void setName(String name) {
        this.name = new String(name);
    }

    public ContactInfo getContactInformation() {
        return new ContactInfo(contactInformation);
    }

    public void setContactInformation(ContactInfo contackInformation) {
        this.contactInformation = new ContactInfo(contactInformation);
    }

    @Override
    public String toString() {
        return "Name: " + getName() + "\nContact Information:\n" + getContactInformation();
    }
    
    public boolean equals(Object other) {
        if (other == null) {
            return false;
        }
        else if(this.getClass() != other.getClass()){
            return false;
        }
        else{
            Person person = (Person) other;
            return (this.getContactInformation().equals(person.getContactInformation()) &&
                    this.getName().equals(person.getName()));
            
        }
       
    }

    
}
