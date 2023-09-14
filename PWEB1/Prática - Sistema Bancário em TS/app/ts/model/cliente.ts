class Cliente {

    private _nome: string;
    private _cpf: string;
    private _conta: Conta;

    constructor(nome:string, cpf:string,numeroConta:string){
        this._nome = nome;
        this._cpf = cpf;
        this._conta = new Conta(numeroConta);
    }

    get nome(){
        return this._nome;
    }

    set nome(nome:string){
        this._nome = nome;
    }

    get cpf(){
        return this._cpf;
    }

    get conta(){
        return this._conta;
    }
}