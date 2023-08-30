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
      this.inserirNoHtml(disciplinaInserida, listaDisciplinasElemento)
    }
  }
  remover(codigo) {
    const listaDisciplinasElemento = document.querySelector('#listaDisciplinas')
    console.log(typeof (codigo))
    const disciplinaRemover = this.servico.remover(Number(codigo));
    if (disciplinaRemover) {
      this.carregarNoHtml(listaDisciplinasElemento);
    }
  }

  inserirNoHtml(disciplina, elementoDestino) {
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

  carregarNoHtml(elementoDestino) {
    // const disciplinaElemento = document.createElement('li')
    // let disciplinaElemento = documento.querySelector('#disciplinaContainer')
    // let disciplinaElemento = document.createElement('div')
    // disciplinaElemento.innerHTML = `<div class="container" id="disciplinasContainer">
    // </div>`;
    elementoDestino.innerHTML = ''
    let disciplinas = this.servico.listar();
    console.log(disciplinas.length)
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

    // disciplinaElemento.textContent = `Código: ${disciplina.codigo} - Nome: ${disciplina.nome} `
    // const botaoExcluir = document.createElement('button')
    // botaoExcluir.textContent = 'X'
    // disciplinaElemento.appendChild(botaoExcluir)
    // botaoExcluir.addEventListener('click')
    // elementoDestino.appendChild(disciplinaElemento)
  }
}
