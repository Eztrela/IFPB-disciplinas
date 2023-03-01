
public class AlunoFlex {
	String nome;
	double[] notas;
	double media;
	
	public AlunoFlex( String nome,double... notas) {
		this.nome = nome;
		this.notas = notas;
	}
	
	public double getMedia() {
		double soma = 0;
		for(double nota:notas) {
			soma+=nota;
		}
		return soma/notas.length;
	}
	
	public String getNome() {
		return nome;
	}
	
	public String getSituacao() {
		double media = getMedia();
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
