let clienteController = new ClienteController();
let contaController = new ContaController();

contaController.listar();

const c1 = new Conta('1', 100);
const p1 = new Poupanca('2', 100);
const cb1 = new ContaBonificada('3', 0);

console.log('Conta: ' + c1.saldo);

p1.atualizarSaldoAniversario();
console.log('Poupanca: ' + p1.saldo);

cb1.creditar(100);
console.log('Conta Bonificada: ' + cb1.saldo);

console.log('============================');


const cliente1 = new Cliente('Pablo','1234');
const cliente2 = new Cliente('Yago','1235');

console.log('Cliente1: '+cliente1);
console.log('Cliente1: '+cliente2);

clienteController.inserirClienteNoHTML(cliente1)
clienteController.inserirClienteNoHTML(cliente2)

const clienteE1 = new ClienteEspecial('Matheus','1236');

clienteController.inserirClienteNoHTML(clienteE1)
console.log('Cliente Especial 1: '+clienteE1);

let listaDeClientes = new Clientes();

listaDeClientes.inserir(cliente1)
listaDeClientes.inserir(clienteE1)

console.log(listaDeClientes.listar())