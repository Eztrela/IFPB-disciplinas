
public class Conta {
	public String numero;
	public String cpf;
	public double saldo;
	
	public Conta(String numero, String cpf) {
		this.numero = numero;
		this.cpf = cpf;
		this.saldo = 0;
	}
	
	public void creditar(double valor) {
		saldo += valor;
	}
	
	public void debitar(double valor) {
		saldo -= valor;
	}
	
	public void transferir(double valor, Conta conta) {
		this.debitar(valor);
		conta.creditar(valor);
	}
	
	public boolean vazia() {
		if (saldo == 0) {
			return true;
		}else {
			return false;
		}
	}
	
	public Conta clonar() {
		Conta c2 = new Conta(numero, cpf);
		c2.creditar(saldo);
		return c2;
	}

	@Override
	public String toString() {
		return "Conta [numero=" + numero + ", cpf=" + cpf + ", saldo=" + saldo + "]";
	}
	
	
}
