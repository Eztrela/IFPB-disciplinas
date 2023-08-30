--select * from cliente; 

CREATE TABLE Cliente (
CodCLI Serial PRIMARY KEY,
Nome Varchar(30),
Endereco Varchar(30),
Telefone Varchar(12),
InscE Varchar(10),
CNPJ Varchar(10),
Cidade Varchar(15),
UF Varchar(2)
);

CREATE TABLE Produto (
CodPROD Serial not null,
Descricao Varchar(20),
Valor Numeric(10,2),
Unidade Char(2),
constraint pk_prod primary key(CodPROD));

CREATE TABLE Pedido (
NumPED Serial PRIMARY KEY,
PrazoEntrega Integer,
Data Date,
CodCLI Integer,
CodVEND Integer,
FOREIGN KEY(CodCLI) REFERENCES Cliente (CodCLI)
);

CREATE TABLE Vendedor (
CodVEND Serial PRIMARY KEY,
Nome Varchar(30),
DataNasc Date,
SalarioFixo Numeric(12,2),
FaixaComissao Char(1)
);

CREATE TABLE ItensPedido (
NumPED Integer,
CodPROD Integer,
Quantidade Integer,
constraint pk_itens PRIMARY KEY(CodPROD,NumPED),
constraint fk_prod FOREIGN KEY(CodPROD) REFERENCES Produto (CodPROD),
constraint fk_ped FOREIGN KEY(NumPED) REFERENCES Pedido (NumPED)
);
 

ALTER TABLE Pedido ADD FOREIGN KEY(CodVEND) REFERENCES Vendedor (CodVEND);

insert into cliente values(default,'Claudia Dias',null,null, '564325','786534','Recife','PE');
insert into cliente values(default,'Joaquim Moraes','Epitacio Pessoa, 123','32425643', '500925','789004','Joao Pessoa','PB');
insert into cliente values(default,'Janaina Rodrigues','Rui Carneiro, 342',null, '764325','386534','Joao Pessoa','PB');
insert into cliente values(default,'Maria Portela','Boa Viagem, 345','76435678', null,null,'Recife','PE');
insert into cliente values(default,'Ana Moura','Nego, 321','32465432', '87325','780978','Joao Pessoa','PB');
insert into cliente values(default,'Cassandra Doura',null,null, '786525','79876','Recife','PE');
insert into cliente values(default,'Cicero Novaes',null,null, '123525','432534','Natal','RN');
insert into cliente values(default,'Marcos Araruna','Sergipe,267','43265432', '900325','800534','Joao Pessoa','PB');


insert into vendedor values(default,'Juan Gomes', '1978/07/28', 2300.80,'C');
insert into vendedor values(default,'Joao Peregrino', '1970/05/20', 3300.80,'B');
insert into vendedor values(default,'Carla Gomes', '1984/02/12', 5300.80,'A');
insert into vendedor values(default,'Josefa Cirino', '1990/08/23', 2300.80,'C');
insert into vendedor values(default,'Ariane Dutra', '1993/09/28', 3300.80,'B');


insert into produto values(default,'Queijo', 22.00, 'KG');
insert into produto values(default,'Chocolate', 6.12, 'G');
insert into produto values(default,'Leite', 10.00, 'L');
insert into produto values(default,'Linho', 24.00, 'M');
insert into produto values(default,'Feijao', 12.00, 'KG');
insert into produto values(default,'Açucar', 9.00, 'KG');

insert into pedido values(default,23, '2019/09/12', 1,1);
insert into pedido values(default,10, '2020/09/21', 2,1);
insert into pedido values(default,5, '2020/08/25', 3,4);
insert into pedido values(default,2, '2020/07/28', 4,2);
insert into pedido values(default,3, '2020/09/28', 5,3);
insert into pedido values(default,3, '2020/10/26', 5,2);

insert into itenspedido values(2,2, 35);
insert into itenspedido values(2,3, 30);
insert into itenspedido values(1,1, 10);
insert into itenspedido values(4,5, 35);
insert into itenspedido values(5,4, 10);
insert into itenspedido values(3,4, 35);
insert into itenspedido values(1,5, 10);

-- Aula 04

Select nome
	From cliente
	Where cidade = 'Joao Pessoa';
	
	select * from cliente; 
	select * from pedido; 
	select * from vendedor; 
	
Select nome, UF 
from cliente JOIN pedido 
        on cliente.codcli = pedido.codcli 
where UF in ('PB','PE') and prazoentrega > 15;

-- Operações de conjuntos 

(Select nome
    from cliente
    where cidade like 'Recife')
    UNION
(Select nome
 from vendedor);

select codcli
  from cliente
  where UF = 'PB'
  INTERSECT
select codcli
   from pedido;

select codcli
  from cliente
Except
select codcli
   from pedido;
   
select * from cliente order by codcli; 

select * from pedido order by numped; 

