class DisciplinaRepositorio {

    constructor() {
        this._disciplinas = [];
    }

    inserir(disciplina) {
        this._disciplinas.push(disciplina);
    }

    remover(codigo) {
        const indxDisciplinaARemover = this._disciplinas.findIndex(disciplina => Number(disciplina.codigo) === codigo);
        if (indxDisciplinaARemover > -1) {
            this._disciplinas.splice(indxDisciplinaARemover, 1);
        }
    }

    listar() {
        return this._disciplinas;
    }

    atualizar(codigo, novoNome) {
        const indxDisciplinaAAtualizar = this._disciplinas.findIndex(disciplina => disciplina.codigo === codigo);
        if (indxDisciplinaAAtualizar > -1) {
            this._disciplinas[indxDisciplinaAAtualizar].nome = novoNome;
        }
    }
    
}
