class Pessoa {

    protected _nome: string;
    private _idade: number;
    private _dataNascimento: Date;

    constructor(nome: string, idade:number, dataNascimento: string) {
        this._nome = nome;
        this._idade = idade;
        this._dataNascimento = new Date(dataNascimento);

    }

    get nome() {
        return this._nome;
    }

    set nome(nome) {
        this._nome = nome;
    }

    get idade() {
        return this._idade;
    }

    set idade(idade) {
        this._idade = idade;
    }

    toString(): string {
        return `Nome: ${this._nome}
Idade: ${this._idade}
Data de Nascimento: ${this._dataNascimento.toISOString().split('T')[0]}`;
    }
}
