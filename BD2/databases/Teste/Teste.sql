-- criando a tabela Teste

Create table teste(
cod serial not null, 
valor char(2));
Insert into teste(valor) values('xx');
Insert into teste(cod,valor) values (default, 'yy');
Insert into teste values (default, 'zz');
Select * from teste;

-- Alter table

ALTER TABLE Teste ADD telefone char(16);
ALTER TABLE Teste ADD fone char(16) default 'não listado';

Select * from teste; 

ALTER TABLE Teste DROP COLUMN telefone;
ALTER TABLE Teste alter column valor type varchar(30);
ALTER TABLE teste RENAME TO teste2; 
ALTER TABLE Teste2 RENAME COLUMN valor TO descrição;
Select * from teste2; 


