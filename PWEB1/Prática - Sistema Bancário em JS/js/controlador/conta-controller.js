class ContaController {
  constructor() {
    this.repositorioContas = new RepositorioContas()
  }

  adicionarConta(conta) {
    this.repositorioContas.adicionar(conta)
  }

  listar() {
    this.repositorioContas.getContas().forEach(conta => {
      if (conta instanceof Poupanca) {
        this.inserirContaNoHTML(conta, 'Poupanca')
      } else if (conta instanceof ContaBonificada) {
        this.inserirContaNoHTML(conta, 'Conta Bonificada')
      } else {
        this.inserirContaNoHTML(conta, 'Conta')
      }
    })
  }

  inserir(evento) {
    evento.preventDefault()
    const elementoNumero = document.querySelector('#numero')
    const elementoSaldo = document.querySelector('#saldo')
    const elementoDataAniversario = document.querySelector('#dataAniversario')
    const tipoConta = document.querySelector('#tiposConta').value
    // switch(tipoConta){
    //     case 'Conta':
    //         var conta = new Conta(elementoNumero.value,
    //             Number(elementoSaldo.value));
    //     case 'Conta Bonificada':
    //         var conta = new ContaBonificada(elementoNumero.value,
    //             Number(elementoSaldo.value));
    //     case 'Poupanca':
    //         var conta = new Poupanca(elementoNumero.value,
    //             Number(elementoSaldo.value), elementoDataAniversario.value);

    // }
    let conta
    if (tipoConta === 'Conta') {
      conta = new Conta(elementoNumero.value, Number(elementoSaldo.value))
    } else if (tipoConta === 'Conta Bonificada') {
      conta = new Conta(elementoNumero.value, Number(elementoSaldo.value))
    } else if (tipoConta === 'Poupanca') {
      conta = new Poupanca(
        elementoNumero.value,
        Number(elementoSaldo.value),
        elementoDataAniversario.value
      )
    }

    this.repositorioContas.adicionar(conta)
    this.inserirContaNoHTML(conta, tipoConta)
  }

  inserirContaNoHTML(conta, tipoConta) {
    const elementoP = document.createElement('p')
    if (tipoConta === 'Poupanca') {
      elementoP.textContent =
        'Conta ' +
        conta.numero +
        ': ' +
        conta.saldo +
        ' Data Aniversário: ' +
        conta.dataAniversario +
        ' Tipo de Conta: ' +
        tipoConta
    } else if (tipoConta === 'Conta Bonificada') {
      elementoP.textContent =
        'Conta ' +
        conta.numero +
        ': ' +
        conta.saldo +
        ' Tipo de Conta: ' +
        tipoConta
    } else if (tipoConta === 'Conta') {
      elementoP.textContent =
        'Conta ' +
        conta.numero +
        ': ' +
        conta.saldo +
        ' Tipo de Conta: ' +
        tipoConta
    }
    const botaoApagar = document.createElement('button')
    botaoApagar.textContent = 'X'

    botaoApagar.addEventListener('click', event => {
      this.repositorioContas.remover(conta.numero)
      event.target.parentElement.remove()
    })

    elementoP.appendChild(botaoApagar)
    document.body.appendChild(elementoP)
  }
}
