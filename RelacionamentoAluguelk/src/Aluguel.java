public class Aluguel {
    private Casa casa;
    private Pessoa inquilino;

    public Aluguel(Casa casa, Pessoa inquilino) {
        this.casa = casa;
        this.inquilino = inquilino;
    }

    public Casa getCasa() {
        return casa;
    }

    public Pessoa getInquilino() {
        return inquilino;
    }

    public void setCasa(Casa casa) {
        this.casa = casa;
    }

    public void setInquilino(Pessoa inquilino) {
        this.inquilino = inquilino;
    }

    public double getValorAluguel(){
        return this.casa.getPrecoVenda() * 0.003;
    }
}
