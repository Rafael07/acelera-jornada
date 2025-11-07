# Teste Técnico SQL – Acelera Jornada de Dados

## Objetivo

Entender e aplicar as diferenças entre as funções de janela ROW_NUMBER(), RANK() e DENSE_RANK(). Essas funções são fundamentais para resolver problemas de classificação e segmentação em SQL, e aparecem com frequência em entrevistas técnicas.

Sua missão é:

1. Gerar rankings de usuários com base em uma métrica (quantidade de e-mails enviados).
2. Comparar os resultados usando ROW_NUMBER(), RANK() e DENSE_RANK().
3. Explicar a diferença prática entre os três métodos.

---

## Dataset de Entrada

<div align="center">

| id | from_user | to_user | day |
|----|-----------|---------|-----|
| 1  | ana       | bruno   | 1   |
| 2  | ana       | carlos  | 1   |
| 3  | bruno     | daniela | 1   |
| 4  | carlos    | ana     | 2   |
| 5  | ana       | daniela | 2   |
| 6  | bruno     | carlos  | 2   |
| 7  | ana       | erica   | 3   |

</div>

---

## Regras de Validação

* O usuário com mais e-mails enviados deve estar no topo (rank = 1).
* Em caso de empate:
    * ROW_NUMBER() → sempre gera valores únicos (não permite empate, usa a ordem alfabética como desempate).
    * RANK() → mantém empates, mas pula posições (ex.: 1, 1, 3).
    * DENSE_RANK() → mantém empates, mas não pula posições (ex.: 1, 1, 2).

---

## Critérios de Avaliação

* ✅ Consulta correta para contar e-mails enviados por usuário.
* ✅ Uso das três funções de ranking (ROW_NUMBER, RANK, DENSE_RANK).
* ✅ Explicação clara da diferença prática entre os resultados.
* ⭐ Bônus: aplicação em outro contexto (clientes, produtos, categorias).

---