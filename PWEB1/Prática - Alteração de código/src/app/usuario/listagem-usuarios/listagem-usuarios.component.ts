import { Component } from '@angular/core';
import {Usuario} from '../../shared/modelo/usuario';
import {USUARIOS} from '../../shared/modelo/USUARIOS';

@Component({
  selector: 'app-listagem-usuarios',
  templateUrl: './listagem-usuarios.component.html',
  styleUrls: ['./listagem-usuarios.component.css']
})
export class ListagemUsuariosComponent {

  usuarios = USUARIOS;
  excluir(usuarioARemover: Usuario): void {
    const indx = this.usuarios.findIndex(usuario =>
      usuario.cpf === usuarioARemover.cpf);

    this.usuarios.splice(indx, 1);
  }

}
