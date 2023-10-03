import { Component } from '@angular/core';
import {Livro} from './shared/models/livro'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Pratica-Angular-do-zero';
  livros: Array<Livro> = []
  livroAtual: Livro;
  mensagemErro = '';
  pesquisaLivros: Array<Livro> = [];

  constructor(){
    this.livroAtual = new Livro('','',0) 
  }

  cadastrar(): void{
    if(!this.livroJaCadastrado(this.livroAtual.isbn)){
      this.livros.push(this.livroAtual);
      this.livroAtual = new Livro('','',0);
      this.mensagemErro = '';
    }else{
      this.mensagemErro = `ISBN ${this.livroAtual.isbn} já cadastrada`
    }
  }

  remover(livroARemover: Livro): void{
    const indxARemover = this.buscaLivro(livroARemover.titulo);
    if(indxARemover >= 0){
      this.livros.splice(indxARemover,1);
    }
  }

  pesquisar (corteTitulo: string){
    if(corteTitulo.length == 0){
      this.pesquisaLivros = [];
    }
    this.livros.forEach(livro => {
      if (livro.titulo.startsWith(corteTitulo)){
        this.pesquisaLivros.push(livro);
      }
    });
  }

  buscaLivro(tituloLivro: string){
    const indxLivroPesquisado = this.livros.findIndex(livro => livro.titulo === tituloLivro);
    if(indxLivroPesquisado >= 0){
      return indxLivroPesquisado;
    }else{
      return -1;
    }
  }

  livroJaCadastrado(isbn: string){
    const livrosRetornados = this.livros.filter(livro => livro.isbn === isbn);
    return livrosRetornados.length > 0;
  }
}
