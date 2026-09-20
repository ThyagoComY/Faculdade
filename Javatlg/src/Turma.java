import java.util.ArrayList;
import java.util.List;

public class Turma {
    public String codigo;
    private Disciplina disciplina;
    private Professor professor;
    public List<Aluno> alunos;
    public List<Nota> notas;

    public Turma(String codigo, Disciplina disciplina, Professor professor) {
        this.codigo = codigo;
        this.disciplina = disciplina;
        this.professor = professor;
        this.alunos = new ArrayList<Aluno>();
        this.notas = new ArrayList<Nota>();
    }

    public void adicionarAluno(Aluno aluno) {
        boolean achou = false;
        for(int i = 0; i < alunos.size(); i++) {
            if(alunos.get(i) == aluno) {
                achou = true;
            }
        }
        if(achou == false) {
            alunos.add(aluno);
            aluno.minhasTurmas.add(this);
        }
    }

    public void removerAluno(Aluno aluno) {
        boolean achou = false;
        for(int i = 0; i < alunos.size(); i++) {
            if(alunos.get(i) == aluno) {
                achou = true;
            }
        }
        if(achou == true) {
            alunos.remove(aluno);
        }
    }

    public void listarAlunos() {
        System.out.println("Lista de alunos da turma:");
        for(int i = 0; i < alunos.size(); i++) {
            alunos.get(i).exibirDados();
        }
    }

    public void adicionarNota(Nota nota) {
        boolean temAluno = false;
        for(int i = 0; i < alunos.size(); i++) {
            if(alunos.get(i) == nota.getAluno()) {
                temAluno = true;
            }
        }
        if(temAluno == true) {
            notas.add(nota);
        }
    }

    public void listarNotas() {
        System.out.println("Lista de notas da turma:");
        for(int i = 0; i < notas.size(); i++) {
            notas.get(i).exibirNota();
        }
    }

    public Disciplina getDisciplina() {
        return disciplina;
    }

    public Professor getProfessor() {
        return professor;
    }
}