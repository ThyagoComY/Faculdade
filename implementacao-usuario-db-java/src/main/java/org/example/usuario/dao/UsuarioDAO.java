package org.example.usuario.dao;

import org.example.usuario.infra.Conexao;
import org.example.usuario.modelo.CPF;
import org.example.usuario.modelo.Email;
import org.example.usuario.modelo.Endereco;
import org.example.usuario.modelo.Telefone;
import org.example.usuario.modelo.Usuario;

import java.sql.Connection;
import java.sql.Date;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

/** DAO: somente persistencia JDBC (sem regras de validacao de dominio). */
public final class UsuarioDAO {
    private static final String CAMPOS = "id, nome, cpf, email, telefone, data_nascimento, "
            + "JSON_UNQUOTE(JSON_EXTRACT(endereco, '$.rua')) AS rua, "
            + "JSON_UNQUOTE(JSON_EXTRACT(endereco, '$.bairro')) AS bairro, "
            + "JSON_UNQUOTE(JSON_EXTRACT(endereco, '$.numero')) AS numero, "
            + "JSON_UNQUOTE(JSON_EXTRACT(endereco, '$.cep')) AS cep";

    public Usuario criar(Usuario usuario) throws SQLException {
        String sql = "INSERT INTO usuario "
                + "(nome, cpf, email, telefone, data_nascimento, endereco) "
                + "VALUES (?, ?, ?, ?, ?, JSON_OBJECT('rua', ?, 'bairro', ?, 'numero', ?, 'cep', ?))";
        try (Connection conexao = Conexao.abrir();
             PreparedStatement stmt = conexao.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS)) {
            preencher(stmt, usuario);
            stmt.executeUpdate();
            try (ResultSet chaves = stmt.getGeneratedKeys()) {
                if (!chaves.next()) throw new SQLException("ID nao foi gerado");
                return usuario.comId(chaves.getLong(1));
            }
        }
    }

    public Optional<Usuario> buscarPorId(long id) throws SQLException {
        String sql = "SELECT " + CAMPOS + " FROM usuario WHERE id = ?";
        try (Connection conexao = Conexao.abrir();
             PreparedStatement stmt = conexao.prepareStatement(sql)) {
            stmt.setLong(1, id);
            try (ResultSet resultado = stmt.executeQuery()) {
                return resultado.next() ? Optional.of(mapear(resultado)) : Optional.empty();
            }
        }
    }

    public List<Usuario> listar() throws SQLException {
        String sql = "SELECT " + CAMPOS + " FROM usuario ORDER BY id";
        List<Usuario> usuarios = new ArrayList<>();
        try (Connection conexao = Conexao.abrir();
             PreparedStatement stmt = conexao.prepareStatement(sql);
             ResultSet resultado = stmt.executeQuery()) {
            while (resultado.next()) usuarios.add(mapear(resultado));
        }
        return usuarios;
    }

    public boolean atualizar(Usuario usuario) throws SQLException {
        if (usuario.getId() == null) {
            throw new IllegalArgumentException("Usuario precisa de ID para atualizar");
        }
        String sql = "UPDATE usuario SET nome=?, cpf=?, email=?, telefone=?, "
                + "data_nascimento=?, endereco=JSON_OBJECT('rua', ?, 'bairro', ?, "
                + "'numero', ?, 'cep', ?) WHERE id=?";
        try (Connection conexao = Conexao.abrir();
             PreparedStatement stmt = conexao.prepareStatement(sql)) {
            preencher(stmt, usuario);
            stmt.setLong(10, usuario.getId());
            return stmt.executeUpdate() > 0;
        }
    }

    public boolean excluir(long id) throws SQLException {
        String sql = "DELETE FROM usuario WHERE id=?";
        try (Connection conexao = Conexao.abrir();
             PreparedStatement stmt = conexao.prepareStatement(sql)) {
            stmt.setLong(1, id);
            return stmt.executeUpdate() > 0;
        }
    }

    private void preencher(PreparedStatement stmt, Usuario usuario) throws SQLException {
        stmt.setString(1, usuario.getNome());
        stmt.setString(2, usuario.getCpf().getDigitos());
        stmt.setString(3, usuario.getEmail().getValor());
        stmt.setString(4, usuario.getTelefone().getDigitos());
        stmt.setDate(5, Date.valueOf(usuario.getDataNascimento()));
        stmt.setString(6, usuario.getEndereco().getRua());
        stmt.setString(7, usuario.getEndereco().getBairro());
        stmt.setString(8, usuario.getEndereco().getNumero());
        stmt.setString(9, usuario.getEndereco().getCEP());
    }

    private Usuario mapear(ResultSet rs) throws SQLException {
        return new Usuario(
                rs.getLong("id"),
                rs.getString("nome"),
                new CPF(rs.getString("cpf")),
                new Email(rs.getString("email")),
                new Telefone(rs.getString("telefone")),
                rs.getDate("data_nascimento").toLocalDate(),
                new Endereco(rs.getString("rua"), rs.getString("bairro"),
                             rs.getString("numero"), rs.getString("cep"))
        );
    }
}
