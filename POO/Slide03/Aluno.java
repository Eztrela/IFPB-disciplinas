
public class Aluno {
	double nota1;
	double nota2;
	String nome;
	
	public Aluno( String nome,double nota1, double nota2) {
		this.nota1 = nota1;
		this.nota2 = nota2;
		this.nome = nome;
	}
	
	public double getMedia() {
		return (nota1+nota2)/2;
	}
	
	public String getNome() {
		return nome;
	}
	
	public String getSituacao() {
		double media = this.getMedia();
		
		if(media >= 7) {
			return "aprovado";
		}else {
			if(media >= 5 && media < 7) {
				return "final";
			}else {
				return "reprovado";
			}
		}
	}
}
