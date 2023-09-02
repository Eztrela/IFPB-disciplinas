class Poupanca extends Conta {
  constructor(numero, saldo, dataAniversario) {
    super(numero, saldo)
    this.dataAniversario = dataAniversario
  }

  juros(data) {
    if (this.dataAniversario === data) {
      this.creditar(this.saldo * 0.05)
    }
  }
}
