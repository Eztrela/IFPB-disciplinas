class DisciplinaControlador {
  constructor() {
    this.servico = new DisciplinaService()
  }

  inserir() {
    const codigoElemento = document.querySelector('#codigo')
    const nomeElemento = document.querySelector('#nome')
    const disciplinaInserida = this.servico.inserir(
      Number(codigoElemento.value),
      nomeElemento.value
    )
    const listaDisciplinasElemento = document.querySelector('#listaDisciplinas')
    if (disciplinaInserida) {
      this.inserirDisciplinaNoHtml(disciplinaInserida, listaDisciplinasElemento)
    }
  }
  remover(codigo) {
    codigo = codigo.split('-')[1]
    const disciplinaRemovida = this.servico.remover(Number(codigo))
    if (disciplinaRemovida) {
      this.removerDisciplinaDoHtml(codigo)
    }
  }

  inserirDisciplinaNoHtml(disciplina, elementoDestino) {
    const elementoDisciplina = document.createElement('li')
    const codigo = disciplina.codigo
    elementoDisciplina.setAttribute('id', `disciplina-${codigo}`)

    const disciplinaText = document.createElement('p')
    disciplinaText.textContent = `${disciplina}`
    elementoDisciplina.appendChild(disciplinaText)

    const disciplinaCloseButton = document.createElement('button')
    disciplinaCloseButton.textContent = 'X'
    disciplinaCloseButton.setAttribute('id', `remover-${codigo}`)
    disciplinaCloseButton.addEventListener('click', click => {
      const codigo = click.target.id
      this.remover(codigo)
    })
    elementoDisciplina.appendChild(disciplinaCloseButton)
    elementoDestino.appendChild(elementoDisciplina)
  }

  removerDisciplinaDoHtml(codigo) {
    const disciplinaARemover = document.querySelector(`#disciplina-${codigo}`)
    disciplinaARemover.remove()
  }
}
