import javax.swing.JFrame;

public class TesteAluno {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		AlunoFlex a1 = new AlunoFlex("joao", 10.0, 7.0);
		System.out.println(a1.getNome()+" "+a1.getMedia()+" "+a1.getSituacao());
		JFrame j  = new JFrame();
		j.setTitle("titulo");
		j.setSize(250,250);
		j.setVisible(true);
		

	}

}
