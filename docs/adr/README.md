# Architecture Decision Records

Cada ADR registra uma decisão técnica e o motivo dela. ADRs não são editados depois de aceitos: se a decisão mudar, cria-se um novo ADR que substitui o anterior.

| Nº | Título | Status |
|----|--------|--------|
| [0001](0001-separar-composicao-de-gravacao.md) | Separar composição de gravação no modelo de dados | Proposto |
| [0002](0002-escopo-do-mvp-somente-gravacoes-oficiais.md) | Escopo do MVP: somente gravações oficiais, por fingerprint | Aceito |
| [0003](0003-stack-do-mvp.md) | Stack do MVP | Aceito |

## Decisões que ainda precisam de ADR

- Tecnologia da fila entre API e worker
- Busca vetorial dedicada (só se o volume exigir; ver ADR-0003)
- Fonte do catálogo de referência
- Como combinar as evidências dos motores e calibrar a confiança

Modelo para novos ADRs: [`0000-modelo.md`](0000-modelo.md).
