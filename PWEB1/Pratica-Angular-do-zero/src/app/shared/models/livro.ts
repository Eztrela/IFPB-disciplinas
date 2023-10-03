export class Livro{
    private _isbn: string;
    private _titulo: string;
    private _autores: Array<string>;
    private _edicao: number;
    private _disponibilidade: boolean;
    constructor(isbn: string, _titulo: string, edicao: number){
        this._isbn = isbn;
        this._titulo = _titulo;
        this._edicao = edicao;
        this._autores = [];
        this._disponibilidade = true;
    }

	get isbn(): string {
		return this._isbn;
	}

    get titulo(): string {
		return this._titulo;
	}

    get autores(): Array<string> {
		return this._autores;
	}

    get disponibilidade(): boolean {
		return this._disponibilidade;
	}

    set disponibilidade(disponibilidade: boolean) {
		this._disponibilidade = disponibilidade;
	}

    get edicao(): number {
		return this._edicao;
	}

    set edicao(value: number) {
		this._edicao = value;
	}

}