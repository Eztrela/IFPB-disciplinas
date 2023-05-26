public class Filho {
    public String nome;
    public int idade;

    public Filho(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    public String getNome() {
        return nome;
    }

    public int getIdade() {
        return idade;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    @Override
    public String toString() {
        return "Filho{" +
                "nome='" + nome + '\'' +
                ", idade=" + idade +
                '}';
    }
}
