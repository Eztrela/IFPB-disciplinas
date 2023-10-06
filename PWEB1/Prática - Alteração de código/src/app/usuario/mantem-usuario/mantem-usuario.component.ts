import { Component } from '@angular/core';
import {Usuario} from '../../shared/modelo/usuario';
import {USUARIOS} from '../../shared/modelo/USUARIOS';
import {ActivatedRoute, Router} from '@angular/router';

@Component({
  selector: 'app-mantem-usuario',
  templateUrl: './mantem-usuario.component.html',
  styleUrls: ['./mantem-usuario.component.css']
})
export class MantemUsuarioComponent {

  usuarioDeManutencao: Usuario;
  estahCadastrando = true;
  nomeBotaoManutencao = 'Cadastrar';

  usuarios = USUARIOS;
  constructor(private rotaAtual: ActivatedRoute, private roteador: Router) {
    this.usuarioDeManutencao = new Usuario('', 0);
    const idParaEdicao = this.rotaAtual.snapshot.paramMap.get('id');
    if (idParaEdicao) {
      // editando
      const usuarioEncontrado = this.usuarios.find(
        usuario => usuario.cpf === idParaEdicao);
      if (usuarioEncontrado) {
        this.estahCadastrando = false;
        this.nomeBotaoManutencao = 'Salvar';
        this.usuarioDeManutencao = usuarioEncontrado;
      }
    } else {
      this.nomeBotaoManutencao = 'Cadastrar';
    }
  }

  manter(): void {
    if (this.estahCadastrando && this.usuarioDeManutencao) {
      this.usuarios.push(this.usuarioDeManutencao);
    }
    this.usuarioDeManutencao = new Usuario();
    this.nomeBotaoManutencao = 'Cadastrar';
    this.roteador.navigate(['listagemusuarios']);
  }

}
