import java.util.ArrayList;

public class testeParticipante {

	public static void main(String[] args) {
		Participante joao = new Participante("joao@gmail.com", "joao", 17);
		Participante maria = new Participante ("maria@gmail.com","maria",30);
		Participante pedro = new Participante ("pedro@gmail.com","pedro",70);
		Convidado paulo = new Convidado("paulo@gmail.com", "paulo", 17, "IFPB");
		Convidado katia = new Convidado("katia@gmail.com", "katia", 30, "IFPB");
		Convidado antonio = new Convidado("antonio@gmail.com", "antonio", 70, "IFPB");
		Convidado paula = new Convidado("paula@gmail.com", "paula", 17, "IFPB");
		
		ArrayList<Participante> lista = new ArrayList<>();
		lista.add(joao);
		lista.add(maria);
		lista.add(pedro);
		lista.add(paulo);
		lista.add(katia);
		lista.add(antonio);
		lista.add(paula);
		
		ArrayList<Participante> participantes1730 = new ArrayList<>();
		ArrayList<Convidado> listaConvidados = new ArrayList<>();
		ArrayList<Participante> listaSemIdoso = new ArrayList<>();
		
		double total = 0;
		double valorPago = 0;
		int gratuidades = 0;
		
		for (Participante a : lista) {
			valorPago = a.getValorPago(1000);
			total += valorPago;
			
			if (valorPago == 0) {
				gratuidades += 1;
			}
			
			if (a.getIdade() >= 17 && a.getIdade() <= 30) {
				participantes1730.add(a);
			}
			
			if (a instanceof Convidado c) {
				if (c.getEmpresa().equals("IFPB")) {
					listaConvidados.add(c);
				}
			}
			
			
		}
		
		for (Participante b : lista) {
			if (b.getIdade() < 60) listaSemIdoso.add(b);
		}
		
		lista = listaSemIdoso;
		
	System.out.println("Gratuitos: "+ gratuidades);
	System.out.println("Total Arrecadado: " + total);
	System.out.println(listaConvidados);
	System.out.println(lista);
	System.out.println("\nvalores pagos pelos participantes para um evento de R$ 1000");
	System.out.println("João = R$ " +joao.getValorPago(1000));
	System.out.println("Maria = R$ " +maria.getValorPago(1000));
	System.out.println("Pedro = R$ " +pedro.getValorPago(1000));
	System.out.println("\nvalores pagos pelos convidados para um evento de R$ 1000");
	System.out.println("Paulo = R$ " +paulo.getValorPago(1000));
	System.out.println("Katia = R$ " +katia.getValorPago(1000));
	System.out.println("Antonio = R$ " +antonio.getValorPago(1000));
	System.out.println("paula = R$ " +paula.getValorPago(1000));
		
	}
	
	
}
