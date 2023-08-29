class DisciplinaService {
  constructor() {
    this.repositorio = new DisciplinaRepositorio()
  }

  inserir(codigo, nome) {
    const disciplinaPesquisada = this.pesquisarPorCodigo(codigo)
    if (disciplinaPesquisada.length > 0) {
      throw new Error('Disciplina já cadastrado!')
    }
    const DisciplinaNova = new Disciplina(codigo, nome)
    this.repositorio.inserir(DisciplinaNova)
    return DisciplinaNova
  }

  pesquisarPorCodigo(codigo) {
    return this.repositorio
      .listar()
      .filter(disciplina => disciplina.codigo === codigo)
  }

  remover(codigo) {
    this.repositorio.remover(codigo)
  }

  inserirAlunoNaDisciplina(aluno, codigo) {
    disciplina = this.pesquisarPorCodigo(codigo)
    if (disciplinaPesquisada.length < 0) {
      throw new Error('Disciplina não encontrada')
    }
    disciplinaPesquisada[0].matricularAluno(aluno)
  }
}
