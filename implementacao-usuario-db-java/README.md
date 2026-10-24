# CRUD de usuário — Java 21 + MySQL

Implementação do exercício proposto para o repositório `Caique-FLopes/db-java`.

> **Atenção:** este pacote é um módulo independente para **adicionar** ao repositório. Não foi possível acessar todos os arquivos Java originais pelo GitHub, então não substitua os arquivos preexistentes às cegas. As classes novas foram isoladas no pacote `org.example.usuario`, evitando conflitos de nomes.

## O que contém

- `Usuario`: entidade imutável com nome, CPF, e-mail, telefone, nascimento e endereço.
- `Email`: `validarEmail()`.
- `CPF`: `validarCPF()` e `getDigitos()`; verifica os dois dígitos verificadores.
- `Telefone`: `validarTelefone()` e `getDDD()`; aceita DDD e número brasileiro fixo/celular, com ou sem +55.
- `Endereco`: `getRua()`, `getBairro()`, `getNumero()`, `getCEP()`, `validarCEP()`.
- `Conexao`: abre conexão JDBC por variáveis de ambiente.
- `UsuarioDAO`: `criar`, `buscarPorId`, `listar`, `atualizar`, `excluir` (CRUD com `PreparedStatement`).
- `ExemploCrud`: demonstra as quatro operações (insere e remove um usuário fictício).
- `TesteValidacoes`: testes simples executáveis sem depender do servidor MySQL.
- `sql/01_criar_usuario.sql`: cria banco e tabela.

## Modelo SQL

A tabela `usuario` contém as colunas `id`, `nome`, `cpf`, `email`, `telefone`, `data_nascimento` e **`endereco`**.

`endereco` é uma **coluna JSON do MySQL**, estruturada assim:

```json
{"rua":"Rua Exemplo","bairro":"Centro","numero":"123","cep":"79002000"}
```

A opção de armazenar o endereço como JSON permite conservar **uma coluna `endereco`**, conforme o enunciado, sem concatenar valores ou perder a divisão entre rua, bairro, número e CEP. O DAO usa `JSON_OBJECT` para salvar e `JSON_EXTRACT` para ler cada atributo. CPF e telefone são armazenados como texto (preservam zeros à esquerda).

## Como integrar ao repositório original

1. Copie as pastas `src/main/java/org/example/usuario` e `src/test/java/org/example/usuario` para as mesmas pastas do projeto original.
2. Copie o script em `sql/`.
3. Não é necessário substituir o `pom.xml` existente se ele já usa Java 21 e MySQL Connector/J 9.1.0. O `pom.xml` incluído permite testar o módulo separadamente.
4. Abra o MySQL Workbench e execute `sql/01_criar_usuario.sql`.
5. Configure a conexão. Por padrão, o módulo usa `jdbc:mysql://localhost:3306/db_java`, usuário `root` e senha vazia; **recomenda-se configurar uma conta local e senha por variáveis de ambiente**, como abaixo.

### Configuração de banco no PowerShell (Windows)

```powershell
$env:DB_URL = 'jdbc:mysql://localhost:3306/db_java'
$env:DB_USER = 'root'
$env:DB_PASSWORD = 'SUA_SENHA_LOCAL'
```

No terminal Linux/macOS:

```bash
export DB_URL='jdbc:mysql://localhost:3306/db_java'
export DB_USER='root'
export DB_PASSWORD='SUA_SENHA_LOCAL'
```

### Compilar com Maven

```bash
mvn compile
```

### Testar validações em PowerShell

Na raiz do projeto, compile as classes e os testes em uma pasta temporária:

```powershell
New-Item -ItemType Directory -Force .\out | Out-Null
$javaFiles = Get-ChildItem .\src\main\java\org\example\usuario, .\src\test\java\org\example\usuario -Recurse -Filter *.java | ForEach-Object { $_.FullName }
javac -encoding UTF-8 -d .\out $javaFiles
java -ea -cp .\out org.example.usuario.TesteValidacoes
```

No Linux/macOS:

```bash
mkdir -p out
javac -encoding UTF-8 -d out $(find src/main/java/org/example/usuario src/test/java/org/example/usuario -name '*.java')
java -ea -cp out org.example.usuario.TesteValidacoes
```

Saída esperada: `Testes de validacao passaram.`

### Testar o CRUD no MySQL

**Use um banco de testes** antes de executar o exemplo, pois ele insere, altera e exclui um registro fictício. Com o servidor MySQL rodando e o SQL executado:

```bash
mvn compile exec:java -Dexec.mainClass=org.example.usuario.exemplo.ExemploCrud
```

> Se já existir um registro com CPF `52998224725` ou com e-mail `teste.exemplo@exemplo.com`, o índice UNIQUE impedirá duplicidade. Remova/edite apenas dados fictícios do banco de testes.

## Operações disponíveis

```java
UsuarioDAO dao = new UsuarioDAO();
Usuario usuarioCriado = dao.criar(usuario);                  // CREATE
Optional<Usuario> encontrado = dao.buscarPorId(1L);         // READ
List<Usuario> todos = dao.listar();                         // READ
boolean atualizado = dao.atualizar(usuarioComId);           // UPDATE
boolean excluido = dao.excluir(1L);                          // DELETE
```

## Object Calisthenics aplicada

- **Envolver tipos primitivos**: CPF, Email, Telefone e Endereco são objetos de valor específicos, em vez de `String` soltas na entidade.
- **Encapsulamento**: atributos privados/finais, construtores que impedem estados inválidos e ausência de setters.
- **Responsabilidade única**: regras de validação nos objetos de valor; persistência no DAO; conexão JDBC em infraestrutura.
- **Evitar repetições**: método privado `preencher` reutilizado por INSERT e UPDATE.
- **Independência**: validar CPF/CEP/email/telefone não exige um servidor de banco de dados.

A aplicação usa `PreparedStatement` em vez de concatenar valores SQL para reduzir risco de SQL injection.

## Limites dos testes

Os testes incluídos exercitam os objetos de valor sem um MySQL em funcionamento. A compilação das classes Java e os testes básicos foram executados em Java 21. O exemplo de CRUD foi preparado, mas **não foi executado contra um servidor MySQL** neste ambiente.

Este código valida o **formato e/ou dígitos verificadores**, mas não confirma a existência real de e-mails, linhas telefônicas, endereços/CEPs ou inscrição de CPF na Receita Federal.
