package biblioteca;

import java.util.ArrayList;

public class Acervo {
    public ArrayList<Livro> estoque = new ArrayList<Livro>();

    public Acervo(){}

    public ArrayList<Livro> adicionarLivro(Livro livro){
        this.estoque.add(livro);

        return this.estoque;
    }

    public ArrayList<Livro> removerLivro(String titulo){

        for(int posicaoAtual = 0; posicaoAtual<=this.estoque.toArray().length-1; posicaoAtual++){
            if(this.estoque.get(posicaoAtual).titulo.equals(titulo)){
                this.estoque.remove(posicaoAtual);
            }
        }
        return estoque;
    }
    public void listarLivros(){
        for(int i=0; i<=this.estoque.toArray().length-1;i++){
            System.out.println(this.estoque.get(i).titulo);
        }
    }
}
