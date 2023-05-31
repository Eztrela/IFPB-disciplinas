public class Convidado extends Participante {
	private String empresa;
	
	
	public Convidado(String email, String nome, int idade, String empresa) {
		super(email, nome, idade);
		this.empresa = empresa;
	}
	
	public int getPercentual () {
		return super.getPercentual()+50;
	}

	public String getEmpresa () {
		return this.empresa;
	}
}
