from models import ExecutarTransferenciaFinanceira


def gerar_transferencias():
    transacoes = []

    transacoes.append({"correlation_id": 1, "datetime": "09/09/2023 14:15:00", "conta_id_origem": 938485762, "conta_id_destino": 2147483649, "VALOR": 150})
    transacoes.append({"correlation_id": 2, "datetime": "09/09/2023 14:15:05", "conta_id_origem": 2147483649, "conta_id_destino": 210385733, "VALOR": 149})
    transacoes.append({"correlation_id": 3, "datetime": "09/09/2023 14:15:29", "conta_id_origem": 347586970, "conta_id_destino": 238596054, "VALOR": 1100})
    transacoes.append({"correlation_id": 4, "datetime": "09/09/2023 14:17:00", "conta_id_origem": 675869708, "conta_id_destino": 210385733, "VALOR": 5300})
    transacoes.append({"correlation_id": 5, "datetime": "09/09/2023 14:18:00", "conta_id_origem": 238596054, "conta_id_destino": 674038564, "VALOR": 1489})
    transacoes.append({"correlation_id": 6, "datetime": "09/09/2023 14:18:20", "conta_id_origem": 573659065, "conta_id_destino": 563856300, "VALOR": 49})
    transacoes.append({"correlation_id": 7, "datetime": "09/09/2023 14:19:00", "conta_id_origem": 938485762, "conta_id_destino": 2147483649, "VALOR": 44})
    transacoes.append({"correlation_id": 8, "datetime": "09/09/2023 14:19:01", "conta_id_origem": 573659065, "conta_id_destino": 675869708, "VALOR": 150})

    return transacoes

if __name__ == "__main__":
    transacoes = gerar_transferencias()
    # TODO: necessário criar ordenação das transacoes por datetime
    # Atualmente a lista já vem ordenada, mas é necessário criar essa verificação

    executor = ExecutarTransferenciaFinanceira()

    # como as transferências tem o campo de datetime sequencial não faz sentido seguir com paralelismo da execução das transferências
    for transacao in transacoes:
        print(executor.transferir(transacao["correlation_id"], transacao["conta_id_origem"], transacao["conta_id_destino"], transacao["VALOR"]))
        
