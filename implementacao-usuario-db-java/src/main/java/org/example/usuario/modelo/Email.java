package org.example.usuario.modelo;

import java.util.Locale;
import java.util.Objects;
import java.util.regex.Pattern;

/** Objeto de valor: representa um e-mail valido para o cadastro. */
public final class Email {
    private static final Pattern FORMATO = Pattern.compile(
            "^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)+$"
    );
    private final String valor;

    public Email(String valor) {
        if (!validarEmail(valor)) {
            throw new IllegalArgumentException("E-mail invalido: " + valor);
        }
        this.valor = valor.trim().toLowerCase(Locale.ROOT);
    }

    public static boolean validarEmail(String email) {
        return email != null && email.length() <= 254
                && FORMATO.matcher(email.trim()).matches();
    }

    public boolean validarEmail() {
        return validarEmail(valor);
    }

    public String getValor() {
        return valor;
    }

    @Override public String toString() { return valor; }
    @Override public boolean equals(Object obj) {
        return obj instanceof Email outro && valor.equals(outro.valor);
    }
    @Override public int hashCode() { return Objects.hash(valor); }
}
