
public class Venda {
	
	private String data;
	private String nome;
	private int quantidade;
	private double valor;
	public Venda(String data,Produto produto, int quantidade) {
		this.data = data;
		this.quantidade = quantidade;
		this.nome = produto.getNome();
		this.valor = quantidade * produto.getPreco();
		produto.setEstoque(produto.getEstoque() -  this.quantidade);
		
	}
	
	@Override
	public String toString() {
		return "Venda [data=" + data + " , valor=" + valor + "]";
	}
	

}
