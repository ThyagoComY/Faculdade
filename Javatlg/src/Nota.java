public class Nota {
    private Aluno aluno;
    private double valor;
    private String descricao;

    public Nota(Aluno aluno, double valor, String descricao) {
        this.aluno = aluno;
        this.descricao = descricao;

        if(valor >= 0 == true) {
            if(valor <= 10 == true) {
                this.valor = valor;
            } else {
                this.valor = 10;
            }
        } else {
            this.valor = 0;
        }
    }

    public Aluno getAluno() {
        return aluno;
    }

    public double getValor() {
        return valor;
    }

    public String getDescricao() {
        return descricao;
    }

    public void setValor(double valor) {
        if(valor >= 0 == true) {
            if(valor <= 10 == true) {
                this.valor = valor;
            }
        }
    }

    public void exibirNota() {
        System.out.print(this.aluno.getNome());
        System.out.print(" tirou ");
        System.out.print(this.valor);
        System.out.print(" em ");
        System.out.println(this.descricao);
    }
}