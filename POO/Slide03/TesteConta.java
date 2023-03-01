
public class TesteConta {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Conta conta1 = new Conta("333","123456");
		conta1.creditar(300.0);	
		Conta conta2 = conta1.clonar();
		conta1.creditar(200.0);
		System.out.println(conta1);
		System.out.println(conta2);
		
	}

}
