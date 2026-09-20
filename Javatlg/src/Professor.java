public class Professor extends Pessoa {
    private String registro;
    public int cont = 0;

    public Professor(String nome, String cpf, String email) {
        this.nome = nome;
        this.cpf = cpf;
        this.email = email;
        this.registro = "PRO" + cpf;
    }

    public String getRegistro() {
        return this.registro;
    }

    public Aluno cadastrarAluno(String nome, String cpf, String email) {
        Aluno a = new Aluno(nome, cpf, email);
        return a;
    }

    public Disciplina cadastrarDisciplina(String nome, int cargaHoraria) {
        cont = cont + 1;
        Disciplina d = new Disciplina("D" + cont, nome, cargaHoraria);
        return d;
    }

    public Turma criarTurma(Disciplina disciplina, Professor professor) {
        cont = cont + 1;
        Turma t = new Turma("T" + cont, disciplina, professor);
        return t;
    }

    public Nota lancarNota(Aluno aluno, double valor, String descricao) {
        Nota n = new Nota(aluno, valor, descricao);
        return n;
    }

    public void exibirDados() {
        System.out.print("Professor: ");
        System.out.println(this.nome);
    }
}