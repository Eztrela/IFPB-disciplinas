public class Main {
    public static void main(String[] args) {
        Motor motor = new Motor("Zetec", 1.0);
        Motorista motorista = new Motorista("1111");
        Carro carro1 = new Carro("AAA1234", motor, motorista);
        System.out.println(carro1);
        carro1.getMotor().setPotencia(1.4);
        System.out.println(carro1.getMotor().getPotencia());
        Carro carro2 = new Carro("XYZ2000", new Motor("fire",1.6), carro1.getMotorista());
        carro1.getMotorista().setCnh("3333");
        System.out.println(carro2.getMotorista().getCnh());
        carro1.setMotorista(null);
        carro2.setMotorista(null);
        carro1.setMotorista(new Motorista("4444"));
        carro2.setMotorista(new Motorista("5555"));
        System.out.println(carro1.getMotorista());
        System.out.println(carro2.getMotorista());
    }
}
