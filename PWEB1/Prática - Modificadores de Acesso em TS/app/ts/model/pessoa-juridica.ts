class PessoaJuridica extends Pessoa {

    readonly _cnpj: string;

    constructor(nome: string, idade: number, dataNascimento: string, cnpj: string) {
        super(nome + '-Jurídica', idade, dataNascimento);
        this._cnpj = cnpj;
    }

    get cnpj(): string {
        return this._cnpj;
    }
}
