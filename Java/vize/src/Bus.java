public class Bus extends Vehicle{
    
    private int capacity;
    private int ageOfBus;
    
    public Bus(){
        super();
        this.capacity = 0;
        this.ageOfBus = 0;
    }

    public Bus(String brand, String licencePlate, Person owner, int capacity, int ageOfBus) {
        super(brand, licencePlate, owner);
        this.capacity = capacity;
        this.ageOfBus = ageOfBus;
    }

    public Bus(Bus other) {
        super(other.getBrand(), other.getLicencePlate(), other.getOwner());
        this.capacity = other.getCapacity();
        this.ageOfBus = other.getAgeOfBus();
    }

    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }

    public int getAgeOfBus() {
        return ageOfBus;
    }

    public void setAgeOfBus(int ageOfBus) {
        this.ageOfBus = ageOfBus;
    }
    
    
    @Override
    public int calculateTax() {
        if (ageOfBus < 5) {
            return 4000;
        } else if (ageOfBus >= 5 && ageOfBus <= 10) {
            return 3000;
        } else {
            return 2000;
        }
    }

    @Override
    public String toString() {
        return super.toString() + "\n---------------------------------------\nCapacity:" + capacity + ", Age of bus=" + ageOfBus;
    }

    @Override
    public boolean equals(Object object) {
        if (object == this) {
            return true;
        }
        if (!(object instanceof Bus)) {
            return false;
        }
        Bus other = (Bus) object;
        return super.equals(other) && this.capacity == other.getCapacity() && this.ageOfBus == other.getAgeOfBus();
    }
    
    
    
}
