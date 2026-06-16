from PyQt5 import uic, QtWidgets
import pymysql.connections

banco = pymysql.connections.Connection(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "oficina_db"
)

def cadastrar_cliente():
    nome = formulario.txt_cli_nome.text()
    cpf = formulario.txt_cli_cpf.text()
    telefone = formulario.txt_cli_telefone.text()

    cursor = banco.cursor()
    sql = "INSERT INTO clientes (nome, cpf, telefone) VALUES (%s, %s, %s)"
    dados = (str(nome), str(cpf), str(telefone))
    cursor.execute(sql, dados)
    banco.commit()

    formulario.txt_cli_nome.setText("")
    formulario.txt_cli_cpf.setText("")
    formulario.txt_cli_telefone.setText("")
    listar_cliente()

def listar_cliente():
    cursor = banco.cursor()
    sql = "SELECT * FROM clientes"
    cursor.execute(sql)
    dados_lidos = cursor.fetchall()

    formulario.tb_clientes.setRowCount(len(dados_lidos))
    formulario.tb_clientes.setColumnCount(4)
    formulario.tb_clientes.setHorizontalHeaderLabels(['ID', 'Nome', 'CPF', 'Telefone'])

    for linha in range(0, len(dados_lidos)):
        for coluna in range(0, 4):
            formulario.tb_clientes.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(dados_lidos[linha][coluna])))

def excluir_cliente():
    linha = formulario.tb_clientes.currentRow()
    if linha >= 0:
        id_cliente = formulario.tb_clientes.item(linha, 0).text()
        cursor = banco.cursor()
        sql = "DELETE FROM clientes WHERE id = %s"
        cursor.execute(sql, (id_cliente,))
        banco.commit()
        print("Cliente excluído com sucesso!")
        listar_cliente()

def cadastrar_carro():
    marca = formulario.txt_car_marca.text()
    modelo = formulario.txt_car_modelo.text()
    placa = formulario.txt_car_placa.text()
    cli_id = formulario.txt_car_cli_id.text()

    cursor = banco.cursor()
    sql = "INSERT INTO carros (marca, modelo, placa, cliente_id) VALUES (%s, %s, %s, %s)"
    dados = (str(marca), str(modelo), str(placa), str(cli_id))
    cursor.execute(sql, dados)
    banco.commit()

    formulario.txt_car_marca.setText("")
    formulario.txt_car_modelo.setText("")
    formulario.txt_car_placa.setText("")
    formulario.txt_car_cli_id.setText("")
    listar_carro()

def listar_carro():
    cursor = banco.cursor()
    sql = "SELECT * FROM carros"
    cursor.execute(sql)
    dados_lidos = cursor.fetchall()

    formulario.tb_carros.setRowCount(len(dados_lidos))
    formulario.tb_carros.setColumnCount(5)
    formulario.tb_carros.setHorizontalHeaderLabels(['ID', 'Marca', 'Modelo', 'Placa', 'ID Cliente'])

    for linha in range(0, len(dados_lidos)):
        for coluna in range(0, 5):
            formulario.tb_carros.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(dados_lidos[linha][coluna])))

def excluir_carro():
    linha = formulario.tb_carros.currentRow()
    if linha >= 0:
        id_carro = formulario.tb_carros.item(linha, 0).text()
        cursor = banco.cursor()
        sql = "DELETE FROM carros WHERE id = %s"
        cursor.execute(sql, (id_carro,))
        banco.commit()
        listar_carro()

def cadastrar_servico():
    nome = formulario.txt_ser_nome.text()
    descricao = formulario.txt_ser_desc.text()
    valor = formulario.txt_ser_valor.text()

    cursor = banco.cursor()
    sql = "INSERT INTO servicos (nome, descricao, valor) VALUES (%s, %s, %s)"
    dados = (str(nome), str(descricao), str(valor))
    cursor.execute(sql, dados)
    banco.commit()

    formulario.txt_ser_nome.setText("")
    formulario.txt_ser_desc.setText("")
    formulario.txt_ser_valor.setText("")
    listar_servico()

