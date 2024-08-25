public class Node {
    
    //degiskenler
    private Movie movie;
    private Node previous;
    private Node next;

    //Node constructor
    public Node(Movie movie) {
        this.movie = movie;
        this.previous = null;
        this.next = null;
    }

    //getter ve setter metodları
    public Movie getMovie() {
        return movie;
    }

    public void setMovie(Movie movie) {
        this.movie = movie;
    }

    public Node getPrevious() {
        return previous;
    }

    public void setPrevious(Node previous) {
        this.previous = previous;
    }

    public Node getNext() {
        return next;
    }

    public void setNext(Node next) {
        this.next = next;
    }
    
    
  
}
