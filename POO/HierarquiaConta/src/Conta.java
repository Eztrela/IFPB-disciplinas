/*
 * SI - POO - Fausto Ayres
 */
public class Conta {
	private int numero;
	private String cpf;
	private double saldo2=0;
	
	public Conta(int numero, String cpf) {
		this.numero = numero;
		this.cpf = cpf;
	}
	public void creditar(double valor) {
		saldo2 = saldo2 + valor;
	}
	public void debitar(double valor) throws Exception {
		if(valor > saldo2)
			throw new Exception("debito incorreto de "+ valor);	//lan�amento de alerta
		
		saldo2 = saldo2 - valor;
	}
	public void transferir(double valor, Conta destino) throws Exception  {
		this.debitar(valor);
		destino.creditar(valor);
	}

	@Override
	public String toString() {
		return "numero=" + numero + ", cpf=" + cpf + ", saldo=" + saldo2;
	}

	
	public int getNumero() {
		return numero;
	}
	public String getCpf() {
		return cpf;
	}
	public double getSaldo() {
		return saldo2;
	}
	
	public void setSaldo(double saldo2) {
		this.saldo2 = saldo2;
		}
	
	
	
}
