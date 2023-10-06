import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {MantemUsuarioComponent} from './usuario/mantem-usuario/mantem-usuario.component';
import {ListagemUsuariosComponent} from './usuario/listagem-usuarios/listagem-usuarios.component';
import {ListagemLivrosComponent} from './livro/listagem-livros/listagem-livros.component';
import {MantemLivroComponent} from './livro/mantem-livro/mantem-livro.component';
import {UpdateLivroComponent} from './livro/update-livro/update-livro.component';

const routes: Routes = [
  {
    path: 'cadastrousuario',
    component: MantemUsuarioComponent
  },
  {
    path: 'editausuario/:id',
    component: MantemUsuarioComponent
  },
  {
    path: 'listagemusuarios',
    component: ListagemUsuariosComponent
  },
  {
    path: 'listagemlivros',
    component: ListagemLivrosComponent
  },
  {
    path: 'editalivro/:id',
    component: UpdateLivroComponent
  },
  {
    path: 'cadastrolivro',
    component: MantemLivroComponent
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
