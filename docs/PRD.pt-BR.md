# PRD: Identificação musical por composição

- Versão: 0.2 (rascunho para revisão do Product Owner)
- Data: 2026-10-11
- Traduções: [English](PRD.md)
- Product Owner: Igor Katzer
- Nome do produto: a definir ("EchoMind" foi só uma sugestão provisória)

Este documento consolida as decisões da fase de descoberta. O que ainda não foi decidido está marcado como **Pendência** e listado na seção 13. Nenhum número de meta aqui é definitivo: todos precisam ser validados por experimento.

## 1. Problema

As ferramentas atuais de identificação musical dependem da semelhança com gravações conhecidas. Por isso, o usuário não consegue identificar uma música quando ela é executada de outra forma, como em apresentações ao vivo, covers ou quando é apenas cantarolada.

## 2. Missão

Permitir que qualquer pessoa identifique uma música independentemente da forma como ela é executada, reproduzida ou lembrada, e conectar essa descoberta aos serviços onde a música pode ser ouvida ou adquirida.

## 3. Visão

O produto é pensado em três camadas:

| Camada | O que é | Horizonte |
|--------|---------|-----------|
| MVP | Identificação musical | Primeira entrega |
| Produto | Plataforma de descoberta musical: identificar por qualquer forma de entrada e levar o usuário até a música | Versões seguintes |
| Visão | Plataforma de inteligência musical: analisar arranjos, separar instrumentos, extrair acordes e gerar partitura ou tablatura para aprender a tocar | Longo prazo |

A camada de visão não faz parte do escopo deste PRD. Ela está registrada porque influencia decisões de arquitetura desde já (ver ADR-0001).

## 4. Princípios do produto

1. **Composição, não gravação.** O sistema responde "que música é essa?", e não "que gravação é essa?". O áudio pode mudar; a identidade da música permanece.
2. **Suficiência de evidência.** O sistema só afirma uma identificação quando tem evidência suficiente. Quando não tem, diz isso em vez de chutar.
3. **Complexidade musical escondida.** O usuário não precisa entender de música. Tonalidade, por exemplo, é ignorada na comparação.
4. **Entradas são evidências musicais.** Áudio, melodia cantarolada e trecho de letra são formas diferentes de evidência sobre a mesma obra.

## 5. Usuários

O público é amplo: pessoas que gostam de música. Em vez de uma persona restrita, o produto é definido pelas situações de uso da seção 6.

**Pendência:** definir uma persona inicial para orientar prioridades do MVP.

## 6. Casos de uso

| ID | Situação | Entrada | Principais desafios |
|----|----------|---------|---------------------|
| UC-001 | Banda da igreja toca uma música que o usuário não conhece | Áudio ao vivo pelo celular | Reverberação, outra voz, outro arranjo, público cantando, improvisos |
| UC-002 | Música tocando no rádio do carro | Áudio perto da caixa de som | Ruído, compressão, locutor, vinheta ou slogan da rádio no meio da música |
| UC-003 | Música de anime da infância, da qual o usuário só lembra a melodia | Cantarolar | Desafinação, ritmo imperfeito, memória parcial, sem letra, outra tonalidade |
| UC-004 | Música que contém sample de outra obra | Áudio | Não confundir o sample com a música principal |
| UC-005 | Usuário acorda com uma música na cabeça, sem saber nada sobre ela | Cantarolar ou assobiar | Lembrança incompleta, sem saber o gênero |
| UC-006 | Banda cover toca em um bar | Áudio ao vivo pelo celular | Cover, outro vocalista e arranjo, conversas, aplausos |

Resultado esperado em todos: a composição identificada, com os dados da obra original. Em UC-004, o resultado principal é a música que está tocando, com o sample informado à parte.

## 7. Contrato do produto: o que o sistema promete tentar identificar

| # | Entrada | Condição |
|---|---------|----------|
| 1 | Gravação oficial | De fontes oficiais ou licenciadas |
| 2 | Execução ao vivo | Mesmo com interpretação diferente da gravação original |
| 3 | Cover | Desde que a melodia original seja mantida. Com improvisos, basta captar um trecho sem improvisação |
| 4 | Cantarolar (humming) | Mínimo de 10 segundos, com informação melódica suficiente e minimamente no ritmo |
| 5 | Trecho cantado | Mesmo que só o refrão |
| 6 | Letra | Trecho falado, cantado ou citado, mesmo parcial |
| 7 | Instrumental | Música totalmente instrumental |
| 8 | Fingerstyle | Violão dedilhado, desde que a estrutura musical permita a correspondência |
| 9 | Áudio degradado | Rádio, ruído, conversas, aplausos, vinhetas, desde que haja informação musical suficiente |
| 10 | Acordes (futuro) | Sequência tocada com clareza, na ordem e no ritmo da música. Acordes soltos não contam |

Tonalidade é tratada como variável: mudança de tom não deve impedir a identificação.

Qualquer entrada fora dessa tabela não é aceita. Nesses casos, e quando a evidência for insuficiente, o sistema informa que não tem informação suficiente.

## 8. Resultado apresentado ao usuário

Quando a confiança atinge o limiar mínimo do modo de reconhecimento, a tela mostra:

- nome da música;
- artista ou grupo original;
- álbum e ano da obra original (em um cover, os dados são os da obra original, não os do cover);
- porcentagem de confiança;
- forma de identificação: áudio oficial, apresentação ao vivo, cover, rádio, humming, voz, instrumental ou fingerstyle, trecho da letra;
- links para Spotify, Apple Music e YouTube (este último só quando houver vídeo oficial).

