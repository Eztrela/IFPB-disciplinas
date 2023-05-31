public class Participante {
	private String email;
	private String nome;
	private int idade;
	public Participante (String email, String nome, int idade) {
		this.email = email;
		this.nome = nome;
		this.idade = idade;
	}
	
	public int getPercentual () {
			if (this.idade < 18) {
				return 50;
			} else if (this.idade >= 60) {
				return 20;
			}
			return 0;
	}
	
	public double getValorPago (double preco) {
		return preco * (100 - this.getPercentual())/100;
	}
		
	public double getValorPago () {
		double preco = 1000;
		return preco * (100 - this.getPercentual())/100;
	}
	
	
	
	@Override
	public String toString() {
		return "Participante [email=" + email + ", nome=" + nome + ", idade=" + idade + "]";
	}

	public int getIdade() {
		return this.idade;
	}
}

	
