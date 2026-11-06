# ADR-0001: Separar composição de gravação no modelo de dados

- Status: Proposto
- Data: 2026-10-11

## Contexto

O princípio central do produto é identificar a composição, e não uma gravação específica (PRD, seção 4). A mesma composição pode existir como gravação original, remaster, ao vivo, cover, versão acústica ou remix, e um trecho de uma gravação pode aparecer como sample dentro de outra obra.

Quando o usuário ouve um cover, o resultado deve mostrar a obra original, com artista, álbum e ano dela (PRD, seção 8). Quando ouve uma música que contém um sample, o resultado deve ser a música que está tocando, com o sample informado à parte (PRD, UC-004).

## Alternativas consideradas

1. **Uma entidade só ("música" = arquivo de áudio).** É o mais simples e basta para um reconhecedor de gravações oficiais. Não consegue representar que duas gravações são a mesma música, nem a relação de sample entre obras. Migrar depois exige reestruturar o banco e reindexar o catálogo.
2. **Duas entidades: composição e gravação.** Cada gravação aponta para uma composição. Fingerprints pertencem à gravação; melodia e letra pertencem à composição. Custa um pouco mais de modelagem e de cadastro no catálogo.
3. **Modelo completo de obra, com relações entre obras desde o início** (sample, interpolação, remix, medley). Cobre todos os casos, mas adiciona complexidade que o MVP não usa.

## Decisão

Adotar a alternativa 2 desde o primeiro esquema do banco. As relações entre obras da alternativa 3 ficam para um ADR futuro, quando o caso de uso de sample entrar no escopo.

## Consequências

- O resultado de uma busca sempre aponta para uma composição; a gravação que casou é uma evidência.
- No MVP de fingerprint, cada composição terá normalmente uma única gravação. O custo extra é pequeno e evita a migração depois.
- O catálogo precisa de metadados nos dois níveis: da composição (título, autor) e da gravação (intérprete, álbum, ano, tipo).
- Composições com mais de uma gravação exigem um critério de qual gravação é a "original" para exibir álbum e ano.
