
public class Retangulo {
	
	public int id;
	public double largura;
	public double comprimento;
	
	public Retangulo(int id, double largura, double comprimento) {
		this.id = id;
		this.largura = largura;
		this.comprimento = comprimento;
	}
	
	public Retangulo(double lado) {
		this.largura = lado;
		this.comprimento = lado;
	}
	
	public Retangulo() {}
	
	public double calculaArea(){
		return largura * comprimento;
	}
	
	public double calcularPerimetro() {
		return (largura * 2) + (comprimento * 2);
	}
}
