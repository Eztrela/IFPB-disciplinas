let numeros = [1, 3, 5, 6, 7, 4, 10, 20, 0]
const total = numeros.reduce((soma, numero) => soma + numero)
console.log(total)

let alunos = [
    {
      "idade": 20,
    },
    {
      "idade": 33,
    },
    {
      "idade": 18,
    },
    {
      "idade": 40,
    },
    {
      "idade": 25,
    },  
  ];

let total_idade = alunos.reduce((soma,aluno) => soma+aluno.idade,0);
console.log(total_idade)