-- produto cartesiano

Select cliente.codcli, nome, numped, pedido.codcli
from cliente, pedido;

Select cliente.codcli, nome, numped, pedido.codcli
from cliente cross JOIN pedido;

-- Joins

Select cliente.codcli, pedido.codcli, nome, numped
from cliente, pedido
where cliente.codcli = pedido.codcli;

Select cliente.codcli, pedido.codcli, nome, numped
from cliente JOIN pedido on cliente.codcli = pedido.codcli;

Select v.nome 
From vendedor v join pedido p 
        on v.codvend =  p.codvend
     join itenspedido i on p.numped = i.numped 
     join produto pr on i.codprod = pr.codprod
Where i.quantidade > 5 and pr.descricao = 'Chocolate'; 

-- Group by 

Select cidade, count(*)
from cliente C join pedido P on C.codcli = P.codcli 
join vendedor V on P.codvend = V.codvend 
Group by cidade;

select cliente.uf, count(*) 
from cliente
group by uf
having count(*) > 2; 

select v.faixacomissao, avg(salariofixo)
from vendedor v
where v.faixacomissao <> 'B'
group by v.faixacomissao
having avg(salariofixo) > 3000; 

select v.faixacomissao, min(salariofixo), max(salariofixo)
from vendedor v
group by v.faixacomissao;


-- BD Pedidos
-- script da aula 05 - subqueries e outros comandos

select * from produto order by codprod; 

Select descricao
From produto
Where unidade IN ('KG', 'L', 'M');

Select round(avg(valor),0)
From produto; 

Select descricao
From produto
Where codprod in 
     (select codprod
	  From itenspedido
      Where quantidade = 10);

select * from vendedor order by codvend; 

select nome
	From vendedor
	Where salariofixo < 
	      (select round(AVG(salariofixo),1)
		   From vendedor);
								 

select * from produto; 

Select  pr.unidade, max(pr.valor) 
From  produto pr
group by pr.unidade; 
		 
Select p.descricao 
From produto p
Where  p.valor > 
    ANY (Select  max(pr.valor) 
         From  produto pr
         group by pr.unidade) ;
		 
-- Teste com ALL

Select p.descricao 
From produto p
Where  p.valor > 
    ALL (Select  max(pr.valor) 
         From  produto pr
         group by pr.unidade) ;

-- Faça a seguinte inserção
insert into produto values (default, 'XXX', 1.2, 'KG');

select * from produto order by codprod; 

select p.descricao
	From produto P
	Where not exists 
	(select *
     From itenspedido i
	 Where i.codprod = P.codprod);

Select p.descricao
From produto p 
Where p.codprod in  
     (select i.codprod
	  From itenspedido i
	  Where i.quantidade = 10);

Select p.descricao
From produto p 
Where p.codprod in  
     (select i.codprod
	  From itenspedido i);
	  
Select p.descricao
From produto p 
Where p.codprod not in  
     (select i.codprod
	  From itenspedido i);
	  
select p.descricao
	From produto P
	Where exists 
	(select *
     From itenspedido i
	 Where i.codprod = P.codprod);


-- Outras subqueries

Select distinct 
   (Select COUNT(*) from cliente where cidade like 'João Pessoa') AS "Quantidade de Pessoenses", 
   (Select COUNT(*) from cliente where cidade like 'Recife') AS "Quantidade de Recifenses"
  From cliente;
  
insert into cliente (codcli,nome) 
          (select codvend + 10, nome
          from vendedor
          where faixacomissao like 'A');
		  
select * from cliente order by codcli; 
select * from vendedor order by codvend; 

Update produto
Set valor = valor*1.025
Where valor < (select avg(valor) 
			   From produto
			   Where unidade = 'KG');
			   
select * from produto order by unidade; 

--Inserir antes do delete

insert into pedido values(100,10,'12/10/2020',4,null);

select * from pedido; 

delete from pedido P
where not exists (select nome
     		    from vendedor v
     		    where v.codvend = P.codvend);

Select p.data 
from pedido p
where p.numped in 
       (select i.numped 
        from itenspedido i
        where i.codprod in 
               (select pr.codprod 
                from produto pr
                where descricao like 'Chocolate'));

-- Create table as

CREATE TABLE pedidoVendedor AS 
select p.numped, v.nome
from pedido p join vendedor v on p.codvend = v.codvend
where data < '12/12/2020'; 

Select * from pedidoVendedor;

insert into pedidoVendedor values(201, 'Bruno Assis');

create table vendedor1 as 
     select * from vendedor where 1=2;
select * from vendedor1;

-- AntiJOINs

SELECT c.nome, c.codcli 
FROM cliente c
WHERE c.codcli NOT IN 
		(SELECT p.codcli 
		 FROM pedido p) 
ORDER BY c.nome;

Select c.nome, c.codcli
from cliente c left join pedido p on c.codcli = p.codcli
where p.codcli is null
Order by c.nome;

