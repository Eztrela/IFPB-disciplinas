class PessoaJuridica extends Pessoa {
    constructor(nome, idade, dataNascimento, cnpj) {
        super(nome + '-Jurídica', idade, dataNascimento);
        this._cnpj = cnpj;
    }
    get cpf() {
        return this._cnpj;
    }
}
