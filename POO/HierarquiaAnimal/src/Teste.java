
public class Teste {

	public static void main(String[] args) {
		//instanciar os objetos
		Gato fifi = 	new Gato("fifi", 5, 3);
		Cachorro rex = 	new Cachorro("rex", 15);

		//exibir nome, peso e som dos objetos
		System.out.println(rex);	 	//”rex 15 au au”
		System.out.println(fifi);	 	//”fifi 5 miau”
		
		Bode nino = new Bode("Nino", 20.0);
		System.out.println(nino);
	}

}
