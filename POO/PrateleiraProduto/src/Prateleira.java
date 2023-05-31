import java.util.ArrayList;

public class Prateleira {
    private int id;
    private int tamanho;
    private ArrayList<Produto> produtos = new ArrayList<>();

    public Prateleira(int id, int tamanho) {
        this.id = id;
        this.tamanho = tamanho;
    }

    public int getId() {
        return id;
    }

    public int getTamanho() {
        return tamanho;
    }

    public ArrayList<Produto> getProdutos() {
        return produtos;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setTamanho(int tamanho) {
        this.tamanho = tamanho;
    }

    public void adicionar(Produto p){
        this.produtos.add(p);
        p.setPrateleira(this);
    }

    public void remover(Produto p){
        this.produtos.add(p);
        p.setPrateleira(null);
    }

    public Produto localizar(String nome){
        for(Produto p: produtos){
            if(p.getNome().equals(nome)){
                return p;
            }
        }
        return null;
    }

    @Override
    public String toString() {
        String texto = "Prateleira:" + id;
        texto += ", tamanho:" + tamanho ;
        texto += ", Produtos: " + produtos;
        return texto;
    }
}
