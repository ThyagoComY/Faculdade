import java.util.ArrayList;
import java.util.List;

public class Aluno extends Pessoa {
    private String matricula;
    public List<Turma> minhasTurmas;

    public Aluno(String n, String c, String e) {
        this.nome = n;
        this.cpf = c;
        this.email = e;
        this.matricula = "MAT" + c;
        this.minhasTurmas = new ArrayList<Turma>();
    }

    public String getMatricula() {
        return this.matricula;
    }

    public void consultarNotas() {
        System.out.println("Notas de " + this.nome);
        for(int i = 0; i < minhasTurmas.size(); i++) {
            Turma t = minhasTurmas.get(i);
            for(int j = 0; j < t.notas.size(); j++) {
                Nota n = t.notas.get(j);
                if(n.getAluno().getNome() == this.getNome()) {
                    n.exibirNota();
                }
            }
        }
    }

    public void consultarTurmas() {
        System.out.println("Turmas de " + this.nome);
        for(int i = 0; i < minhasTurmas.size(); i++) {
            System.out.println(minhasTurmas.get(i).codigo);
        }
    }

    public void exibirDados() {
        System.out.print(this.nome);
        System.out.print(" - ");
        System.out.println(this.matricula);
    }
}