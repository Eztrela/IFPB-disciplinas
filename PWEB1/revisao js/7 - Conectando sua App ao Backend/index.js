let resposta = {
    "usuarios": [
      {
        "id": 1,
        "nome": "Usuário 1",
        "login": "u1"
      },
      {
        "id": 2,
        "nome": "Usuário 2",
        "login": "u2"
      },
      {
        "id": 3,
        "nome": "Usuário 3",
        "login": "u3"
      }
  ],
  "mensagens": [
    {"id":1,
    "texto": "teste1"},
    {"id":2,
    "texto": "teste2"},
    {"id":3,
    "texto": "teste3"},
  ]
  }
  
for (let usuario of resposta.usuarios) {
console.log(usuario.login);
}
resposta.mensagens.forEach(mensagem=>console.log(mensagem.texto))

  