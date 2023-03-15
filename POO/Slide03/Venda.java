
public class Venda {
	private String data;
	private int quantidade;
	private double valor;
	public Venda(String data,Produto produto, int quantidade) {
		this.data = data;
		this.quantidade = quantidade;
		this.valor = quantidade * produto.getValor();
		produto.setestoque(produto.getEstoque() -  this.quantidade)
		
	}
	
	@Override
	public String toString() {
		return "Venda [data=" + data + ", produto=" + produto + ", quantidade=" + quantidade + ", valor=" + valor + "]";
	}

//	public double calculaValor() {
//		return produto.getPreco() * quantidade;
//	}
	
//	public void decrementaEstoque(Produto produto) {
//		int estoqueAtualizado = produto.getEstoque() -  quantidade;
//		produto.setEstoque(estoqueAtualizado);
//	}

}
