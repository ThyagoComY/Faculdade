package org.example.usuario.infra;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

/** Centraliza a criacao de conexoes; credenciais nao ficam no codigo. */
public final class Conexao {
    private Conexao() { }

    public static Connection abrir() throws SQLException {
        String url = System.getenv().getOrDefault(
                "DB_URL", "jdbc:mysql://localhost:3306/db_java");
        String usuario = System.getenv().getOrDefault("DB_USER", "root");
        String senha = System.getenv().getOrDefault("DB_PASSWORD", "");
        return DriverManager.getConnection(url, usuario, senha);
    }
}
