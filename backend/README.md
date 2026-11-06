# backend

Python + FastAPI, monólito modular (ver `docs/adr/0003-stack-do-mvp.md`).

Roda como dois processos a partir do mesmo código:

- **api**: recebe o áudio, registra o pedido na fila e devolve o resultado.
- **worker**: consome a fila, gera o fingerprint e faz a busca no catálogo.

Módulos:

| Módulo | Responsabilidade |
|--------|------------------|
| `api` | Endpoints HTTP e WebSocket |
| `worker` | Consumo da fila e orquestração do processamento |
| `fingerprint` | Espectrograma, picos e hashes |
| `matching` | Busca dos hashes e alinhamento temporal |
| `catalog` | Composições, gravações e ingestão do catálogo aberto |

Regra: um módulo só usa outro pela interface pública dele e nunca acessa as tabelas de outro módulo diretamente.
