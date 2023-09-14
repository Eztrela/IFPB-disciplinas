class Cliente {
    constructor(nome, cpf, numeroConta) {
        this._nome = nome;
        this._cpf = cpf;
        this._conta = new Conta(numeroConta);
    }
    get nome() {
        return this._nome;
    }
    set nome(nome) {
        this._nome = nome;
    }
    get cpf() {
        return this._cpf;
    }
    get conta() {
        return this._conta;
    }
}
