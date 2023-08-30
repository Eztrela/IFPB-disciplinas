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
  remover(codigo) {
    const listaDisciplinasElemento = document.querySelector('#listaDisciplinas')
    const disciplinaRemover = this.servico.remover(Number(codigo));
    if (disciplinaRemover) {
      this.removerDisciplinaNoHtml(listaDisciplinasElemento);
    }
  }

  inserirDisciplinaNoHtml(disciplina, elementoDestino) {
    let codigo = disciplina.codigo;
    let nome = disciplina.nome;
    let alunos = disciplina.alunosMatriculados;
    let elementoDisciplina = `<li id='${codigo}'>
      <p>
        Código: ${codigo} - Nome: ${nome} - Alunos: ${alunos}
      </p>
      <button id='${codigo}'onclick='controladorDisciplina.remover(this.id)'>X</button>
      </li>`;
    elementoDestino.innerHTML += elementoDisciplina;
  }

  removerDisciplinaNoHtml(elementoDestino) {
    elementoDestino.innerHTML = ''
    let disciplinas = this.servico.listar();
    if (disciplinas.length > 0) {
      disciplinas.forEach(d => {
        let codigo = d.codigo;
        let nome = d.nome;
        let alunos = d.alunosMatriculados;
        let elementoDisciplina = `<li id='${codigo}'>
          <p>
            Código: ${codigo} - Nome: ${nome} - Alunos: ${alunos}
          </p>
          <button id='${codigo}'onclick='controladorDisciplina.remover(this.id)'>X</button>
          </li>`;
        elementoDestino.innerHTML += elementoDisciplina;
      });
    }
  }
}
