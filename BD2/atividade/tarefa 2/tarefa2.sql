CREATE TABLE Filme (
   	CodFILME   	Serial  NOT NULL,
   	Titulo      	Varchar(25),
   	Ano         	integer,
   	Duracao   	  integer,
   	CodCATEG   	integer,
   	CodEst     	integer);
CREATE TABLE Artista (
   	CodART  	Serial  NOT NULL,
   	NomeART	Varchar(25),
   	Cidade      	Varchar(20),
   	Pais        	Varchar(20),
   	DataNasc   	Date);
CREATE TABLE Estudio (
   	CodEst 	serial  NOT NULL,
   	NomeEst	Varchar(25));
CREATE TABLE Categoria (
   	CodCATEG   	serial  NOT NULL,
   	DescCATEG VARCHAR(25));
CREATE TABLE Personagem (
   	CodART 	integer  NOT NULL,
   	CodFILME   integer  NOT NULL,
   	NomePers  VARCHAR(25),
   	Cache       	numeric(15,2));
ALTER TABLE Filme ADD CONSTRAINT PKFilme PRIMARY KEY(CodFILME);
ALTER TABLE Artista ADD CONSTRAINT PKArtista PRIMARY KEY(CodART);
ALTER TABLE Estudio ADD CONSTRAINT PKEst PRIMARY KEY(CodEst);
ALTER TABLE Categoria ADD CONSTRAINT PKCategoria PRIMARY KEY(CodCATEG);
ALTER TABLE Personagem ADD CONSTRAINT PKPersonagem PRIMARY KEY(CodART,CodFILME);
ALTER TABLE Filme ADD CONSTRAINT FKFilme1Categ FOREIGN KEY(CodCATEG) REFERENCES Categoria;
ALTER TABLE Filme ADD CONSTRAINT FKFilme2Estud FOREIGN KEY(CodEst) REFERENCES Estudio;
ALTER TABLE Personagem ADD CONSTRAINT FKPersonagem2Artis FOREIGN KEY(CodART) REFERENCES Artista;
ALTER TABLE Personagem ADD CONSTRAINT FKPersonagem1Filme FOREIGN KEY(CodFILME) REFERENCES Filme;


--------- Inserção de Artitas ---------
insert into artista values(default,'Cameron Diaz',null,'USA',TO_DATE('15/07/75', 'DD/MM/YY'));
insert into artista values(default,'Julia Roberts',null,'USA',TO_DATE('20/08/67', 'DD/MM/YY'));
insert into artista values(default,'Brad Pitt',null,null,TO_DATE('05/03/70', 'DD/MM/YY'));
insert into artista values(default,'Joaquin Phoenix',null,null,TO_DATE('06/04/72', 'DD/MM/YY'));
insert into artista values(default,'Bradley Cooper',null,'USA',TO_DATE('06/06/77', 'DD/MM/YY'));
insert into artista values(default,'Tom Cruise',null,'USA',TO_DATE('10/09/64', 'DD/MM/YY'));
insert into artista values(default,'Rodrigo Santoro','Rio de Janeiro','Brasil','12/10/78');
select * from artista order by codart;


--------- Inseção de Estúdios --------
insert into estudio values(default,'Paramount');
insert into estudio values(default,'Disney');
insert into estudio values(default,'Universal');
select * from estudio;


-------- Inserção de Categorias --------
insert into categoria values(default,'Aventura');
insert into categoria values(default,'Romance');
insert into categoria values(default,'Comédia');
insert into categoria values(default,'Ação');
insert into categoria values(default,'Suspense');
insert into categoria values(default,'Drama');
select * from categoria;


--------- Inserção de Filmes ----------
insert into filme values(default,'Encontro Explosivo',2010,134,4,1);
insert into filme values(default,'O Besouro Verde',2010,155,1,1);
insert into filme values(default,'Comer, Rezar, Amar',2010,177,2,1);
insert into filme values(default,'Coringa',2019,122,6,1);
insert into filme values(default,'Era uma vez em Hollywood',2020,119,4,2);
insert into filme values(default,'Nasce uma estrela',2018,100,6,1);
select * from filme;


--------- Inserção de Personagens ----------
insert into personagem values(1,1,'Natalie',10000);
insert into personagem values(1,2,'Tom',10000);
insert into personagem values(5,3,'John',10000);
insert into personagem values(3,2,'Ana',6000);
insert into personagem values(6,5,'Tom',11000);
insert into personagem values(4,4,'John',12000);
select * from personagem;


------------- Tarefa 2: Consulta no BD Filmes ----------

------- Questão 1 --------
select * from artista order by codart;
select * from estudio;
select * from categoria;
select * from filme;
select * from personagem;

------- Questão 2 --------
insert into filme values(default,'Elvis',2022,120,null,3);
select * from filme;

------- Questão 3 --------
select titulo from filme
where duracao > 120;

------- Questão 4 --------
select * from artista
where cidade is null;
update artista set cidade = 'João Pessoa' where nomeart = 'Brad Pitt';
update artista set cidade = 'João Pessoa' where nomeart = 'Joaquin Phoenix';
update artista set cidade = 'Miami' where nomeart = 'Bradley Cooper';

------- Questão 5 --------
select c.desccateg
from filme f join categoria c
on c.cestão 6 --------
select f.titulo,c.desccateg, e.nomeest from filme f 
join categoria c
on c.codcateg = f.codcateg
join estudio e
on e.codest = f.codest;

------- Questão 7 --------
select a.nomeart from artista a
join personagem p
on a.codart = p.codart
join filme f
on p.codfilme = f.codfilme
where f.titulo = 'Encontro Explosivo';
------- Questão 8 --------
select a.nomeart from artista a
join personagem p
on a.codart = p.codart
join filme f
on p.codfilme = f.codfilme
join categoria c
on c.codcateg = f.codcateg
where c.desccateg = 'Aventura' and a.nomeart like 'B%';
------- Questão 9  --------
select c.desccateg, count(*) from categoria c
join filme f
on c.codcateg = f.codcateg
group by c.desccateg;
------- Questão 10  --------
select a.nomeart, p.nomepers
from artista a left outer join personagem p on a.codart = p.codart;
------- Questão 11  --------
Select f.titulo as Filme, c.desccateg as Categoria
From filme f right join categoria c on f.codcateg = c.codcateg
Where f.codcateg is null; odcateg = f.codcateg
where f.titulo = 'Coringa';

------- Questão 6 --------
select f.titulo,c.desccateg, e.nomeest from filme f 
join categoria c
on c.codcateg = f.codcateg
join estudio e
on e.codest = f.codest;

------- Questão 7 --------
select a.nomeart from artista a
join personagem p
on a.codart = p.codart
join filme f
on p.codfilme = f.codfilme
where f.titulo = 'Encontro Explosivo';
------- Questão 8 --------
select a.nomeart from artista a
join personagem p
on a.codart = p.codart
join filme f
on p.codfilme = f.codfilme
join categoria c
on c.codcateg = f.codcateg
where c.desccateg = 'Aventura' and a.nomeart like 'B%';
------- Questão 9  --------
select c.desccateg, count(*) from categoria c
join filme f
on c.codcateg = f.codcateg
group by c.desccateg;
------- Questão 10  --------
select a.nomeart, p.nomepers
from artista a left outer join personagem p on a.codart = p.codart;
------- Questão 11  --------
Select f.titulo as Filme, c.desccateg as Categoria
From filme f right join categoria c on f.codcateg = c.codcateg
Where f.codcateg is null; 

