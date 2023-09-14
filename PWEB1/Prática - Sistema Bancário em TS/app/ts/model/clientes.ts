class Clientes {

    private clientes: Array<Cliente>;

    constructor() {
        this.clientes = new Array<Cliente>();
        const c1 = new Cliente('Pablo','1234',this.gerarNumConta().toString());
        const c2 = new Cliente('Matheus','1235',this.gerarNumConta().toString());
        this.clientes.push(c1, c2);
    }

    inserir(cliente: Cliente): void {
        this.clientes.push(cliente);
    }

    remover(cpf: string): void {
        const clienteARemover = this.pesquisar(cpf);
        if (clienteARemover) {
            const indiceCliente = this.clientes.indexOf(clienteARemover);
            if (indiceCliente > -1) {
                this.clientes.splice(indiceCliente, 1);
            }
        }
    }

    pesquisar(cpf: string): Cliente {
        return this.clientes.find(
            cliente => cliente.cpf === cpf
        );
    }

    listar(): Array<Cliente> {
        return this.clientes;
    }

    gerarNumConta(): number{
        return Number(this.clientes[-1].conta.numero) + 1;
    }

}
