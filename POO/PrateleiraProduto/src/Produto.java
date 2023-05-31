public class Produto {
    private String nome;
    private double preco;
    private Prateleira prateleira;
    private Fabricante fabricante;

    public Produto(String nome, double preco) {
        this.nome = nome;
        this.preco = preco;
    }

    public String getNome() {
        return nome;
    }

    public double getPreco() {
        return preco;
    }

    public Prateleira getPrateleira() {
        return prateleira;
    }

    public Fabricante getFabricante() {
        return fabricante;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }

    public void setPrateleira(Prateleira prateleira) {
        this.prateleira = prateleira;
    }

    public void setFabricante(Fabricante fabricante) {
        this.fabricante = fabricante;
    }

    @Override
    public String toString() {
        String texto = "nome=" + nome + ", preco=" + preco ;
        if (prateleira==null)
            texto+= ", sem prateleira";
        else
            texto+= ", prateleira= " + prateleira.getId();
        if (fabricante == null)
            texto += ", sem fabricante";
        else
            texto += ", fabricante= " + fabricante.getNome();
        return texto;
    }
}
