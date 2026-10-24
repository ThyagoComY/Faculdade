package org.example.usuario.modelo;

import java.util.Objects;

/** Objeto de valor: CPF de 11 digitos, incluindo verificadores. */
public final class CPF {
    private final String digitos;

    public CPF(String valor) {
        if (!validarCPF(valor)) {
            throw new IllegalArgumentException("CPF invalido");
        }
        this.digitos = somenteDigitos(valor);
    }

    public static boolean validarCPF(String valor) {
        if (valor == null || !valor.matches("(?:\\d{11}|\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2})")) {
            return false;
        }
        String cpf = somenteDigitos(valor);
        if (cpf.chars().distinct().count() == 1) {
            return false;
        }
        return digitoVerificador(cpf, 9) == cpf.charAt(9) - '0'
                && digitoVerificador(cpf, 10) == cpf.charAt(10) - '0';
    }

    public boolean validarCPF() {
        return validarCPF(digitos);
    }

    public String getDigitos() {
        return digitos;
    }

    private static int digitoVerificador(String cpf, int quantidade) {
        int soma = 0;
        for (int pos = 0; pos < quantidade; pos++) {
            soma += (cpf.charAt(pos) - '0') * (quantidade + 1 - pos);
        }
        int resto = (soma * 10) % 11;
        return resto == 10 ? 0 : resto;
    }

    private static String somenteDigitos(String valor) {
        return valor.replaceAll("\\D", "");
    }

    @Override public String toString() { return digitos; }
    @Override public boolean equals(Object obj) {
        return obj instanceof CPF outro && digitos.equals(outro.digitos);
    }
    @Override public int hashCode() { return Objects.hash(digitos); }
}
