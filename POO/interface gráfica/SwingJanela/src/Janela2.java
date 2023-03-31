import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JButton;

public class Janela2 {

	private JFrame frmJanela;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Janela2 window = new Janela2();
					window.frmJanela.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public Janela2() {
		initialize();
		frmJanela.setVisible(true);
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frmJanela = new JFrame();
		frmJanela.setTitle("Janela2");
		frmJanela.setBounds(100, 100, 450, 300);
		frmJanela.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
		frmJanela.getContentPane().setLayout(null);
		
		JButton btnNewButton = new JButton("Fechar");
		btnNewButton.setBounds(165, 100, 89, 23);
		frmJanela.getContentPane().add(btnNewButton);
	}

}
