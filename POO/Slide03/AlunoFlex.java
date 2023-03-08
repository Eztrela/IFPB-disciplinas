import java.util.Arrays;

public class AlunoFlex {
	private String nome;
	private double[] notas;
	private String matricula;
	
	public AlunoFlex( String nome, String matricula, double... notas) {
		this.nome = nome;
		this.notas = notas;
		this.matricula = matricula;
	}
	
	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public double[] getNotas() {
		return notas;
	}

	public void setNotas(double[] notas) {
		this.notas = notas;
	}

	public String getMatricula() {
		return matricula;
	}

	public void setMatricula(String matricula) {
		this.matricula = matricula;
	}


	@Override
	public String toString() {
		return "AlunoFlex [nome=" + nome + ", notas=" + Arrays.toString(notas) + ", matricula="
				+ matricula + "]";
	}

	public double calcularMedia() {
		double soma = 0;
		for(double nota:notas) {
			soma+=nota;
		}
		return (int)Math.round(soma/notas.length);
	}
	
	
	public String calcularSituacao() {
		double media = calcularMedia();
		if(media >= 70) {
			return "aprovado";
		}else {
			if(media >= 50 ) {
				return "final";
			}else {
				return "reprovado";
			}
		}
	}

}
