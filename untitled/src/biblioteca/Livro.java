package biblioteca;

public class Livro {
    public String titulo;
    public String autor;
    public int qtdPaginas;
    public String genero;
    public String editora;

    public Livro(String titulo, String autor, int qtdPaginas, String genero, String editora){
        this.titulo = titulo;
        this.autor = autor;
        this.qtdPaginas = qtdPaginas;
        this.genero = genero;
        this.editora = editora;
    }
    public void atualizar(String novoTitulo){
        this.titulo = novoTitulo;
    }
}
