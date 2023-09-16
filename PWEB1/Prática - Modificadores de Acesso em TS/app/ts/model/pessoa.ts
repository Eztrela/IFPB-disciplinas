class Pessoa {

    protected _nome: string;
    private _idade: number;
    private _dataNascimento: Date;

    constructor(nome: string, idade: number, dataNascimento: string) {
        this._nome = nome;
        this._idade = idade;
        this._dataNascimento = new Date(dataNascimento);

    }

    get nome(): string {
        return this._nome;
    }

    set nome(nome: string) {
        this._nome = nome;
    }

    get idade(): number {
        return this._idade;
    }

    set idade(idade: number) {
        this._idade = idade;
    }

    get dataNascimento(): Date {
        return this._dataNascimento;
    }

    set dataNascimento(dataNascimento: Date) {
        this._dataNascimento = dataNascimento;
    }

    toString(): string {
        return `Nome: ${this._nome}
Idade: ${this._idade}
Data de Nascimento: ${this._dataNascimento.toISOString().split('T')[0]}`;
    }
}
