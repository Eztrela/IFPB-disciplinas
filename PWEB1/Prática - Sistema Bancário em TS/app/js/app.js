let clienteController = new ClienteController();
const cliente1 = new Cliente('Isla', '1236', clienteController.gerarNumConta().toString());
const cliente2 = new Cliente('Juan', '1237', clienteController.gerarNumConta().toString());
// clienteController.inserir(cliente1);
console.log('Cliente: ' + cliente1.nome);
// p1.atualizarSaldoAniversario();
// console.log('Poupanca: ' + p1.saldo);
// cb1.creditar(100);
// console.log('Conta Bonificada: ' + cb1.saldo);
