#01. Exibir, para todos os produtos, código, nome com o cabeçalho "Produto", quantidade em estoque com o cabeçalho "Estoque Real" e estoque mínimo com o cabeçalho "Estoque Mínimo".
SELECT idproduto, nome AS 'Produto', quantest AS 'Estoque Real', estmin AS 'Estoque Mínimo'
FROM Produto;

#02. Exibir, para todos os produtos, o código, o nome, o preço de venda e uma coluna adicional informando um aumento de 25% sobre o preço de venda. Dê um nome a esta coluna.
SELECT idproduto, nome, venda, venda * 1.25 AS 'Venda com aumento' 
FROM Produto;

#03. Exibir as cidades onde residem os funcionários. Elimine a repetição de linhas.
SELECT DISTINCT idreside 
FROM Funcionario;

#04. Exibir código, nome, tipo, preço de custo e preço de venda de todos os produtos ordenados pelo tipo em ordem descendente e pelo nome em ordem ascendente.
SELECT idproduto, nome, idtipo, custo, venda 
FROM Produto 
ORDER BY idtipo DESC, nome;

#05. Exibir o nome e o setor dos funcionários que nasceram nas cidades com código 7, 8 e 15, ordenados pelo setor e nome do funcionário.
SELECT nome, idsetor 
FROM Funcionario 
WHERE idnatural IN (7,8,15) 
ORDER BY idsetor, nome;

#06. Exibir todos os produtos cujo tipo seja 1, 2 ou 3 e o preço de venda esteja entre R$ 10,00 e R$ 50,00.
SELECT * 
FROM Produto 
WHERE idtipo IN (1,2,3) AND venda BETWEEN 10 AND 50;

#07. Exibir todos os dados dos funcionários que não têm e-mail, mas possuam celular.
SELECT * 
FROM Funcionario 
WHERE email IS NULL and celular IS NOT NULL;

#08. Exibir o nome e o salário dos funcionários homens, casados e com salário menor ou igual a R$ 3.000,00, ordenados pelo salário em ordem descendente.
SELECT nome, salario 
FROM Funcionario 
WHERE sexo = 'M' AND estcivil = 'C' AND salario <= 3000
ORDER BY salario DESC;

#09. Exibir o nome e o preço de venda dos produtos cuja descrição contenha a palavra "chocolate" com preço de venda maior ou igual a R$ 15,00, ordenados pelo preço de venda em ordem descendente. 
SELECT nome, venda 
FROM Produto 
WHERE descricao LIKE '%CHOCOLATE%' AND venda >= 15 
ORDER BY venda DESC;

#10. Exibir o código e o nome dos funcionários homens, exceto aqueles cujos nomes iniciam pela letra A, ordenados pelo nome em ordem ascendente.
SELECT idfuncionario, nome 
FROM Funcionario 
WHERE sexo='M' AND nome NOT LIKE 'A%' 
ORDER BY nome;

#11. Exibir quantos clientes fizeram pedido na empresa.
SELECT COUNT(DISTINCT idcliente) 
FROM Pedido; 

#12. Exibir a soma do valor do frete de todos os pedidos atendidos por via marítima.
SELECT SUM(frete)
FROM Pedido 
WHERE via='M';

#13. Exibir a média de salário dos vendedores (funções 10 e 11) que não sejam casados.
SELECT AVG(salario) 
FROM Funcionario 
WHERE idfuncao IN (10,11) AND estcivil <> 'C';

#14. Exibir a data de nascimento da funcionária mais velha.
SELECT MIN(datanasc) 
FROM Funcionario 
WHERE sexo='F';

#15. Exibir qual a quantidade mais vendida de um produto para cada pedido. 
SELECT idpedido, MAX(quant) AS 'Qtd.Máxima' 
FROM Itens 
GROUP BY idpedido;

#16. Exibir quantos homens e quantas mulheres funcionários nasceram em cada cidade.
SELECT idnatural, sexo, COUNT(*) AS 'Quantidade'
FROM Funcionario 
GROUP BY sexo, idnatural; 

#17. Exibir o total de salários de cada setor da empresa que tenha este total > R$ 5.000,00.
SELECT idsetor, SUM(salario) AS 'Total' 
FROM Funcionario 
GROUP BY idsetor 
HAVING SUM(salario) > 5000;

#18. Exibir o código do cliente e a quantidade de pedidos realizados por cada um em cada ano, apenas para os anos em que foram realizados mais de 5 pedidos.
SELECT idcliente, YEAR(datapedid) AS 'Ano', COUNT(*) AS 'Quantidade'
FROM Pedido 
GROUP BY YEAR(datapedid), idcliente 
HAVING COUNT(*) > 5;

#19. Obter todos os funcionários, mostrando código, nome, código da função, nome da função e gratificação da função.
SELECT F1.idfuncionario AS 'Código do Funcionário', 
	   F1.nome AS 'Nome do Funcionário', 
       F1.idfuncao AS 'Código da função', 
       F2.nome AS 'Nome da Função', 
       F2.gratific AS 'Gratificação' 
FROM Funcionario F1
JOIN Funcao F2
ON F1.idfuncao = F2.idfuncao;

#20. Obter o código e o nome dos clientes que moram na cidade de nome "London".
SELECT Cli.idcliente, Cli.nome
FROM Cliente Cli
JOIN Cidade Cid
ON Cli.idcidade = Cid.idcidade
WHERE Cid.nome = 'London';