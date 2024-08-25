public class Rectangle {
    private double en;
    private double boy;
    
    public Rectangle(){
        en = 1.0;
        boy = 1.0;
    }
    
    public Rectangle(double en, double boy){
        this.en = en;
        this.boy = boy;
    }
    
    public double cevre(){
        return 2 * (getEn() + getBoy());
    }
    
    public double alan(){
        return getEn() * getBoy();
    }

    /**
     * @return the en
     */
    public double getEn() {
        return en;
    }

    /**
     * @param en the en to set
     */
    public void setEn(double en) {
        this.en = en;
    }

    /**
     * @return the boy
     */
    public double getBoy() {
        return boy;
    }

    /**
     * @param boy the boy to set
     */
    public void setBoy(double boy) {
        this.boy = boy;
    }
    
    public String toString(){
        return String.format("%s: %.2f%n%s: %.2f%n%s: %.2f%n%s: %.2f",
                "Boy", getBoy(), "En", getEn(),
                "Cevre", cevre(),
                "Alan", alan());
    }
    
}
