class PessoaFisica extends Pessoa {

    readonly _cpf: string;

    constructor(nome: string, idade: number, dataNascimento: string, cpf: string) {
        super(nome + '-Física', idade, dataNascimento);
        this._cpf = cpf;
    }

    get cpf(): string {
        return this._cpf;
    }
}
