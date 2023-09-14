class Clientes {
    constructor() {
        this.clientes = new Array();
        const c1 = new Cliente('Pablo', '1234', this.gerarNumConta().toString());
        const c2 = new Cliente('Matheus', '1235', this.gerarNumConta().toString());
        this.clientes.push(c1, c2);
    }
    inserir(cliente) {
        this.clientes.push(cliente);
    }
    remover(cpf) {
        const clienteARemover = this.pesquisar(cpf);
        if (clienteARemover) {
            const indiceCliente = this.clientes.indexOf(clienteARemover);
            if (indiceCliente > -1) {
                this.clientes.splice(indiceCliente, 1);
            }
        }
    }
    pesquisar(cpf) {
        return this.clientes.find(cliente => cliente.cpf === cpf);
    }
    listar() {
        return this.clientes;
    }
    gerarNumConta() {
        return Number(this.clientes[-1].conta.numero) + 1;
    }
}
