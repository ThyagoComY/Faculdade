package org.example.usuario.exemplo;

import org.example.usuario.dao.UsuarioDAO;
import org.example.usuario.modelo.CPF;
import org.example.usuario.modelo.Email;
import org.example.usuario.modelo.Endereco;
import org.example.usuario.modelo.Telefone;
import org.example.usuario.modelo.Usuario;

import java.sql.SQLException;
import java.time.LocalDate;

/** Executar apenas em banco de testes: cria, consulta, atualiza e remove um usuario. */
public final class ExemploCrud {
    public static void main(String[] args) throws SQLException {
        UsuarioDAO dao = new UsuarioDAO();
        Usuario usuario = new Usuario(
                "Usuario Teste", new CPF("529.982.247-25"),
                new Email("teste.exemplo@exemplo.com"),
                new Telefone("(67) 99999-8888"),
                LocalDate.of(2001, 5, 17),
                new Endereco("Rua Exemplo", "Centro", "123", "79002-000")
        );

        Usuario salvo = dao.criar(usuario);
        System.out.println("Criado: " + salvo);
        System.out.println("Consultado: " + dao.buscarPorId(salvo.getId()));
        System.out.println("Total de usuarios: " + dao.listar().size());

        Usuario editado = new Usuario(
                salvo.getId(), "Usuario Atualizado", salvo.getCpf(), salvo.getEmail(),
                salvo.getTelefone(), salvo.getDataNascimento(), salvo.getEndereco());
        System.out.println("Atualizado: " + dao.atualizar(editado));
        System.out.println("Excluido: " + dao.excluir(salvo.getId()));
    }
}
