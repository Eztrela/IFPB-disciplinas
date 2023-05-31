import java.util.ArrayList;

public class Autor {
    private String nome;
    private ArrayList<Livro> livros = new ArrayList<>();

    public Autor(String nome) {
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }

    public ArrayList<Livro> getLivros() {
        return livros;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void adicionar(Livro liv){
        this.livros.add(liv);
    }

    public void remover(Livro liv){
        this.livros.remove(liv);
    }
    public Livro localizar(String tit){
        for(Livro liv: livros){
            if(liv.getTitulo().equals(tit)){
                return liv;
            }
        }
        return null;
    }

    @Override
    public String toString() {
        String texto = "Autor"
//        if (livros.isEmpty())
//            texto += " n�o tem produto";
//        else
//        {	texto += " produtos da prateleira: ";
//            for(Produto p: produtos) texto += " " + p.getNome();
//        }
        return "Autor{" +
                "nome='" + nome + '\'' +
                '}';
    }
}
