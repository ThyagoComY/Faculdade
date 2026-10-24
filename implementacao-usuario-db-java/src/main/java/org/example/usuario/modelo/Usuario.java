package org.example.usuario.modelo;

import java.time.LocalDate;
import java.util.Objects;

/** Entidade Usuario: delega regras de formato aos objetos de valor. */
public final class Usuario {
    private final Long id;
    private final String nome;
    private final CPF cpf;
    private final Email email;
    private final Telefone telefone;
    private final LocalDate dataNascimento;
    private final Endereco endereco;

    public Usuario(String nome, CPF cpf, Email email, Telefone telefone,
                   LocalDate dataNascimento, Endereco endereco) {
        this(null, nome, cpf, email, telefone, dataNascimento, endereco);
    }

    public Usuario(Long id, String nome, CPF cpf, Email email, Telefone telefone,
                   LocalDate dataNascimento, Endereco endereco) {
        if (id != null && id <= 0) throw new IllegalArgumentException("ID deve ser positivo");
        if (nome == null || nome.isBlank()) throw new IllegalArgumentException("Nome obrigatorio");
        if (dataNascimento == null || dataNascimento.isAfter(LocalDate.now())) {
            throw new IllegalArgumentException("Data de nascimento invalida");
        }
        this.id = id;
        this.nome = nome.trim();
        this.cpf = Objects.requireNonNull(cpf, "CPF obrigatorio");
        this.email = Objects.requireNonNull(email, "Email obrigatorio");
        this.telefone = Objects.requireNonNull(telefone, "Telefone obrigatorio");
        this.dataNascimento = dataNascimento;
        this.endereco = Objects.requireNonNull(endereco, "Endereco obrigatorio");
    }

    public Usuario comId(long novoId) {
        return new Usuario(novoId, nome, cpf, email, telefone, dataNascimento, endereco);
    }

    public Long getId() { return id; }
    public String getNome() { return nome; }
    public CPF getCpf() { return cpf; }
    public Email getEmail() { return email; }
    public Telefone getTelefone() { return telefone; }
    public LocalDate getDataNascimento() { return dataNascimento; }
    public Endereco getEndereco() { return endereco; }

    @Override public String toString() {
        return "Usuario{id=" + id + ", nome='" + nome + "'}";
    }
}
