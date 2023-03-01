
public class Venda {
	String data;
	Produto produto;
	int quantidade;
	double valor;
	public Venda(String data, Produto produto, int quantidade) {
		this.data = data;
		this.produto = produto;
		this.quantidade = quantidade;
		this.valor = calculaValor();
		this.decrementaEstoque();
		
	}
	
	@Override
	public String toString() {
		return "Venda [data=" + data + ", produto=" + produto + ", quantidade=" + quantidade + ", valor=" + valor + "]";
	}

	public double calculaValor() {
		return produto.getPreco() * quantidade;
	}
	
	public void decrementaEstoque() {
		int estoqueAtualizado = produto.getEstoque() -  quantidade;
		produto.setEstoque(estoqueAtualizado);
	}

}
