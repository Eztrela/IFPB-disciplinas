public class Casa {
    private Pessoa proprietario;
    private String endereco;
    private String bairro;
    private double precoVenda;

    public Casa(Pessoa proprietario, String endereco, String bairro, double precoVenda) {
        this.proprietario = proprietario;
        this.endereco = endereco;
        this.bairro = bairro;
        this.precoVenda = precoVenda;
    }

    public Pessoa getProprietario() {
        return proprietario;
    }

    public String getEndereco() {
        return endereco;
    }

    public String getBairro() {
        return bairro;
    }

    public double getPrecoVenda() {
        return precoVenda;
    }

    public void setProprietario(Pessoa proprietario) {
        this.proprietario = proprietario;
    }

    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }

    public void setBairro(String bairro) {
        this.bairro = bairro;
    }

    public void setPrecoVenda(double precoVenda) {
        this.precoVenda = precoVenda;
    }
}
