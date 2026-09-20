public abstract class Pessoa {
    String nome;
    String cpf;
    String email;

    public String getNome() {
        String n = this.nome;
        return n;
    }

    public String getCpf() {
        return this.cpf;
    }

    public String getEmail() {
        return this.email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public abstract void exibirDados();
}