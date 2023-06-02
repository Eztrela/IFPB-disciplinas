/**
 * SI - POO - Prof. Fausto Ayres
 */


import java.util.ArrayList;

public class Evento {
	private int id;
	private String nome;
	private String data;
	private double preco;
	private ArrayList<Participante> participantes = new ArrayList<>();

	public Evento(int id, String nome, String data, double preco) {
		super();
		this.id = id;
		this.nome = nome;
		this.data = data;
		this.preco = preco;
	}
	public void adicionar(Participante p){
		participantes.add(p);
	}
	public void remover(Participante p){
		participantes.remove(p);
	}
	public Participante localizar(String nome){
		for(Participante p : participantes){
			if(p.getNome().equals(nome))
				return p;
		}
		return null;
	}
	@Override
	public String toString() {
		return "Evento [id=" + id + ", nome=" + nome + ", data=" + data + ", preco=" + preco + "]";
	}

	public double getTotalValorPago() {
		double totalPago = 0.0;
		for(Participante p: participantes)
			totalPago += p.getValorPago(this.preco);
		return totalPago;
	}

	public double getIdadeMedia() {
		double somaIdades = 0.0;
		for(Participante p: participantes)
			somaIdades += p.getIdade();
		return somaIdades/participantes.size();
	
	}

	public ArrayList<Participante> getParticipantesPorIdade(int idade) {
		ArrayList<Participante> menoresQue = new ArrayList<>();
		for(Participante p: participantes){
			if(p.getIdade() == idade)
				menoresQue.add(p);
		}
		return menoresQue;
	}
	
	public int contarConvidados() {
		int convidados = 0;
		for (Participante p: participantes){
			if(p instanceof Convidado){
				convidados +=1;
			}
		}
		return convidados;
	}
	
	public ArrayList<Convidado> getConvidados(String empresa) {
		ArrayList<Convidado> convidadosEmpresa = new ArrayList<>();
		for(Participante p: participantes){
			if(p instanceof Convidado c && c.getEmpresa().equals(empresa)){
				convidadosEmpresa.add(c);
			}
		}
		return convidadosEmpresa;
	}

	public ArrayList<Convidado> getConvidados() {
		ArrayList<Convidado> convidadosEmpresa = new ArrayList<>();
		for(Participante p: participantes){
			if(p instanceof Convidado c){
				convidadosEmpresa.add(c);
			}
		}
		return convidadosEmpresa;
	}

	public int contarGratuidades() {
		int gratuitos = 0;
		for(Participante p : participantes){
			if(p.getValorPago(this.preco) == 0){
				gratuitos += 1;
			}
		}
		return gratuitos;
		
	}
	
	
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public String getData() {
		return data;
	}
	public void setData(String data) {
		this.data = data;
	}
	public double getPreco() {
		return preco;
	}
	public void setPreco(double preco) {
		this.preco = preco;
	}
	public ArrayList<Participante> getParticipantes() {
		return participantes;
	}




}
