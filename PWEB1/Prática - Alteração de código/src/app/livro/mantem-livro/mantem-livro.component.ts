import { Component } from '@angular/core';
import {Livro} from '../../shared/modelo/livro';
import {LIVROS} from '../../shared/modelo/LIVROS';
import {ActivatedRoute, Router} from '@angular/router';

@Component({
  selector: 'app-mantem-livro',
  templateUrl: './mantem-livro.component.html',
  styleUrls: ['./mantem-livro.component.css']
})
export class MantemLivroComponent {
  livroDeManutencao: Livro;
  estahCadastrando = true;
  nomeBotaoManutencao = 'Cadastrar';

  livros = LIVROS;
  constructor(private rotaAtual: ActivatedRoute, private roteador: Router) {
    this.livroDeManutencao = new Livro('', 0, '');
    const idParaEdicao = this.rotaAtual.snapshot.paramMap.get('id');
    if (idParaEdicao) {
      // editando
      const livroEncontrado = this.livros.find(
        livro => livro.isbn === idParaEdicao);
      if (livroEncontrado) {
        this.estahCadastrando = false;
        this.nomeBotaoManutencao = 'Salvar';
        this.livroDeManutencao = livroEncontrado;
      }
    } else {
      this.nomeBotaoManutencao = 'Cadastrar';
    }
  }

  manter(): void {
    if (this.estahCadastrando && this.livroDeManutencao) {
      this.livros.push(this.livroDeManutencao);
    }
    this.livroDeManutencao = new Livro('',0,'');
    this.nomeBotaoManutencao = 'Cadastrar';
    this.roteador.navigate(['listagemlivros']);
  }
}
