
public class Gato extends Animal {
	private double salto;

	public Gato(String nome, double peso, double salto) {
		super(nome, peso);
		this.salto = salto;
	}
	
	@Override
	public String emitirSom() {
		return "miauu";
	}

//	@Override
//	public String toString() {
//		return  super.toString() + ",  salto=" + salto ;
//	}

	public double getSalto() {
		return salto;
	}
	
	@Override
	public String toString() {
		return "nome=" + getNome() + 
				", peso=" + getPeso() + 
				", salto=" + salto +
				", emitirSom()=" + emitirSom() ;
	}
}
