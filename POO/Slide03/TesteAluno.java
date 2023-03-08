public class TesteAluno {

	public static void main(String[] args) {
		Aluno a1 = new Aluno("joao", 100, 70) ;
		System.out.println(a1);

		Aluno a2 = new Aluno("maria", 20, 90) ;
		a2.setNota1(50);
		System.out.println(a2);
		
	}

}