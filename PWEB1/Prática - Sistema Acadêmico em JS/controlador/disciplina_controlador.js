class DisciplinaControlador {
  constructor() {
    this.servico = new DisciplinaService()
  }

  inserir() {
    const codigoElemento = document.querySelector('#codigo')
    const nomeElemento = document.querySelector('#nome')
    const disciplinaInserida = this.servico.inserir(
      codigoElemento.value,
      nomeElemento.value
    )
    const listaDisciplinasElemento = document.querySelector('#listaDisciplinas')
    if (disciplinaInserida) {
      this.inserirDisciplinaNoHtml(disciplinaInserida, listaDisciplinasElemento)
    }
  }

  inserirDisciplinaNoHtml(disciplina, elementoDestino) {
    const disciplinaElemento = document.createElement('li')
    disciplinaElemento.textContent = `Código: ${disciplina.codigo} - Nome: ${disciplina.nome}`
    const botaoExcluir = document.createElement('button')
    elementoDestino.appendChild(disciplinaElemento)
  }
}
