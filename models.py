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

        # atributo saldos removido, pois não era utilizado

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

            return item_atualizado


        except Exception as error:
            print(error)


class ExecutarTransferenciaFinanceira (AcessoDados):    
    def transferir(self, correlation_id, conta_origem, conta_destino, valor):
        conta_saldo_origem = self.getSaldo(conta_origem)

        if (conta_saldo_origem.saldo < valor):
            print(f"Transacao numero {correlation_id} foi cancelada por falta de saldo")
        else:
            conta_saldo_destino = self.getSaldo(conta_destino)

            conta_saldo_origem = self.atualizar(conta_origem, (conta_saldo_origem.saldo - valor))
            conta_saldo_destino = self.atualizar(conta_destino, (conta_saldo_destino.saldo + valor))

            print(f"Transacao numero {correlation_id} foi efetivada com sucesso! Novos saldos: Conta Origem:{conta_saldo_origem.saldo} | Conta Destino: {conta_saldo_destino.saldo}")