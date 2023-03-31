

import java.awt.EventQueue;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;

public class Placar {

	private JFrame frmPlacareletronico;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Placar window = new Placar();
					window.frmPlacareletronico.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
		
	}

	/**
	 * Create the application.
	 */
	public Placar() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frmPlacareletronico = new JFrame();
		frmPlacareletronico.setTitle("PlacarEletronico");
		frmPlacareletronico.setBounds(100, 100, 378, 217);
		frmPlacareletronico.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frmPlacareletronico.getContentPane().setLayout(null);
		
		JLabel labelImagemBrasil = new JLabel("");
		labelImagemBrasil.setBounds(23, 38, 46, 31);
		frmPlacareletronico.getContentPane().add(labelImagemBrasil);
		ImageIcon iconBrasil = new  ImageIcon(Placar.class.getResource("/imagens/brasil.png"));
		
		iconBrasil.setImage(iconBrasil.getImage().getScaledInstance(labelImagemBrasil.getWidth(), 
																	labelImagemBrasil.getHeight(), 
																	Image.SCALE_DEFAULT));
		
		labelImagemBrasil.setIcon(iconBrasil);
		
		JLabel labelImagemArgentina = new JLabel("");
		labelImagemArgentina.setBounds(23, 82, 46, 31);
		frmPlacareletronico.getContentPane().add(labelImagemArgentina);
		ImageIcon iconArgentina= new  ImageIcon(Placar.class.getResource("/imagens/argentina.png"));
		
		iconArgentina.setImage(iconArgentina.getImage().getScaledInstance(labelImagemArgentina.getWidth(), 
																	labelImagemArgentina.getHeight(), 
																	Image.SCALE_DEFAULT));
		
		labelImagemArgentina.setIcon(iconArgentina);
		
		
		JLabel labelBrasil = new JLabel("Brasil");
		labelBrasil.setBounds(79, 54, 74, 14);
		frmPlacareletronico.getContentPane().add(labelBrasil);
		
		JLabel labelArgentina = new JLabel("Argentina");
		labelArgentina.setBounds(79, 94, 74, 14);
		frmPlacareletronico.getContentPane().add(labelArgentina);
		
		JLabel golsBrasil = new JLabel("0");
		golsBrasil.setBounds(288, 54, 46, 14);
		frmPlacareletronico.getContentPane().add(golsBrasil);
		
		JLabel golsArgentina = new JLabel("0");
		golsArgentina.setBounds(288, 94, 46, 14);
		frmPlacareletronico.getContentPane().add(golsArgentina);
		
		JButton botaoBrasil = new JButton("gol");
		JButton botaoArgentina = new JButton("gol");
		botaoBrasil.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				Integer valor = Integer.parseInt(golsBrasil.getText());
				if (valor != 5) {
					valor++;
					golsBrasil.setText(Integer.toString(valor));
					if(valor == 5) {
						botaoBrasil.setEnabled(false);
						botaoArgentina.setEnabled(false);
						JOptionPane.showMessageDialog(frmPlacareletronico, "O Brasil Ganhou");
					}
					
				}
				
			}
		});
		
		botaoArgentina.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				Integer valor = Integer.parseInt(golsArgentina.getText());
				if (valor != 5) {
					valor++;
					golsArgentina.setText(Integer.toString(valor));
					if(valor == 5) {
						botaoBrasil.setEnabled(false);
						botaoArgentina.setEnabled(false);
						JOptionPane.showMessageDialog(frmPlacareletronico, "O Argentina Ganhou AMEGANNNN!!!!!!");
					}
					
				}
				
			}
		});
		botaoBrasil.setBounds(189, 50, 89, 23);
		frmPlacareletronico.getContentPane().add(botaoBrasil);
		
		
		botaoArgentina.setBounds(189, 90, 89, 23);
		frmPlacareletronico.getContentPane().add(botaoArgentina);
		
		
		
		JButton buttonRestart = new JButton("reiniciar");
		buttonRestart.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				botaoBrasil.setEnabled(true);
				botaoArgentina.setEnabled(true);
				golsArgentina.setText("0");
				golsBrasil.setText("0");
			}
		});
		buttonRestart.setBounds(126, 127, 89, 23);
		frmPlacareletronico.getContentPane().add(buttonRestart);
	}
}