Select c.nome, c.codcli as cliente, p.codcli as ClienteemPedido, numped
from cliente c left join pedido p on c.codcli = p.codcli
Order by c.nome;


-- Aula 06 - Views

select * from produto order by codprod; 

-- View Prquilo

CREATE  or replace VIEW Prquilo 
     (codigo, descricao,unidade) 
       AS Select codprod,descricao,unidade
	  From produto
	  Where unidade = 'KG';

Select * from Prquilo;
Select * from Prquilo order by codigo; 
Select descricao from prquilo order by descricao;

-- View VendSal

CREATE OR REPLACE VIEW VendSal(codigo,nome,salario)
           AS Select codvend,nome,salariofixo
	          From vendedor; 

Select * from VendSal;
Select nome from vendSal order by nome;

-- Prquilo e tabela produto

Select * from prquilo order by codigo;
Select * from produto order by codprod;

Insert into PRquilo 
values (110,'Arroz','KG');

Select * from prquilo order by codigo;
Select * from produto order by codprod;

Delete from PRquilo 
where descricao = 'Arroz Integral';

-- View Listapedidos

CREATE or replace VIEW Listapedidos AS
   Select nome, descricao
   From vendedor v join pedido p on v.codvend = p.codvend 
   Join itenspedido i on p.numped = i.numped 
   join produto pr on i.codprod = pr.codprod
   order by nome;
   
Select * from listapedidos order by nome;

-- View totalSalarios

Create or replace view totalsalarios as
    select sum(salariofixo) as TotaldeSalarios
    from vendedor;

Select * from totalsalarios;

-- View ProdutodescA

CREATE OR REPLACE VIEW ProdutodescA AS
SELECT codprod, descricao
FROM produto
WHERE descricao like 'A%'
WITH CHECK OPTION;

Select * from produtodesca;

--Insert into ProdutodescA values (40, 'Manteiga');
Insert into ProdutodescA values (41, 'Azeite');

-- com JOIN

Select nome from vendsal v join pedido p on v.codigo = p.codvend;

Select nome from vendedor v join pedido p on v.codvend = p.codvend;

-- Comando WITH

With ClientesAtivos AS
    (SELECT codcli from Cliente WHERE endereco is not null ), 
    ClientesInativos AS
    (SELECT codcli from Cliente WHERE endereco is null )
    SELECT * FROM ClientesAtivos
    UNION 
    SELECT * FROM ClientesInativos;
	
	
-- Aula 08 Transações 

-- Parte 01
-- desabilite o autocommit; 
-- Iniciando transação
select * from vendedor;
insert into vendedor values(default,'Melissa Gonçalves', '1988/07/28', 3300.80,'B');
insert into vendedor values(default,'Debora Maciel', '1990/04/20', 3300.80,'B');
insert into vendedor values(default,'Alicia Silva', '1998/06/28', 2300.80,'C');
select * from vendedor;
commit; 

-- novo teste de transação
-- Início da nova transação
select * from vendedor;
insert into vendedor values(default,'Moacir Ribeiro', '1988/07/27', 3300.80,'B');
insert into vendedor values(default,'Daniel Moura', '1990/03/20', 3300.80,'B');
insert into vendedor values(default,'Alvaro Soares', '1998/04/28', 2300.80,'C');
select * from vendedor;
-- supondo uma exceção - if exception ... then 
rollback; 
-- final da transação

select * from vendedor;

-- Parte 02
-- User 1:postgres
-- Criação de outro usuário caso ainda não tenha 
CREATE ROLE plme LOGIN
  PASSWORD 'bd2' SUPERUSER CREATEDB CREATEROLE ;
-- crie conexão com novo usuário e deixe-a aberta em outra query tool 

-- delete from vendedor where codvend > 11; 

Grant all on vendedor to plme;

--Iniciando a transação 
select * from vendedor; 
insert into vendedor values(12,'Clovis Paulo', '1994/01/12', 5300.80,'A');
Select * from vendedor;
commit;
select * from vendedor;

-- novo teste de transação
insert into vendedor values(40,'Augusto Paulo', '1996/03/12', 5300.80,'A');
commit; 

-- Parte 03
-- Nova transação

Begin;
UPDATE vendedor
 SET salariofixo = 6000
 WHERE codvend = 1;
SAVEPOINT a_v1;
UPDATE vendedor
 SET salariofixo = 5000
 WHERE codvend = 2;
SAVEPOINT a_v2;
Select * from vendedor; 
SELECT sum(salariofixo) FROM vendedor;
ROLLBACK TO SAVEPOINT a_v1;
SELECT SUM(salariofixo) FROM vendedor;
Select * from vendedor; 
UPDATE vendedor
 SET salariofixo = 5000
 WHERE codvend = 2;
Select * from vendedor; 
COMMIT;
