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
    const disciplinaPesquisada = this.pesquisarPorCodigo(codigo)
    this.repositorio.remover(codigo)
    return true
  }

  inserirAlunoNaDisciplina(aluno, codigo) {
    const disciplina = this.pesquisarPorCodigo(codigo)
    if (disciplina.length === 0) {
      throw new Error('Disciplina não encontrada')
    }
    disciplina[0].alunosMatriculados.push(aluno)
  }

  // listar() {
  //   return this.repositorio.listar()
  // }

  atualizar(codigo, novoNome) {
    const disciplina = this.pesquisarPorCodigo(codigo)
    if (disciplina.length === 0) {
      throw new Error('Disciplina não encontrada')
    }
    disciplina[0].nome = novoNome
  }
}
