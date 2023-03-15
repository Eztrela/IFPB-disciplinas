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


------- Inserção questão 7 -----------
insert into artista values(default,'Will Smith','Pensilvânia','USA','12/10/68');
insert into artista values(default,'Phyllis Smith','Missouri','USA','10/07/51');
insert into artista values(default,'Matthew McConaughey', 'Texas','04/11/69');

insert into categoria values(default,'Ficção Científica');
insert into categoria values(default,'Animação');
insert into categoria values(default,'Terror');

insert into estudio values(default,'Warner Bros.');
insert into estudio values(default,'Pixar.');
insert into estudio values (default,'Marvel');

insert into filme values(default,'Eu sou a lenda', 2007,101,4);
insert into filme values(default,'Divertidamente', 2015,94,5);
insert into filme values(default,'Interstellar',2014,169,1);

insert into personagem values(8,7, 'Robert Neville',100000);
insert into personagem values(9,8, 'Tristeza',15000);
insert into personagem values(10,9, 'Cooper',50000);

----------- Questão 8 -----------
select * from artista
order by nomeart;

----------- Questão 9 ------------
select * from artista
where nomeart like 'B%';

----------- Questão 10 -----------
select * from filme
where ano = 2019;

---------- Questão 11 -----------
update personagem set cache = cache * 1.15;

---------- Questão 12 -----------
update artista set pais = 'Congo' where nomeart = 'Cameron Diaz'
update artista set pais = 'Argentina' where nomeart = 'Matthew McConaughey'
update artista set pais = 'Australia' where nomeart = 'Phyllis Smith'

---------- Questão 13 -----------
insert into artista values(default,'Wagner Moura','Bahia','Brasil',TO_DATE('27/06/76', 'DD/MM/YY'));
insert into artista values(default,'Fernanda Montenegro','Rio de Janeiro','Brasil',TO_DATE('16/10/29', 'DD/MM/YY'));

----------- Questão 14 -----------
alter table personagem drop  constraint FKPersonagem2Artis;
alter table personagem 
add constraint FKPersonagem2Artis 
foreign key (codart) 
references artista 
on delete cascade;

delete from artista
where nomeart = 'Will Smith';