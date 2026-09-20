public class Main {
    public static void main(String[] args) {
        Professor p1 = new Professor("Enilda Caceres", "123.456.789.21", "adonadetudo@email.com");
        p1.exibirDados();

        Disciplina d1 = p1.cadastrarDisciplina("POO em Java", 80);

        Turma t1 = p1.criarTurma(d1, p1);

        Aluno a1 = p1.cadastrarAluno("Ana", "25688056431", "aninha33@email.com");
        Aluno a2 = p1.cadastrarAluno("Thyago", "09455586188", "thyago@email.com");
        Aluno a3 = p1.cadastrarAluno("Gustavo", "15792864924", "gustah@email.com");

        t1.adicionarAluno(a1);
        t1.adicionarAluno(a2);
        t1.adicionarAluno(a3);

        System.out.println("");
        t1.listarAlunos();

        Nota n1 = p1.lancarNota(a1, 8.0, "Prova 1");
        Nota n2 = p1.lancarNota(a1, 7.5, "Trabalho");

        Nota n3 = p1.lancarNota(a2, 5.0, "Prova 1");
        Nota n4 = p1.lancarNota(a2, 6.0, "Trabalho");

        Nota n5 = p1.lancarNota(a3, 9.0, "Prova 1");
        Nota n6 = p1.lancarNota(a3, 10.0, "Trabalho");

        t1.adicionarNota(n1);
        t1.adicionarNota(n2);
        t1.adicionarNota(n3);
        t1.adicionarNota(n4);
        t1.adicionarNota(n5);
        t1.adicionarNota(n6);

        System.out.println("");
        t1.listarNotas();

        System.out.println("");
        a1.consultarNotas();

        System.out.println("");
        a2.consultarTurmas();

        System.out.println("");
        d1.exibirDados();
    }
}