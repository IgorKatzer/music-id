# ADR-0004: Fila de processamento entre API e worker no PostgreSQL

- Status: Aceito
- Data: 2026-11-06
- Decidido por: Igor Katzer (Product Owner)

## Contexto

O ADR-0003 definiu dois processos: a API recebe o áudio e o worker faz o processamento pesado (fingerprint e busca). Falta decidir como a API entrega o pedido ao worker.

Requisitos para o MVP:

- um pedido não pode se perder se a API ou o worker reiniciar;
- dois workers nunca podem processar o mesmo pedido ao mesmo tempo;
- deve ser possível rodar mais de um worker;
- o volume esperado é baixo (dezenas de pedidos por minuto, não milhares por segundo);
- o mínimo possível de infraestrutura nova, com um único desenvolvedor.

## Alternativas consideradas

1. **Tarefas em segundo plano dentro da API (BackgroundTasks do FastAPI).** Não exige nada novo. Mas o processamento volta a rodar no processo da API, o que contraria o ADR-0003, e os pedidos em andamento se perdem se a API reiniciar.
2. **Redis com uma biblioteca de filas (RQ, Celery ou arq).** É o padrão de mercado, rápido e com retentativas prontas. Acrescenta um serviço para subir, monitorar e manter, e o estado do pedido fica dividido entre Redis e PostgreSQL.
3. **RabbitMQ.** Broker completo, com roteamento e garantias de entrega. É muito mais do que o MVP precisa.
4. **Fila numa tabela do PostgreSQL.** Os workers pegam pedidos com `SELECT ... FOR UPDATE SKIP LOCKED`, que trava a linha escolhida e faz os outros workers pularem linhas já travadas. Não acrescenta infraestrutura, e o pedido e seu resultado ficam no mesmo banco, na mesma transação. O limite é a vazão: para volumes muito altos, um broker dedicado escala melhor.

Dentro da alternativa 4, há a opção de usar uma biblioteca pronta de fila sobre PostgreSQL (por exemplo, procrastinate) ou implementar uma tabela própria. A implementação própria fica em algumas dezenas de linhas, não traz dependência nova e deixa explícito como a fila funciona.

## Decisão

Alternativa 4, com implementação própria.

- Tabela `jobs` com, no mínimo: identificador, tipo do pedido, dados de entrada, status (`pending`, `running`, `done`, `failed`), número de tentativas, horário em que foi travado e resultado ou erro.
- A API insere o pedido com status `pending` e devolve o identificador ao cliente.
- O worker, em laço, pega o próximo pedido `pending` com `FOR UPDATE SKIP LOCKED`, marca como `running`, processa e grava o resultado como `done` ou o erro como `failed`.
- Quando não há pedidos, o worker espera um intervalo curto antes de consultar de novo (polling).

## Consequências

- Nenhum serviço novo: a fila usa o PostgreSQL que já existe.
- A entrega é "pelo menos uma vez": se um worker cair depois de processar e antes de gravar o resultado, o pedido pode ser processado de novo. Por isso o processamento precisa ser idempotente, isto é, rodar duas vezes o mesmo pedido deve dar o mesmo resultado sem efeitos duplicados.
- Pedidos travados por um worker que morreu precisam de um tempo limite: passado esse tempo, o pedido volta para `pending`. Também é preciso um limite de tentativas, depois do qual o pedido fica `failed`.
- O polling acrescenta uma pequena latência (o intervalo de espera). Se ela pesar na meta de tempo de resposta do PRD, dá para usar `LISTEN/NOTIFY` do PostgreSQL para acordar o worker na hora.
- Os futuros motores de cover e humming entram como novos tipos de pedido na mesma tabela, consumidos por workers próprios.
- Se o volume crescer a ponto de a tabela virar gargalo, a troca por Redis ou RabbitMQ será registrada num novo ADR. Como a fila fica atrás de uma interface do módulo `worker`, a troca não afeta o resto do código.
