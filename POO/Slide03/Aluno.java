
public class Aluno {
	private int nota1;
	private int nota2;
	private String nome;
	
	public Aluno( String nome,int nota1, int nota2) {
		this.nota1 = nota1;
		this.nota2 = nota2;
		this.nome = nome;
	}
	
	public int calcularMedia() {
		double media = (nota1+nota2)/2.0;
		return (int)Math.round(media);
	}
	
	
	
	public String calcularSituacao() {
		int media = this.calcularMedia();
		
		if(media >= 70) {
			return "aprovado";
		}else {
			if(media >= 40) {
				return "final";
			}else {
				return "reprovado";
			}
		}
	}
	
	@Override
	public String toString() {
		return "Aluno [nome=" + nome + ", nota1=" + nota1 + ", nota2=" + nota2 + ""
				+ ", calcularMedia()=" + calcularMedia()
				+ ", calcularSituacao()=" + calcularSituacao() + "]";
	}
	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public int getNota1() {
		return nota1;
	}

	public void setNota1(int nota1) {
		this.nota1 = nota1;
	}

	public int getNota2() {
		return nota2;
	}

	public void setNota2(int nota2) {
		this.nota2 = nota2;
	}
}
