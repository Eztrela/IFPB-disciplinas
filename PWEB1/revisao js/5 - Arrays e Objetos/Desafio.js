let alunos = [
    {
      "matricula": "345",
      "nome": "Carlos",
      "idade": 20,
    },
    {
      "matricula": "246",
      "nome": "João",
      "idade": 33,
    },
    {
      "matricula": "156",
      "nome": "Maria",
      "idade": 18,
    },
    {
      "matricula": "543",
      "nome": "José",
      "idade": 40,
    },
    {
      "matricula": "765",
      "nome": "Sebastião",
      "idade": 25,
    },  
  ];

for(let aluno of alunos){
    if (aluno.idade > 30)
        console.log(aluno.nome)
}