public class Motorista {
    private String cnh;

    public Motorista(String cnh) {
        this.cnh = cnh;
    }

    public void setCnh(String cnh) {
        this.cnh = cnh;
    }

    public String getCnh() {
        return cnh;
    }

    @Override
    public String toString() {
        return "Motorista{" +
                "cnh='" + cnh + '\'' +
                '}';
    }
}
