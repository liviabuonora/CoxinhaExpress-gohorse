# Cantina CESAR (versão go-horse)

App de linha de comando para fazer os 15 minutos do intervalo renderem: o aluno pede antes, paga e recebe um aviso quando o pedido está pronto. Esta é a **Entrega 1 (go-horse)** do Hackathon Relâmpago #1 de FDS 2026.2: funciona, mas o código está cru de propósito.

## Decisões da stack
- Python 3, sem dependências externas e sem banco de dados (os pedidos ficam em memória).
- Um único arquivo (`app.py`) para ir rápido. IA liberada para ajudar a escrever o código.

## Equipe:
- Antônio Marcos
- Arthur Florencio
- Cecília de Moraes
- Lívia Buonora
- Luiza Beltrão
- Silvio Ronaldo 
- Victor Bacelar

## O que é o app
- Cardápio fixo (coxinha, pastel, sanduíche, suco, refri, água).
- Pedido com combo automático: cada comida + bebida ganha R$ 1,50 de desconto.
- Pagamento por Pix, cartão ou dinheiro (com troco).
- Estimativa de fila (2 minutos por pedido pendente) e aviso de "pedido pronto".

## Como rodar
```bash
python app.py        # menu interativo
python app.py demo   # cenário pronto
```

## Onde estão os princípios no código
Ainda não estão, e esse é o ponto desta versão. Os problemas que a versão final vai corrigir:
- `fazer_pedido` faz tudo (preço, desconto, pagamento, gravação, fila e print): **falta Responsabilidade Única e coesão**.
- O pagamento é um `if/elif` dentro da função: **para criar um meio novo é preciso editar o código existente (fere Aberto/Fechado)**.
- Variáveis globais (`pedidos`, `proximo`, `precos`): **acoplamento alto e sem ocultamento de informação**.
- Regras de negócio misturadas com `print`: **não dá para trocar o aviso por WhatsApp sem reescrever tudo (fere Inversão de Dependências)**.

A versão final está em outro repositório, com o antes e depois comparado.
