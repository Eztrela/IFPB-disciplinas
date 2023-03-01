
public class TesteVendaProduto {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Produto p1 = new Produto("arroz", 10, 4.5);
		System.out.println("\nestoque antes da venda");
		System.out.println(p1);
		
		Venda v1 = new Venda("31/08/2022", p1, 2);
		System.out.println(v1);
		
		System.out.println("\n estoque depois da venda");
		System.out.println(p1);
	}

}
