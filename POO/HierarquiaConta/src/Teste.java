
/*
 * SI - POO - Fausto Ayres
 */

  public class Teste {
	public static void main(String[] args)	{	
		ContaEspecial conta1 = new ContaEspecial(2, "222", 500.0); 
		Conta conta2 = new Conta(1,"111"); 	//id, cpf
		
		
		conta1.creditar(500.0);					
		try{
			conta1.debitar(100.0);				//saldo 400
			conta1.transferir(400.0, conta2);	//saldo 0
			conta1.transferir(100.0, conta2);	//saldo -100
			conta1.transferir(500.0, conta2);	//exce��o
		}
		catch(Exception e) {
			System.out.println(e.getMessage()); 
		}
		System.out.println(conta1);		//saldo -100
		System.out.println(conta2);		//saldo 500
	}
}
  