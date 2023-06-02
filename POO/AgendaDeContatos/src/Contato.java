import java.util.ArrayList;

public class Contato {
    private String nome;
    private String logradouro;
    private ArrayList<Telefone> telefones = new ArrayList<>();

    public Contato(String nome, String logradouro) {
        this.nome = nome;
        this.logradouro = logradouro;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getLogradouro() {
        return logradouro;
    }

    public void setLogradouro(String logradouro) {
        this.logradouro = logradouro;
    }

    public void adicionar (Telefone t){
        this.telefones.add(t);
        t.adicionar(this);
    }

    public void remover (Telefone t){
        telefones.remove(t);
        t.remover(this);
    }

    public Telefone localizar(String numero){
        for (Telefone t: telefones){
            if (numero.substring(0,3) == t.getDdd() || numero.substring(3) == t.getNumero()){
                return t;
            }
        }
        return null;
    }
    @Override
    public String toString() {
        String texto = "Contato{" +
                "nome='" + nome + '\'' +
                ", logradouro='" + logradouro + '\'' + '}' +
                ", Contatos: ";
        for (Telefone t : telefones) {
            texto += "(" + t.getDdd() + ") " + t.getNumero() + ", ";
        }
        return texto;
    }
}
