import pytest

from models import AcessoDados, ContaSaldo, ExecutarTransferenciaFinanceira


# Teste de criação da ContaSaldo 
def test_initialize_conta_saldo():
    test_argument_conta_id = 12345
    test_argument_saldo = 10

    expected_conta_id = 12345
    expected_saldo = 10

    actual = ContaSaldo(test_argument_conta_id, test_argument_saldo)

    error_message_conta_id = "Conta ID não é a esperada"
    error_message_saldo = "Saldo não é a esperada"

    assert actual.conta_id == expected_conta_id, error_message_conta_id
    assert actual.saldo == expected_saldo, error_message_saldo

# Teste do retorno do getSaldo
def test_return_get_saldo():
    test_argument_conta_id = 938485762

    expected_conta_id = 938485762
    expected_saldo = 180

    acesso_dados = AcessoDados()
    actual = acesso_dados.getSaldo(test_argument_conta_id)

    error_message_conta_id = "Conta ID não é a esperada"
    error_message_saldo = "Saldo não é a esperada"

    assert actual.conta_id == expected_conta_id, error_message_conta_id
    assert actual.saldo == expected_saldo, error_message_saldo


# Teste do método da atualizar
def test_atualizar_method():
    test_argument_conta_id = 938485762
    test_argument_saldo_atualizado = 0

    expected_conta_id = 938485762
    expected_saldo = 0

    acesso_dados = AcessoDados()
    actual = acesso_dados.atualizar(test_argument_conta_id, test_argument_saldo_atualizado)

    error_message_conta_id = "Conta ID não é a esperada"
    error_message_saldo = "Saldo não é a esperada"

    assert actual.conta_id == expected_conta_id, error_message_conta_id
    assert actual.saldo == expected_saldo, error_message_saldo


# Teste de método de transferir com sucesso
def test_success_transferir_method():
    test_argument_correlation_id = 1
    test_argument_conta_id_origem = 210385733
    test_argument_conta_id_destion = 2147483649
    test_argument_valor = 10

    expect_message = "Transacao numero 1 foi efetivada com sucesso! Novos saldos: Conta Origem:0 | Conta Destino: 10"

    executar_transferencia_financeira = ExecutarTransferenciaFinanceira()
    actual = executar_transferencia_financeira.transferir(
        test_argument_correlation_id, test_argument_conta_id_origem, 
        test_argument_conta_id_destion, test_argument_valor
        )

    error_message = "Mensagem de sucesso não condiz com o esperado"

    assert actual == expect_message, error_message

# Teste de método de transferir com falha
def test_failed_transferir_method():
    test_argument_correlation_id = 1
    test_argument_conta_id_origem = 2147483649 
    test_argument_conta_id_destion = 210385733
    test_argument_valor = 10

    expect_message = "Transacao numero 1 foi cancelada por falta de saldo"

    executar_transferencia_financeira = ExecutarTransferenciaFinanceira()
    actual = executar_transferencia_financeira.transferir(
        test_argument_correlation_id, test_argument_conta_id_origem, 
        test_argument_conta_id_destion, test_argument_valor
        )

    error_message = "Mensagem de falha não condiz com o esperado"

    assert actual == expect_message, error_message