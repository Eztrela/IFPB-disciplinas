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
const pessoa1 = new Pessoa('Matheus', 18, '2005/01/29');
// console.log(`${pessoa1}`)
console.log(`Nome da Pessoa 1: ${pessoa1.nome}`);
console.log(`idade da Pessoa 1: ${pessoa1.idade}`);
console.log(`Data de Nascimento da Pessoa 1: ${pessoa1.dataNascimento.toISOString().split('T')[0]}`);
const pessoa2 = new PessoaFisica('Juan', 18, '2004/11/29', '1234');
// console.log(`${pessoa2}`)
console.log(`Nome da Pessoa 2: ${pessoa2.nome}`);
console.log(`idade da Pessoa 2: ${pessoa2.idade}`);
console.log(`Data de Nascimento da Pessoa 2: ${pessoa2.dataNascimento.toISOString().split('T')[0]}`);
console.log(`Cpf da Pessoa 2: ${pessoa2.cpf}`);
const pessoa3 = new PessoaJuridica('Marcela', 19, '2004/11/27', '1235');
// console.log(`${pessoa3}`)
console.log(`Nome da Pessoa 3: ${pessoa3.nome}`);
console.log(`idade da Pessoa 3: ${pessoa3.idade}`);
console.log(`Data de Nascimento da Pessoa 3: ${pessoa3.dataNascimento.toISOString().split('T')[0]}`);
console.log(`Cnpj da Pessoa 3: ${pessoa3.cnpj}`);
