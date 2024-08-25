public class Employee {
    private String adSoyad;
    private int kurumSicilNo;
    private String departman;
    private String pozisyon;
    
    // parametresiz default giriş için employee
    public Employee(){
        this.adSoyad = "";
        this.kurumSicilNo = 9999;
        this.departman = "";
        this.pozisyon = "";
    }
    
    // parametreli inputlarla employee bilgilerini aktarma
    public Employee(String adSoyad, int kurumSicilNo, String departman, String pozisyon){
        this.adSoyad = adSoyad;
        this.kurumSicilNo = kurumSicilNo;
        this.departman = departman;
        this.pozisyon = pozisyon;
    }
    
    // getler ve setler
    /**
     * @return the adSoyad
     */
    public String getAdSoyad() {
        return adSoyad;
    }

    /**
     * @param adSoyad the adSoyad to set
     */
    public void setAdSoyad(String adSoyad) {
        this.adSoyad = adSoyad;
    }

    /**
     * @return the kurumSicilNo
     */
    public int getKurumSicilNo() {
        return kurumSicilNo;
    }

    /**
     * @param kurumSicilNo the kurumSicilNo to set
     */
    public void setKurumSicilNo(int kurumSicilNo) {
        this.kurumSicilNo = kurumSicilNo;
    }

    /**
     * @return the departman
     */ 
    public String getDepartman() {
        return departman;
    }

    /**
     * @param departman the departman to set
     */
    public void setDepartman(String departman) {
        this.departman = departman;
    }

    /**
     * @return the pozisyon
     */
    public String getPozisyon() {
        return pozisyon;
    }

    /**
     * @param pozisyon the pozisyon to set
     */
    public void setPozisyon(String pozisyon) {
        this.pozisyon = pozisyon;
    }
    
    public String toString(){
        return "*****************\n" + "Ad Soyad: " + adSoyad + "\nKurum Sicil No: " + kurumSicilNo
                + "\nDepartman: " + departman + "\nPozisyon: " + pozisyon;
    }
}
