import java.util.ArrayList;

public class Fabricante {
    private String nome;
    private ArrayList<Produto> produtos = new ArrayList<>();

    public Fabricante(String nome) {
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }

    public ArrayList<Produto> getProdutos() {
        return produtos;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void adicionar(Produto p){
        this.produtos.add(p);
        p.setFabricante(this);
    }

    public void remover(Produto p){
        this.produtos.add(p);
        p.setFabricante(this);
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
        String texto = "Prateleira:" + nome + "Produtos: " + produtos;

        return texto;
    }
}