def listar_servico():
    cursor = banco.cursor()
    sql = "SELECT * FROM servicos"
    cursor.execute(sql)
    dados_lidos = cursor.fetchall()

    formulario.tb_servicos.setRowCount(len(dados_lidos))
    formulario.tb_servicos.setColumnCount(4)
    formulario.tb_servicos.setHorizontalHeaderLabels(['ID', 'Nome', 'Descrição', 'Valor (R$)'])

    for linha in range(0, len(dados_lidos)):
        for coluna in range(0, 4):
            formulario.tb_servicos.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(dados_lidos[linha][coluna])))

def excluir_servico():
    linha = formulario.tb_servicos.currentRow()
    if linha >= 0:
        id_ser = formulario.tb_servicos.item(linha, 0).text()
        cursor = banco.cursor()
        sql = "DELETE FROM servicos WHERE id = %s"
        cursor.execute(sql, (id_ser,))
        banco.commit()
        listar_servico()

def cadastrar_os():
    data = formulario.txt_os_data.text()
    status = formulario.txt_os_status.text()
    cli_id = formulario.txt_os_cli_id.text()
    carro_id = formulario.txt_os_carro_id.text()
    valor = formulario.txt_os_valor.text()

    cursor = banco.cursor()
    sql = "INSERT INTO ordens_servico (data_abertura, status, valor, cliente_id, veiculo_id) VALUES (%s, %s, %s, %s, %s)"
    dados = (str(data), str(status), str(valor), str(cli_id), str(carro_id))
    cursor.execute(sql, dados)
    banco.commit()

    formulario.txt_os_data.setText("")
    formulario.txt_os_status.setText("")
    formulario.txt_os_cli_id.setText("")
    formulario.txt_os_carro_id.setText("")
    formulario.txt_os_valor.setText("")
    listar_os()

def listar_os():
    cursor = banco.cursor()
    sql = "SELECT * FROM ordens_servico"
    cursor.execute(sql)
    dados_lidos = cursor.fetchall()

    formulario.tb_os.setRowCount(len(dados_lidos))
    formulario.tb_os.setColumnCount(6)
    formulario.tb_os.setHorizontalHeaderLabels(['ID', 'Data', 'Status', 'Valor (R$)', 'ID Cliente', 'ID Veículo'])

    for linha in range(0, len(dados_lidos)):
        for coluna in range(0, 6):
            formulario.tb_os.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(dados_lidos[linha][coluna])))

def excluir_os():
    linha = formulario.tb_os.currentRow()
    if linha >= 0:
        id_os = formulario.tb_os.item(linha, 0).text()
        cursor = banco.cursor()
        sql = "DELETE FROM ordens_servico WHERE id = %s"
        cursor.execute(sql, (id_os,))
        banco.commit()
        listar_os()

import sys
app = QtWidgets.QApplication(sys.argv)
formulario = uic.loadUi("tela_oficina.ui")

formulario.btn_cad_cliente.clicked.connect(cadastrar_cliente)
formulario.btn_lis_cliente.clicked.connect(listar_cliente)
formulario.btn_exc_cliente.clicked.connect(excluir_cliente)

formulario.btn_cad_carro.clicked.connect(cadastrar_carro)
formulario.btn_lis_carro.clicked.connect(listar_carro)
formulario.btn_exc_carro.clicked.connect(excluir_carro)

formulario.btn_cad_servico.clicked.connect(cadastrar_servico)
formulario.btn_lis_servico.clicked.connect(listar_servico)
formulario.btn_exc_servico.clicked.connect(excluir_servico)

formulario.btn_cad_os.clicked.connect(cadastrar_os)
formulario.btn_lis_os.clicked.connect(listar_os)
formulario.btn_exc_os.clicked.connect(excluir_os)

formulario.show()
app.exec()
