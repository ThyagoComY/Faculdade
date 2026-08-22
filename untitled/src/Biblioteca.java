import biblioteca.*;

public class Biblioteca {
    public static void main(String[] args) {
        Acervo acervo = new Acervo();

        Livro livro01 = new Livro("Dom Casmurro", "Machado de Assis", 400, "Romance", "Garnier");

        acervo.adicionarLivro(livro01);

        acervo.listarLivros();
    }
}
