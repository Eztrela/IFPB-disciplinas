public class Teste {
    public static void main(String[] args) {
        /**********************************
         * IFPB - Curso Superior de Tec. em Sist. para Internet
         * Programa��o Orientada a Objetos
         * Prof. Fausto Maranh�o Ayres
         **********************************/




                Produto arroz,feijao,carne,leite;
                arroz = new Produto("arroz", 5.0) ;
                feijao = new Produto("feijao", 8.0) ;
                carne = new Produto("carne", 40.0) ;
                leite = new Produto("leite", 5.0) ;

                Prateleira prat1 = new Prateleira(1, 10);
                Prateleira prat2 = new Prateleira(2, 20) ;

                Fabricante tiojoao, friboi;
                tiojoao = new Fabricante("Tio Joao");
                friboi = new Fabricante("Friboi");

                prat1.adicionar(arroz);
                prat1.adicionar(feijao);
                prat1.adicionar(carne);
                prat2.adicionar(leite);

                tiojoao.adicionar(arroz);
                tiojoao.adicionar(feijao);
                friboi.adicionar(carne);
                friboi.adicionar(leite);

                System.out.println("\n exibir relacionamentos");
                System.out.println(prat1);
                System.out.println(prat2);

                System.out.println(arroz);
                System.out.println(feijao);
                System.out.println(carne);
                System.out.println(leite);

                System.out.println(tiojoao);
                System.out.println(friboi);

                System.out.println("\n nome dos produtos Friboi");
                for(Produto p : friboi.getProdutos()) {
                    System.out.println(p.getNome());
                }


                System.out.println("\n nome+id das prateleiras dos produtos friboi");
                for(Produto p : friboi.getProdutos()) {
                    if(p.getPrateleira() == null)
                        System.out.println(p.getNome() + " sem prateleira");
                    else
                        System.out.println(p.getNome() + " "+p.getPrateleira().getId());
                }


            }
        }