Quando nenhum candidato atinge o limiar, o sistema não afirma uma identificação. Ele informa que não conseguiu identificar com confiança suficiente e lista os candidatos mais prováveis, com a pergunta "É alguma dessas?".

Ideias para versões futuras, fora do MVP: detalhamento de por que a música foi identificada (melodia, letra, ritmo), uso da resposta do usuário para melhorar o sistema, links para cifra e partitura.

## 9. Requisitos funcionais (rascunho)

As prioridades seguem o escopo do MVP decidido na seção 11.

| ID | Requisito | Prioridade |
|----|-----------|---------------------|
| RF-001 | Capturar áudio pelo microfone do dispositivo | MVP |
| RF-002 | Identificar uma gravação oficial a partir do áudio captado | MVP |
| RF-003 | Apresentar o resultado com os campos da seção 8 | MVP |
| RF-004 | Apresentar uma pontuação de confiança e só afirmar a identificação acima do limiar do modo | MVP |
| RF-005 | Abaixo do limiar, listar os candidatos mais prováveis sem afirmar nenhum | MVP |
| RF-006 | Tolerar trechos descontínuos e interrupções, como vinhetas de rádio | MVP |
| RF-007 | Identificar execuções ao vivo e covers pela composição | Pós-MVP |
| RF-008 | Identificar por cantarolar, com mínimo de 10 segundos | Pós-MVP |
| RF-009 | Identificar por trecho de letra falado, cantado ou digitado | Pós-MVP |
| RF-010 | Identificar músicas instrumentais e em fingerstyle | Pós-MVP |
| RF-011 | Diferenciar sample, interpolação, cover e remix, informando o sample à parte | Pós-MVP |
| RF-012 | Identificar por sequência de acordes | Futuro |

**Pendência:** tempo máximo de gravação por consulta.

## 10. Requisitos não funcionais e métricas

Metas provisórias, propostas como ponto de partida. Serão ajustadas depois dos primeiros experimentos.

| Métrica | Meta provisória | Vale a partir de |
|---------|-----------------|------------------|
| Acerto em gravações oficiais | ≥ 98% | MVP |
| Acerto em gravações com ruído | ≥ 95% | MVP |
| Resposta correta entre os 5 primeiros candidatos | ≥ 95% | MVP |
| Tempo de resposta | < 3 s em 95% das buscas | MVP |
| Acerto em ao vivo e covers | ≥ 90% | Pós-MVP |
| Acerto em cantarolar | ≥ 85% | Pós-MVP |

A meta geral declarada pelo Product Owner é um mínimo de 90% de acerto.

Observações:

- A pontuação de um modelo não é automaticamente uma probabilidade. A porcentagem exibida precisa ser calibrada antes de ser mostrada como confiança.
- O limiar mínimo é definido por modo de reconhecimento, e não um valor único para tudo.
- Toda meta só é mensurável com um conjunto de teste definido. **Pendência:** montar esse conjunto.

## 11. Escopo do MVP

**Decidido (ADR-0002):** o primeiro MVP identifica apenas gravações oficiais, por fingerprint, em um catálogo de referência com músicas em domínio público ou com licença aberta.

- Entram no MVP: RF-001 a RF-006.
- Ficam para versões seguintes: execuções ao vivo, covers, cantarolar, letra, instrumental, fingerstyle e samples (RF-007 a RF-012).

O objetivo do MVP é validar a arquitetura de ponta a ponta (captura, API, processamento, banco e tela de resultado) com uma técnica conhecida, antes de construir o diferencial do produto sobre ela.

## 12. Fora do escopo deste PRD

- Análise musical: separação de instrumentos, acordes, BPM, tom.
- Geração de partitura e tablatura.
- Contas de usuário e histórico de buscas.
- Exibição de letras completas.

## 13. Riscos e pendências

### Riscos

| Risco | Impacto | Tratamento proposto |
|-------|---------|---------------------|
| Catálogo de referência: gravações comerciais e letras são protegidas por direitos autorais | Sem catálogo, não há o que reconhecer nem como medir as metas | Começar com domínio público e licenças abertas; estudar licenciamento antes de qualquer uso comercial |
| Identificar ao vivo, cover e cantarolar é problema de pesquisa em aberto | Metas da seção 10 podem não ser alcançáveis | Tratar as metas como hipóteses e medir cedo |
| Similaridade não é identidade (samples, interpolações) | Atribuições erradas | Modelo de dados separando composição de gravação (ADR-0001) |
| Áudio de voz de usuários é dado pessoal | Obrigações legais (LGPD) | No desenvolvimento, usar só gravações do autor; definir política antes de ter usuários |

### Pendências

1. Nome do produto.
2. Persona inicial.
3. Tempo máximo de gravação por consulta.
4. Conjunto de teste para medir as metas.
5. Fonte do catálogo de referência.
6. Plataforma do primeiro cliente: web ou aplicativo móvel.
7. Decisões de arquitetura, listadas em `docs/adr/README.md`.

## 14. Histórico

| Versão | Data | Mudança |
|--------|------|---------|
| 0.1 | 2026-10-11 | Primeira consolidação da fase de descoberta |
| 0.2 | 2026-10-12 | Escopo do MVP decidido: somente gravações oficiais, por fingerprint (ADR-0002) |
