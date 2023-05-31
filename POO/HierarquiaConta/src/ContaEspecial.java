
public class ContaEspecial extends Conta {
	public double limite;
	
	public ContaEspecial(int numero, String cpf, double limite) {
		super (numero, cpf);
		this.limite=limite;
	}

	public void debitar(double valor) throws Exception {
		if(this.getSaldo() - valor < 0 - limite)
			throw new Exception("debito incorreto de "+ valor);	//lan�amento de alerta
		
		this.setSaldo(this.getSaldo()-valor);
	}
}

