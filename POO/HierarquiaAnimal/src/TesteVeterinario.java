
public class TesteVeterinario {

	public static void main(String[] args) {
		Gato fifi = new Gato("fifi", 5, 3);
		Cachorro rex = new Cachorro("rex", 15);
		Veterinario bob = new Veterinario("Bob");

		System.out.println( bob.aplicarInjecao(fifi) ) ;
		System.out.println( bob.aplicarInjecao(rex) ) ;
		
		Bode nino = new Bode("Nino", 20.0);
		System.out.println( bob.aplicarInjecao(nino));
	}

}
