class Poupanca extends Conta {
    constructor(numero, saldo, dataAniversario) {
        super(numero, saldo);
        this.dataAniversario = dataAniversario;
    }

    creditar(){
        super.creditar(valor*(1.05));
    }

    juros(data){
        if (this.dataAniversario === data){
            this.creditar();
        }
    }
}