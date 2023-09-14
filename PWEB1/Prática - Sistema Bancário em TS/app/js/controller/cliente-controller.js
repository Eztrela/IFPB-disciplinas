class ClienteController {
    constructor() {
        this.inputNome =
            document.querySelector("#nome");
        this.inputCpf =
            document.querySelector("#cpf");
        this.clientes = new Clientes();
    }
    inserir(evento) {
        evento.preventDefault();
        let novoCliente = new Cliente(this.inputNome.value, this.inputCpf.value, this.gerarNumConta().toString());
        this.clientes.inserir(novoCliente);
        this.inserirContaNoHTML(novoCliente);
    }
    listar() {
        this.clientes.listar().forEach(cliente => {
            this.inserirContaNoHTML(cliente);
        });
    }
    inserirContaNoHTML(cliente) {
        const elementoP = document.createElement('p');
        elementoP.textContent = cliente.toString();
        const botaoApagar = document.createElement('button');
        botaoApagar.textContent = 'X';
        botaoApagar.addEventListener('click', (event) => {
            console.log('removendo cliente ' + cliente.toString());
            this.clientes.remover(cliente.cpf);
            event.target.parentElement.remove();
        });
        elementoP.appendChild(botaoApagar);
        document.body.appendChild(elementoP);
    }
    gerarNumConta() {
        return this.clientes.listar().length + 1;
    }
}
