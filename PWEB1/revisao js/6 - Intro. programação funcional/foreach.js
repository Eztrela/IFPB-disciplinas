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
  
  console.log("for tradicional");
  for (let i=0; i < alunos.length; i++) {
    console.log(alunos[i].idade);
  }
  
  console.log("foreach");
  alunos.forEach(aluno => console.log(aluno.matricula));