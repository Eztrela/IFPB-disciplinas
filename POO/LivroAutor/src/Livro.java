import java.util.ArrayList;

public class Livro {
    private String titulo;
    private ArrayList<Autor> autores = new ArrayList<>();

    public Livro(String titulo) {
        this.titulo = titulo;
    }

    public String getTitulo() {
        return titulo;
    }

    public ArrayList<Autor> getAutores() {
        return autores;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    @Override
    public String toString() {
        return "Livro{" +
                "titulo='" + titulo + '\'' +
                ", autores=" + autores +
                '}';
    }

    public void adicionar(Autor a){
        this.autores.add(a);
        a.adicionar(this);
    }

    public void remover(Autor a){
        this.autores.remove(a);
        a.remover(this);
    }
    public Autor localizar(String nome){
        for(Autor a: autores){
            if(a.getNome().equals(nome)){
                return a;
            }
        }
        return null;
    }

}
