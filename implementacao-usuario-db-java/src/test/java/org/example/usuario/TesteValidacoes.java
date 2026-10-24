package org.example.usuario;

import org.example.usuario.modelo.CPF;
import org.example.usuario.modelo.Email;
import org.example.usuario.modelo.Endereco;
import org.example.usuario.modelo.Telefone;
import org.example.usuario.modelo.Usuario;
import java.time.LocalDate;

/** Testes sem dependencia extra: java -ea org.example.usuario.TesteValidacoes */
public final class TesteValidacoes {
    public static void main(String[] args) {
        assert CPF.validarCPF("529.982.247-25");
        assert CPF.validarCPF("11144477735");
        assert !CPF.validarCPF("111.111.111-11");
        assert !CPF.validarCPF("52998224726");
        assert !CPF.validarCPF("123");
        assert new CPF("529.982.247-25").getDigitos().equals("52998224725");

        assert Email.validarEmail("alguem@exemplo.com.br");
        assert !Email.validarEmail("sem-arroba");
        assert !Email.validarEmail("invalido@.com");
        assert new Email("ALGUEM@EXEMPLO.COM").getValor().equals("alguem@exemplo.com");

        assert Telefone.validarTelefone("(67) 99999-8888");
        assert Telefone.validarTelefone("+55 (67) 99999-8888");
        assert Telefone.validarTelefone("(67) 3333-4444");
        assert !Telefone.validarTelefone("1234");
        assert !Telefone.validarTelefone("(67) 1234-5678");
        assert new Telefone("+55 (67) 99999-8888").getDDD().equals("67");

        assert Endereco.validarCEP("79002-000");
        assert Endereco.validarCEP("79002000");
        assert !Endereco.validarCEP("7900200");
        Endereco endereco = new Endereco("Rua Exemplo", "Centro", "123", "79002-000");
        assert endereco.getRua().equals("Rua Exemplo");
        assert endereco.getBairro().equals("Centro");
        assert endereco.getNumero().equals("123");
        assert endereco.getCEP().equals("79002000");

        Usuario usuario = new Usuario("Teste", new CPF("52998224725"),
                new Email("teste@exemplo.com"), new Telefone("67999998888"),
                LocalDate.of(2000, 1, 1), endereco);
        assert usuario.getId() == null;
        assert usuario.comId(5).getId() == 5;
        boolean rejeitou = false;
        try {
            new Usuario("Teste", usuario.getCpf(), usuario.getEmail(),
                    usuario.getTelefone(), LocalDate.now().plusDays(1), endereco);
        } catch (IllegalArgumentException expected) {
            rejeitou = true;
        }
        assert rejeitou;

        System.out.println("Testes de validacao passaram.");
    }
}
