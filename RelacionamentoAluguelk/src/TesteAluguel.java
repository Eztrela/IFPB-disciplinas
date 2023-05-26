public class TesteAluguel {
    public static void main(String[] args) {
        Pessoa joao = new Pessoa("joao da silva", "123.000.555-88");
        Pessoa maria = new Pessoa("maria de sousa", "222.101.666-32");
        Casa casa = new Casa(joao, "rua primeiro de maio, 45","jaguaribe",800000.0);
        Aluguel alug1 = new Aluguel(casa, maria);
        double valor = alug1.getValorAluguel();
        System.out.println(valor);
    }
}
