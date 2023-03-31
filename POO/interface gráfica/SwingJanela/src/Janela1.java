import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JMenuBar;
import javax.swing.JMenu;
import javax.swing.JMenuItem;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class Janela1 {

	private JFrame frmJanela;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Janela1 window = new Janela1();
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
	public Janela1() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frmJanela = new JFrame();
		frmJanela.setTitle("Janela 1");
		frmJanela.setBounds(100, 100, 450, 300);
		frmJanela.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frmJanela.getContentPane().setLayout(null);
		
		JButton btnNewButton = new JButton("abrir janela 2");
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				Janela2 janela2 = new Janela2();
			}
		});
		btnNewButton.setBounds(108, 58, 185, 23);
		frmJanela.getContentPane().add(btnNewButton);
		
		JButton btnAbrirJanela = new JButton("abrir janela 3");
		btnAbrirJanela.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				Janela3 janela3 = new Janela3();
			}
		});
		btnAbrirJanela.setBounds(108, 115, 185, 23);
		frmJanela.getContentPane().add(btnAbrirJanela);
		
		JMenuBar menuBar = new JMenuBar();
		menuBar.setBounds(0, 0, 83, 22);
		frmJanela.getContentPane().add(menuBar);
		
		JMenu mnNewMenu = new JMenu("Exibir");
		menuBar.add(mnNewMenu);
		
		JMenuItem mntmNewMenuItem = new JMenuItem("Segunda Janela");
		mntmNewMenuItem.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				btnNewButton.doClick();
			}
		});
		mnNewMenu.add(mntmNewMenuItem);
		
		JMenuItem mntmNewMenuItem_1 = new JMenuItem("Terceira Janela");
		mntmNewMenuItem_1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				btnAbrirJanela.doClick();
			}
		});
		mnNewMenu.add(mntmNewMenuItem_1);
		
		JMenu mnNewMenu_1 = new JMenu("Sair");
		mnNewMenu_1.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				frmJanela.dispose();
			}
		});
		
		menuBar.add(mnNewMenu_1);
	}
}
