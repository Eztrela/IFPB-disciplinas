class Disciplina {

    constructor(codigo, nome) {
        this._codigo = codigo;
        this._nome = nome;
        this._alunosMatriculados = [];
    }

    get nome() {
        return this._nome;
    }

    set nome(novoNome) {
        this._nome = novoNome;
    }

    get codigo(){
        return this._codigo;
    }

    set codigo(novoCodigo){
        this._codigo = novoCodigo;
    }

    get alunosMatriculados(){
        return this._alunosMatriculados;
    }

    toString(){
        return `Código: ${this.codigo} - Nome: ${this.nome} - Alunos: ${this.alunosMatriculados}`
    }
}