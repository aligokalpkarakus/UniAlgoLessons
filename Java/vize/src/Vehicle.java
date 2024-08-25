public abstract class Vehicle {
    
    private String brand;
    private String licencePlate;
    private Person owner;
    
    public Vehicle(){
        this.brand = null;
        this.licencePlate = null;
        this.owner = null;
    }

    public Vehicle(String brand, String licencePlate, Person owner) {
        this.brand = new String(brand);
        this.licencePlate = new String (licencePlate);
        this.owner = new Person(owner);
    }
    
    public Vehicle(Vehicle other) {
        this.brand = new String(other.brand);
        this.licencePlate = new String(other.licencePlate);
        this.owner = new Person(other.owner);
    }
    
    public abstract int calculateTax();

    public String getBrand() {
        return new String(brand);
    }

    public void setBrand(String brand) {
        this.brand = new String(brand);
    }

    public String getLicencePlate() {
        return new String(licencePlate);
    }

    public void setLicencePlate(String licencePlate) {
        this.licencePlate = new String(licencePlate);
    }

    public Person getOwner() {
        return new Person(owner);
    }

    public void setOwner(Person owner) {
        this.owner = new Person(owner);
    }
    
    @Override
    public String toString() {
        return "Brand: " + this.brand + ", Licence Plate: " + this.licencePlate + ",\n---------------------------------------\nOwner's " + this.owner;
    }
    
    
    @Override
    public boolean equals(Object object) {
        if (object instanceof Vehicle) {
            Vehicle other = (Vehicle) object;
            return this.brand.equals(other.brand) && this.licencePlate.equals(other.licencePlate) && this.owner.equals(other.owner);
        }
        return false;
    }
    
    
    
    
    
}
