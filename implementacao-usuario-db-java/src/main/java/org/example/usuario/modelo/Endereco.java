package org.example.usuario.modelo;

import java.util.Objects;

/** Endereco imutavel; CEP e salvo somente com 8 digitos. */
public final class Endereco {
    private final String rua;
    private final String bairro;
    private final String numero;
    private final String cep;

    public Endereco(String rua, String bairro, String numero, String cep) {
        this.rua = textoObrigatorio(rua, "rua");
        this.bairro = textoObrigatorio(bairro, "bairro");
        this.numero = textoObrigatorio(numero, "numero");
        if (!validarCEP(cep)) {
            throw new IllegalArgumentException("CEP invalido");
        }
        this.cep = cep.replaceAll("\\D", "");
    }

    public static boolean validarCEP(String cep) {
        return cep != null && cep.matches("(?:\\d{8}|\\d{5}-\\d{3})");
    }

    public boolean validarCEP() { return validarCEP(cep); }
    public String getRua() { return rua; }
    public String getBairro() { return bairro; }
    public String getNumero() { return numero; }
    public String getCEP() { return cep; }

    private static String textoObrigatorio(String texto, String campo) {
        if (texto == null || texto.isBlank()) {
            throw new IllegalArgumentException("Campo obrigatorio: " + campo);
        }
        return texto.trim();
    }

    @Override public String toString() {
        return rua + ", " + numero + " - " + bairro + " - CEP " + cep;
    }
    @Override public boolean equals(Object obj) {
        return obj instanceof Endereco outro && rua.equals(outro.rua)
                && bairro.equals(outro.bairro) && numero.equals(outro.numero)
                && cep.equals(outro.cep);
    }
    @Override public int hashCode() { return Objects.hash(rua, bairro, numero, cep); }
}
