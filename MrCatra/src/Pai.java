import java.util.ArrayList;

public class Pai {
    private String nome;
    private ArrayList<Filho> filhos = new ArrayList<>();

    public Pai(String nome) {
        this.nome = nome;
    }
    public void adicionar(Filho f){
        filhos.add(f);
    }
    public void remover(Filho f){
        filhos.remove(f);
    }

    public Filho localizar(String nome){
        for(Filho f: filhos){
            if(f.getNome().equals(nome))
                return f;
        }
        return null;
    }

    @Override
    public String toString() {
        return "Pai{" +
                "nome='" + nome + '\'' +
                ", filhos=" + filhos +
                '}';
    }

    public Filho obterCacula(){
        Filho menor = filhos.get(0);
        for(Filho filho: filhos){
            if (filho.getIdade() <= menor.getIdade()){
                menor = filho;
            }
        }
        return menor;
    }

    public double obterIdadeMedia(){
        int somaIdades = 0;
        for(Filho filho: this.filhos){
            somaIdades += filho.getIdade();
        }
        return somaIdades/filhos.size();
    }
}
