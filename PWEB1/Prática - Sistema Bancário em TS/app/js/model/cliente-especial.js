class ClienteEspecial extends Cliente {
    constructor(nome, cpf) {
        super(nome, cpf);
        this._dependentes = [];
    }
    get dependentes() {
        return this._dependentes;
    }
}
