import java.util.ArrayList;

public class Telefone {
    private String ddd;
    private String numero;
    private ArrayList<Contato> contatos = new ArrayList<>();

    public Telefone(String ddd, String numero) {
        this.ddd = ddd;
        this.numero = numero;
    }

    public String getDdd() {
        return ddd;
    }

    public String getNumero() {
        return numero;
    }

    public void setDdd(String ddd) {
        this.ddd = ddd;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }

    public void adicionar(Contato c){
        this.contatos.add(c);
    }
    public void remover(Contato c){
        this.contatos.remove(c);
    }

    @Override
    public String toString() {
        String texto = "Telefone{" +
                "ddd='" + ddd + '\'' +
                ", numero='" + numero + '\'' + "}" +
                ", Contatos: ";
        for(Contato c: contatos) {
            texto += c.getNome() + ", ";
        }
        return texto;
    }

}
