import javax.swing.JFrame;

public class TesteAlunoFlex {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		AlunoFlex a1 = new AlunoFlex("joao","20221370085", 100);
		System.out.println(a1.getNome()+" "+a1.calcularMedia()+" "+a1.calcularSituacao());
		JFrame j  = new JFrame();
		j.setTitle("titulo");
		j.setSize(250,250);
		j.setVisible(true);
		

	}

}
