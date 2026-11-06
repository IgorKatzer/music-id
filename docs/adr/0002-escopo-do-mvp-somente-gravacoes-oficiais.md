# ADR-0002: Escopo do MVP: somente gravações oficiais, por fingerprint

- Status: Aceito
- Data: 2026-10-12
- Decidido por: Igor Katzer (Product Owner)

## Contexto

O contrato do produto (PRD, seção 7) prevê identificar músicas a partir de várias entradas: gravação oficial, ao vivo, cover, cantarolar, letra, instrumental, fingerstyle e áudio degradado. Só a gravação oficial pode ser resolvida com uma técnica madura e bem documentada, o fingerprint de áudio. As demais dependem de pesquisa cujo resultado é incerto.

Ainda não existe nenhuma parte do sistema construída: captura de áudio, API, processamento, banco e tela de resultado precisam ser feitos do zero.

## Alternativas consideradas

1. **MVP só com fingerprint (gravações oficiais).** Usa uma técnica conhecida e permite validar a arquitetura inteira de ponta a ponta. Não entrega ainda o diferencial do produto em relação ao Shazam.
2. **MVP "identificação universal" (oficial, ao vivo, cover e cantarolar).** Entrega o diferencial desde o início, mas mistura dois riscos ao mesmo tempo: construir a infraestrutura e resolver problemas de pesquisa. Se algo falhar, fica difícil saber onde está o problema.

## Decisão

Alternativa 1. O primeiro MVP identifica somente gravações oficiais, por fingerprint de áudio, cobrindo os requisitos RF-001 a RF-006 do PRD.

## Consequências

- O MVP funciona, na prática, como um identificador no estilo do Shazam, sobre um catálogo de domínio público ou com licença aberta.
- A arquitetura construída no MVP (captura, API, banco, tela de resultado) deve ser reaproveitada pelos próximos motores, e não descartada. Por isso o modelo de dados já separa composição de gravação (ADR-0001).
- As metas de acerto para ao vivo, cover e cantarolar passam a valer só depois do MVP.
- A tela de resultado já nasce com os campos de confiança e forma de identificação, mesmo que no MVP a forma seja sempre "áudio oficial".
