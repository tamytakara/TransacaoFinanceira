class ContaSaldo:
    def __init__(self, conta, saldo):
        self.conta = conta
        self.saldo = saldo


class AcessoDados:
    def __init__(self):
        self.tabela_saldos = []
        self.tabela_saldos.append(ContaSaldo(938485762, 180))
        self.tabela_saldos.append(ContaSaldo(347586970, 1200))
        self.tabela_saldos.append(ContaSaldo(2147483649, 0))
        self.tabela_saldos.append(ContaSaldo(675869708, 4900))
        self.tabela_saldos.append(ContaSaldo(238596054, 478))
        self.tabela_saldos.append(ContaSaldo(573659065, 787))
        self.tabela_saldos.append(ContaSaldo(210385733, 10))
        self.tabela_saldos.append(ContaSaldo(674038564, 400))
        self.tabela_saldos.append(ContaSaldo(563856300, 1200))

        self.saldos = {}
        self.saldos[938485762] = 180

    def getSaldo(self, id):
        return next((x for x in self.tabela_saldos if x.conta == id), None)

    def atualizar(self, conta, saldo):
        try:
            item_atualizado = ContaSaldo(conta, saldo)
            for x in self.tabela_saldos:
                if x.conta == item_atualizado.conta:
                    index = x
            self.tabela_saldos.remove(index)
            self.tabela_saldos.append(item_atualizado)

        except Exception as error:
            print(error)


class ExecutarTransferenciaFinanceira (AcessoDados):    
    def transferir(self, correlation_id, conta_origem, conta_destino, valor):
        conta_saldo_origem = self.getSaldo(conta_origem)

        if (conta_saldo_origem.saldo < valor):
            print(f"Transacao numero {correlation_id} foi cancelada por falta de saldo")
        else:
            conta_saldo_destino = self.getSaldo(conta_destino)
            conta_saldo_origem.saldo -= valor
            conta_saldo_destino.saldo += valor

            print(f"Transacao numero {correlation_id} foi efetivada com sucesso! Novos saldos: Conta Origem:{conta_saldo_origem.saldo} | Conta Destino: {conta_saldo_destino.saldo}")

if __name__ == "__main__":
    transacoes = []

    transacoes.append({"correlation_id": 1, "datetime": "09/09/2023 14:15:00", "conta_origem": 938485762, "conta_destino": 2147483649, "VALOR": 150})
    transacoes.append({"correlation_id": 2, "datetime": "09/09/2023 14:15:05", "conta_origem": 2147483649, "conta_destino": 210385733, "VALOR": 149})
    transacoes.append({"correlation_id": 3, "datetime": "09/09/2023 14:15:29", "conta_origem": 347586970, "conta_destino": 238596054, "VALOR": 1100})
    transacoes.append({"correlation_id": 4, "datetime": "09/09/2023 14:17:00", "conta_origem": 675869708, "conta_destino": 210385733, "VALOR": 5300})
    transacoes.append({"correlation_id": 5, "datetime": "09/09/2023 14:18:00", "conta_origem": 238596054, "conta_destino": 674038564, "VALOR": 1489})
    transacoes.append({"correlation_id": 6, "datetime": "09/09/2023 14:18:20", "conta_origem": 573659065, "conta_destino": 563856300, "VALOR": 49})
    transacoes.append({"correlation_id": 7, "datetime": "09/09/2023 14:19:00", "conta_origem": 938485762, "conta_destino": 2147483649, "VALOR": 44})
    transacoes.append({"correlation_id": 8, "datetime": "09/09/2023 14:19:01", "conta_origem": 573659065, "conta_destino": 675869708, "VALOR": 150})

    executor = ExecutarTransferenciaFinanceira()

    # como as transferências tem o campo de datetime sequencial não faz sentido seguir com paralelismo da execução das transferências
    for transacao in transacoes:
        executor.transferir(transacao["correlation_id"], transacao["conta_origem"], transacao["conta_destino"], transacao["VALOR"])
        
