# ADR-0003: Stack do MVP

- Status: Aceito
- Data: 2026-11-06
- Decidido por: Igor Katzer (Product Owner)

## Contexto

O MVP identifica gravações oficiais por fingerprint em um catálogo aberto (ADR-0002). O fluxo é: gravar alguns segundos de áudio no navegador, gerar o espectrograma, encontrar os picos de frequência, gerar hashes a partir de pares de picos, buscar esses hashes no banco e conferir se os acertos se alinham no tempo.

Nesse fluxo não há modelo de IA, embeddings nem busca vetorial. O processamento de áudio é pesado em CPU. O projeto tem um único desenvolvedor.

O esboço inicial da descoberta previa React no front, uma API em Node.js e serviços de IA em Python.

## Alternativas consideradas

### Back end

1. **Node.js na API e Python no processamento de áudio.** Permite praticar Node. No MVP, porém, o Node só repassaria o áudio para o Python: seriam duas linguagens no back end, dois serviços e uma chamada de rede a mais, sem ganho funcional.
2. **Python com FastAPI para tudo.** O ecossistema de processamento de áudio (numpy, scipy, librosa) está em Python, e o FastAPI cobre upload, API REST e WebSocket.

### Estrutura

1. **Microsserviços desde o início.** Antecipa uma separação que pode ser necessária quando entrarem os motores de embeddings e humming (GPU, processamento lento, escala própria). Em troca, traz desde o primeiro dia comunicação em rede, falhas parciais, deploy de vários serviços e depuração entre processos, além do risco de fixar fronteiras erradas antes de o código existir.
2. **Monólito modular.** Um único código, com módulos que só se comunicam por interfaces definidas e não acessam as tabelas uns dos outros. Extrair um módulo depois passa a ser colocar uma API na frente da interface, não reescrever.

### Algoritmo de fingerprint

1. **Chromaprint (AcoustID).** Pensado para identificar arquivos inteiros; não é adequado a trechos curtos e ruidosos gravados por microfone.
2. **Dejavu ou audfprint.** Seguem a abordagem certa (picos e hashes), mas são projetos antigos e pouco mantidos.
3. **Implementação própria no estilo de Wang (2003).** Algumas centenas de linhas de Python, é o núcleo técnico do produto e o projeto passa a dominar o próprio motor. Dejavu e audfprint servem de referência.

## Decisão

| Camada | Escolha |
|--------|---------|
| Front end | React + TypeScript + Vite, como aplicação web |
| Back end | Python + FastAPI, sem Node.js |
| Estrutura | Monólito modular, executado como dois processos: API e worker |
| Processamento de áudio | numpy, scipy e librosa; fingerprint próprio no estilo de Wang |
| Banco | PostgreSQL |
| Ambiente | Docker Compose, em WSL2 no Windows |
| Testes | pytest no back end, Vitest no front end |

Módulos iniciais do back end: `api`, `worker`, `fingerprint`, `matching`, `catalog`.

A API recebe o áudio e registra um pedido de processamento numa fila; o worker consome a fila e executa o fingerprint e a busca. Assim o processamento pesado não roda dentro da requisição HTTP e não trava a API.

## Consequências

- Um único código Python e um único banco no MVP.
- Fingerprints ficam numa tabela com índice no hash (busca exata, não por similaridade). Composição e gravação ficam em tabelas próprias (ADR-0001).
- Quando os embeddings entrarem, a extensão pgvector permite busca vetorial no mesmo PostgreSQL. Um banco vetorial dedicado só entra se o volume exigir, com ADR próprio.
- O worker é o ponto natural de separação futura: os motores de embeddings e humming devem nascer como workers separados, consumindo a mesma fila.
- O navegador só libera o microfone em `localhost` ou em HTTPS; o deploy precisará de HTTPS.
- Node.js fica fora do projeto. Se um gateway em Node fizer sentido no futuro, entra com ADR próprio.
- O teste principal do MVP é o de acerto: faixas do catálogo com ruído adicionado e cortadas em trechos, medindo a meta de acerto do PRD a cada mudança.
- Ficam para ADRs futuros: tecnologia da fila, fonte do catálogo aberto, hospedagem e deploy.
