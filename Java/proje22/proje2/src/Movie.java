
import java.util.ArrayList;

public class Movie {
    //degiskenler
    private int year;
    private String title;
    private String category;
    private String director;
    private ArrayList<Actor> actors;
    
    //null constructor
    public Movie(){
        this.year = 0000;
        this.title = null;
        this.category = null;
        this.director = null;
        this.actors = null;
    }

    //movie constructor
    public Movie(int year, String title, String category, String director, ArrayList<Actor> actors) {
        this.year = year;
        this.title = title;
        this.category = category;
        this.director = director;
        this.actors = actors;
    }
    
    //copy constructor
    public Movie(Movie other){
        this.year = other.year;
        this.title = other.title;
        this.category = other.category;
        this.director = other.director;
        this.actors = other.actors;
    }
    
    // getter ve setter metodları
    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public String getDirector() {
        return director;
    }

    public void setDirector(String director) {
        this.director = director;
    }

    public ArrayList<Actor> getActors() {
        return actors;
    }

    public void setActors(ArrayList<Actor> actors) {
        this.actors = actors;
    }
    
    //Film bilgisi gösterirken listeyi stringe dönüştürerek yazdırmak istedik. StringBuilderdan obje yaratarak verimli bir şekilde output aldık
    @Override
    public String toString() {
    StringBuilder stringBuilder = new StringBuilder();
    stringBuilder.append("Year: ").append(year).append("\n");
    stringBuilder.append("Title: ").append(title).append("\n");
    stringBuilder.append("Category: ").append(category).append("\n");
    stringBuilder.append("Director's Full Name: ").append(director).append("\n");
    stringBuilder.append("Actors:\n");
    for (Actor actor : actors) {
        stringBuilder.append("Isim: ").append(actor.getFullName()).append("\n");
        stringBuilder.append("Cinsiyet: ").append(actor.getGender()).append("\n");
        stringBuilder.append("Ulke: ").append(actor.getNationality()).append("\n");
    }
    return stringBuilder.toString();
}
    
}