# CANTINA CESAR - versao go-horse (24h, sem pensar muito)
# Funciona, mas esta feio de proposito: tudo num arquivo, variaveis globais,
# if/elif para pagamento, regras de preco misturadas com print.
import sys

precos = {"coxinha": 6.0, "pastel": 7.0, "sanduiche": 9.0, "suco": 5.0, "refri": 6.0, "agua": 3.0}
pedidos = []
proximo = 1


def fazer_pedido(aluno, itens, pagamento, valor_pago=0):
    global proximo
    total = 0
    for i in itens:
        if i in precos:
            total = total + precos[i]
        else:
            print("item nao existe: " + i)
            return None

    # combo: cada comida + bebida ganha R$ 1,50 de desconto
    comidas = 0
    bebidas = 0
    for i in itens:
        if i == "coxinha" or i == "pastel" or i == "sanduiche":
            comidas = comidas + 1
        if i == "suco" or i == "refri" or i == "agua":
            bebidas = bebidas + 1
    combos = min(comidas, bebidas)
    total = total - combos * 1.5

    # pagamento
    if pagamento == "pix":
        print("Gerando QR Code Pix de R$ %.2f" % total)
        print("Pix confirmado!")
    elif pagamento == "cartao":
        print("Passando cartao de R$ %.2f" % total)
        if total > 100:
            print("cartao recusado")
            return None
        print("Cartao aprovado!")
    elif pagamento == "dinheiro":
        if valor_pago < total:
            print("dinheiro insuficiente")
            return None
        print("Troco: R$ %.2f" % (valor_pago - total))
    else:
        print("pagamento invalido")
        return None

    pedido = {"id": proximo, "aluno": aluno, "itens": itens, "total": total, "status": "recebido"}
    proximo = proximo + 1
    pedidos.append(pedido)

    # estima a fila: 2 minutos por pedido pendente
    fila = 0
    for p in pedidos:
        if p["status"] == "recebido":
            fila = fila + 1
    print("Pedido #%d de %s recebido. Total R$ %.2f. Fila estimada: %d min" % (pedido["id"], aluno, total, fila * 2))
    return pedido


def pedido_pronto(id):
    for p in pedidos:
        if p["id"] == id:
            p["status"] = "pronto"
            print("Aviso para %s: seu pedido #%d esta pronto!" % (p["aluno"], id))
            return
    print("pedido nao encontrado")


def main():
    print("=== CANTINA CESAR (go-horse) ===")
    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        fazer_pedido("Ana", ["coxinha", "suco"], "pix")
        fazer_pedido("Bruno", ["pastel", "refri", "agua"], "dinheiro", 20)
        fazer_pedido("Carla", ["sanduiche"], "cartao")
        pedido_pronto(1)
        return
    while True:
        print("\n1) Fazer pedido  2) Marcar pedido pronto  3) Sair")
        op = input("> ")
        if op == "1":
            aluno = input("Nome do aluno: ")
            print("Itens disponiveis: " + ", ".join(precos.keys()))
            itens = input("Itens (separados por virgula): ").replace(" ", "").split(",")
            pag = input("Pagamento (pix/cartao/dinheiro): ")
            valor = 0
            if pag == "dinheiro":
                valor = float(input("Valor entregue: "))
            fazer_pedido(aluno, itens, pag, valor)
        elif op == "2":
            pedido_pronto(int(input("Numero do pedido: ")))
        elif op == "3":
            break


if __name__ == "__main__":
    main()
