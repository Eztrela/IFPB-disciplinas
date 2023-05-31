
public abstract class Animal {
	private String nome;
	private double peso;
	
	public Animal(String nome, double peso) {
		super();
		this.nome = nome;
		this.peso = peso;
	}
	
	public abstract String emitirSom() ;

	@Override
	public String toString() {
		return "nome=" + nome + 
				", peso=" + peso + 
				", emitirSom()=" + emitirSom() ;
	}

	public String getNome() {
		return nome;
	}

	public double getPeso() {
		return peso;
	}
	
	
}
