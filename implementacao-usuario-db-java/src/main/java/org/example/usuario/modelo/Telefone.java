package org.example.usuario.modelo;

import java.util.Objects;

/** Telefone brasileiro com DDD, fixo (10 digitos) ou celular (11). */
public final class Telefone {
    private final String digitos;

    public Telefone(String valor) {
        if (!validarTelefone(valor)) {
            throw new IllegalArgumentException("Telefone invalido");
        }
        this.digitos = normalizar(valor);
    }

    public static boolean validarTelefone(String valor) {
        if (valor == null || !valor.matches("[+()0-9\\s.-]+")) {
            return false;
        }
        String numero = normalizar(valor);
        if (!numero.matches("\\d{10,11}")) {
            return false;
        }
        int ddd = Integer.parseInt(numero.substring(0, 2));
        if (ddd < 11 || ddd > 99 || ddd % 10 == 0) {
            return false;
        }
        String local = numero.substring(2);
        return local.length() == 9 ? local.charAt(0) == '9'
                : local.charAt(0) >= '2' && local.charAt(0) <= '5';
    }

    public boolean validarTelefone() {
        return validarTelefone(digitos);
    }

    public String getDDD() {
        return digitos.substring(0, 2);
    }

    public String getDigitos() {
        return digitos;
    }

    private static String normalizar(String valor) {
        String d = valor.replaceAll("\\D", "");
        if (d.startsWith("55") && (d.length() == 12 || d.length() == 13)) {
            return d.substring(2);
        }
        return d;
    }

    @Override public String toString() { return digitos; }
    @Override public boolean equals(Object obj) {
        return obj instanceof Telefone outro && digitos.equals(outro.digitos);
    }
    @Override public int hashCode() { return Objects.hash(digitos); }
}
