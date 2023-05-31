
/**********************************
 * IFPB - Curso Superior de Tec. em Sist. para Internet
 * Programa��o Orientada a Objetos
 * Prof. Fausto Maranh�o Ayres
 **********************************/

public class Teste {

    public static void main(String[] args) {
        Livro java = new Livro("java");
        Livro php = new Livro("php");
        Autor joao = new Autor("joao");
        Autor maria = new Autor("maria");

        java.adicionar(joao);
        java.adicionar(maria);
        php.adicionar(maria);


        System.out.println("-------livros");
        System.out.println(java);
        System.out.println(php);

        System.out.println("\n-----autores");
        System.out.println(joao);
        System.out.println(maria);

        //transferir autor joao do livro java para php
        Autor a = java.localizar("joao");
        if(a!=null) {
            java.remover(a);
            php.adicionar(a);
            a.remover(java);
            a.adicionar(php);
        }

        System.out.println("-------livros");
        System.out.println(java);
        System.out.println(php);

        System.out.println("\n-----autores");
        System.out.println(joao);
        System.out.println(maria);

    }

}
