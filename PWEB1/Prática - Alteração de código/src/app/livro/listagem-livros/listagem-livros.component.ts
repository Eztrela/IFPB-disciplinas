import { Component } from '@angular/core';
import {Livro} from '../../shared/modelo/livro';
import { LIVROS } from 'src/app/shared/modelo/LIVROS';

@Component({
  selector: 'app-listagem-livros',
  templateUrl: './listagem-livros.component.html',
  styleUrls: ['./listagem-livros.component.css']
})
export class ListagemLivrosComponent {
  livros = LIVROS;
  excluir(livroARemover: Livro): void {
    const indx = this.livros.findIndex(livro =>
      livro.isbn === livroARemover.isbn);

    this.livros.splice(indx, 1);
  }

}
