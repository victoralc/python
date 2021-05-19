def create_account(numero, titular, saldo, limite):
    account = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}  # Object representation
    return account


def deposita(conta, valor):
    conta["saldo"] += valor


def saca(conta, valor):
    conta["saldo"] -= valor


def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))


if __name__ == '__main__':
    conta = create_account(123, "Victor", 55.0, 1000.0)
    deposita(conta, 1000)
    saca(conta, 100)
    extrato(conta)
